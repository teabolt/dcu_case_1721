#!/usr/bin/env python3
# Done by Tomas Baltrunas, student number 17350793, Computer Applications Year 2. For CA216 2019 shell assignment.

"""Shell engines"""

import cmd
import sys
import os
import os.path
import stat
import datetime
import shutil
import subprocess

from parsing import InternalCommandParser, SpecialCharacterParser, ManualParser
from utils import slice_to_list, strip_around_lines


class Sheller(cmd.Cmd):
    """The hottest shell in the game"""

    # class variables

    # ANSI colouring codes to make the terminal in colours (available only on some platforms)
    COLOURS = {
        'black': '30',
        'red': '31',
        'bold_red': '1;31',
        'green': '32',
        'bold_green': '1;32',
        'yellow': '33',
        'yellow_bold': '1;33',
        'blue': '34',
        'magenta': '35',
        'bold_magenta':'1;35',
        'cyan': '36',
        'white': '37',
        'bold_white': '1;37',
    }

    SEMANTIC_COLOURS = {
        'err': 'bold_red',
        'prompt': 'bold_green',
        'command': 'white',
        'quit': 'yellow_bold',
        'manprompt': 'bold_white',
        'intro': 'bold_magenta',
        'isdir': 'yellow',
        'isfile': 'cyan',
    }
    # to refactor, move this into the shell classes that support ANSI colour codes


    # method overrides

    def __init__(self, completekey='tab', stdin=None, stdout=None, stderr=None, argv=None, shell_path=None, batchmode=False):
        """Initialise the shell"""
        # call cmd's constructor implementation
        super().__init__(completekey=completekey, stdin=stdin, stdout=stdout)

        # set stderr pointer
        if stderr is None:
            # report errors to stdout
            # may want to consider using sys.stderr
            stderr = stdout 
        self.stderr = stderr

        # original launch configuration (used for restarting the shell)
        self.sysargv = argv # argument vector to the 'myshell.py' call
        self.orig_dir = os.getcwd() # directory where the shell was launched from

        # initialise parsers
        self.internalparser = InternalCommandParser()
        self.specialparser = SpecialCharacterParser()

        # initialise the manual
        self.manual = os.path.abspath('readme')
        self.manualparser = ManualParser(self.manual)

        # get a table of contents
        toc = self.manualparser.get_table_of_contents()
        command_prefix = 'command-'
        if not toc:
            self.toc_infotopics = None
            self.toc_commands = None
        else: 
            commands = list(filter(lambda c: c.startswith(command_prefix), toc))
            nocommands = list(filter(lambda c: not c.startswith(command_prefix), toc))
            # may want to use set difference

            commands = [comm[len(command_prefix):] for comm in commands] # remove prefix
            self.toc_infotopics = nocommands
            self.toc_commands = commands

        # initialise list of child processes (for background execution)
        self.subprocesses = []

        # get the path where the shell resides (before the user can change directory)
        if shell_path is None:
            # 'myshell.py' did not supply its location
            shell_path = os.path.realpath(__file__)

        # update environment variables
        os.environ['SHELL'] = shell_path
        # introduce the PWD environment variable (needed on certain platforms)
        os.environ['PWD'] = os.getcwd() 

        # initialise batch mode if needed
        if batchmode:
            self.use_rawinput = 0
        self.batchmode = batchmode

    def onecmd(self, line):
        # parse the line into its command and arguments
        cmd, arg, line = self.parseline(line)
        # this method allows arguments to follow just after the command, eg: 'cd..' instead of 'cd ..'
        # the method also tries to find only the first alphanumeric or underscore character, so commands without such characters get ignored

        if not line:
            # no input, do nothing
            pass
        elif line == '^':
            # repeat the last command if available
            return self.emptyline()
        elif line == 'EOF':
            # quit if End Of File was sent (via CTRL+D or end of batchfile)
            return self.do_quit()
        elif cmd is None or cmd == '':
            # do nothing if no command could be found
            pass
        else:
            # try to execute the command

            # save this command as the last one entered
            self.lastcmd = line
            try:
                # check if internal command
                func = getattr(self, 'do_' + cmd)
            except AttributeError:
                # execute as an external command
                return self.extern(line)
            else:
                # execute as an internal command
                return self.intern(cmd, arg, func)

    def intern(self, cmd, arg, func):
        """Try to execute cmd as an internal command"""
        # parse special symbols such as for IO redirection
        args, special = self.parse_special(arg.split())
        stdin, stdout = self.bind_io_redirection(special)

        # set stdin / stdout
        if stdin:
            old_stdin = self.set_stdin(stdin) # this does not work for some things (they take arguments, not read from stdin)
        if stdout:
            old_stdout = self.set_stdout(stdout)

        try:
            # parse the arguments into a suitable format
            args, kwargs = self.parse_arg(cmd, args)
        except SystemExit:
            # parsing error (see printed message)
            pass
        else:
            # execute with parsed arguments
            return func(*args, **kwargs) # use starred expressions
        finally:
            # restore stdin / stdout
            try:
                self.set_stdin(old_stdin)
            except NameError:
                pass
            try:
                self.set_stdout(old_stdout)
            except NameError:
                pass

    def parse_arg(self, cmd, arg):
        """Attempt to parse the line's arguments, returning a list of positionals and a dictionary of keyword-based arguments object."""
        cmd = self.dealias(cmd) # remove any alises from the command
        args, kwargs = self.internalparser.parse_pos_kw(cmd, arg, self.get_stderr()) # parse and pass the shell's stderr for error messages
        return args, kwargs

    def parse_special(self, arg):
        """Extract the special characters <, >, >>, &"""
        args, special = [], {}
        try:
            args, iotype, iofile = self.specialparser.parse_io(arg)
        except IndexError as e:
            self.eprint(e)
            args = tokens
        args, bg = self.specialparser.parse_bg(args)

        if iotype is not None and iofile is not None:
            special[iotype] = iofile
        special['&'] = bg
        return args, special        

    def bind_io_redirection(self, special):
        """Returns new stdin and stdout or None based on the parsed characters"""
        try:
            stdin = open(special['<'])
        except KeyError:
            stdin = None
        try:
            stdout = open(special['>'], 'w')
        except KeyError:
            try:
                stdout = open(special['>>'], 'a')
            except KeyError:
                stdout = None
        return stdin, stdout

    def extern(self, line):
        """Try to execute the line as an external command"""
        # todo: validate filename
        tokens = line.split()
        args, special = self.parse_special(tokens)
        stdin, stdout = self.bind_io_redirection(special)
        bg = special['&']
        try:
            if not bg:
                # run program in the "shell foreground"
                try:
                    # >= python3.5
                    runner = subprocess.run
                except AttributeError:
                    # older API
                    runner = subprocess.call
                runner(args, stdin=stdin, stdout=stdout)
                # blocks until the subprocess finishes
            else:
                # run program in the "shell background"

                # it is recommended to specify stdin and stdout for the background process
                if not stdin:
                    # no stdin specified, subprocess.DEVNULL is used (no input)
                    stdin = subprocess.DEVNULL
                proc = subprocess.Popen(args, stdin=stdin, stdout=stdout, stderr=stdout)
                self.subprocesses.append(proc)
        except (FileNotFoundError, BaseException) as e:
            self.eprint("Failed to execute '{}' as an external command".format(line))
            self.eprint(str(e))
            # may not want to catch BaseException in case something is wrong with this code

        # todo: make external command prompt different from actual running shell prompt
        # todo: allow for handling of internal commands on same line as external command


    # getters and setters for internal instance variables

    def get_stdin(self):
        return self.stdin

    def get_stdout(self):
        return self.stdout

    def get_stderr(self):
        return self.stderr

    def set_stdin(self, f):
        old = self.stdin
        self.stdin = f
        return old

    def set_stdout(self, f):
        old = self.stdout
        self.stdout = f
        return old

    def get_prompt(self):
        return self.prompt

    def set_prompt(self, s):
        self.prompt = s

    def get_sysargv(self):
        return self.sysargv

    @classmethod
    def set_intro(cls, intro):
        cls.intro = intro


    # hook overrides

    def preloop(self):
        __doc__ = super().preloop.__doc__

        # initialise shell prompt to current path
        self.update_prompt()


    # stdin / stdout

    def print(self, *objects, sep=' ', end='\n', flush=False):
        """Convenience function. Use self.print() instead of print() to correctly direct output to the shell's stdout stream."""
        print(*objects, sep=sep, end=end, file=self.get_stdout(), flush=flush)
    # todo: change parent processes' stdin, stdout, stderr

    def eprint(self, *objects, sep=' ', end='\n', flush=False):
        objects = [self.colourise(obj, self.SEMANTIC_COLOURS['err']) for obj in objects] 
        print(*objects, sep=sep, end=end, file=self.get_stderr(), flush=flush)

    @staticmethod
    def colourise(s, colour):
        return s # ANSI colour codes are not supported on NT (Windows) "cmd.exe" (or "PowerShell")terminal.

    # convenience / utility methods


    def format_prompt(self, s):
        """Pretty-format the prompt and make it into a suitable colour."""
        # s = Sheller.colourise(s, self.SEMANTIC_COLOURS['prompt'])
        s = '({})'.format(s)
        # weird cursor jumps even without colourise (nevermind, it actually there's no problem!)
        # with colourise + cmdloop flush=True for prompt print, not going back to *same line* (but still jagged cursor jumps)
        # pressing up arrow messes things up (only if enter commands over multiple lines)
        return s + ' '     

    def update_prompt(self):
        """Set the prompt to the current working directory, formatted."""
        if not self.batchmode:
            # in interactive mode, display the current directory in the prompt
            cwd = os.environ['PWD']
            self.set_prompt(self.format_prompt(cwd))
        else:
            # in batchmode, don't display the prompt
            self.set_prompt('')

    def get_shell_height(self):
        return shutil.get_terminal_size().lines

    def get_shell_width(self):
        return shutil.get_terminal_size().columns

    @staticmethod
    def dealias(cmd):
        """Return the true command, not an alias. Raises AttributeError if command does not actually exist."""
        return getattr(Sheller, 'do_'+cmd).__name__[3:]

    def pause_subprocesses(self):
        pass

    def unpause_subprocesses(self):
        pass

    def get_username(self, uid):
        """uid -> username"""
        # not implemented in a portable way
        # self.eprint('uid to username mapping service not available')
        return uid

    @staticmethod
    def format_datetime(d):
        return d.strftime('%c').replace(' ', '/')

    def get_entry_details(self, entry):
        """Details for an entry in a directory"""
        b = []
        inode = os.stat(entry)

        # name
        # colourise by type
        isdir = stat.S_ISDIR(inode.st_mode)
        if isdir:
            name = Sheller.colourise(entry, Sheller.SEMANTIC_COLOURS['isdir'])
        elif os.path.isfile(entry): # need this?
            name = Sheller.colourise(entry, Sheller.SEMANTIC_COLOURS['isfile'])
        else:
            name = entry
        # b.append('{:<{}}'.format(name, padding))
        b.append(name)

        # size
        size = inode.st_size
        b.append(size)
        
        # owner
        owner_uid = inode.st_uid
        owner = self.get_username(owner_uid)
        b.append(owner)

        # read-write-execute permissions
        permissions = stat.filemode(inode.st_mode)
        b.append(permissions)

        # times
        access_time = datetime.datetime.fromtimestamp(inode.st_atime)
        b.append(Sheller.format_datetime(access_time))
        modification_time = datetime.datetime.fromtimestamp(inode.st_mtime)
        b.append(Sheller.format_datetime(modification_time))
        return list(map(str, b)) # ensure that all things are string

    def pretty_dirlist(self, contents, all_details=False, hide=False, sorted_order=False):
        """Pretty formatting for directory contents"""
        b = []
        if hide:
            contents = list(filter(
                lambda c: not c.startswith('.') and not c.startswith('_'), 
                contents))
        if not all_details:
            b = contents
        else:
            details = []
            details.append(['name', 'size', 'owner', 'permissions', 'access time', 'modify time'])
            # todo: fix

            for entry in contents:
                try:
                    detailed_entry = self.get_entry_details(entry)
                except OSError:
                    # likely could not access the entry
                    pass
                else:
                    details.append(detailed_entry)                    
            # get maxwidths of columns
            widths = []
            for i in range(0, len(details[0])):
                col = [row[i] for row in details]
                maxwidth = max(map(len, col))
                widths.append(maxwidth)
            # pad with widths
            for row in details:
                for i in range(0, len(row)):
                    row[i] = '{:<{}}'.format(row[i], widths[i])

            # add entries
            b.extend([' '.join(detail) for detail in details])
        if sorted_order:
            b.sort()
        # todo: header for all_details
        return b

    @staticmethod
    def pretty_environ(env):
        """Pretty formatting for environment strings"""
        b = []
        for key, value in env.items():
            b.append('{}: {}'.format(key, value))
        return '\n'.join(b)

    def read_keypress(self):
        """Read a keypress"""
        self.eprint('Press ENTER at the end.', end=' ', flush=True)
        return self.get_stdin().readline()

    def is_space_read(self, s):
        """Return True if space was read"""
        return s == ' \n'

    def wrap_line(self, s):
        """Return a list of lines where s fits the width of the terminal screen"""
        # todo: space separated only (no cuts in middle of words!)
        w = self.get_shell_width()
        return slice_to_list(s, w)


    # help

    # def help_topic(self):
    #     """test"""
    #     return "test"


    def do_help(self, detail=''):
        """List help or specific help"""
        # todo: help for specific topics in the manual, not just the commands -> misc_header, help_notcommand
        if not detail:
            # list available help

            # extra topics
            self.print(self.colourise('(Usage: help <topic>)', self.SEMANTIC_COLOURS['manprompt']))
            self.print()

            self.section_help('Documented commands:', self.toc_commands)
            self.section_help('Various informational topics:', self.toc_infotopics)
            self.section_help('Full manual:', ['manual'])
            # todo/fix: undocumented commands at the very end, not in the middle
        else:
            self.detailed_help(detail)

    def detailed_help(self, detail):
        """Provide help to a specific detail (topic or command)"""
        man = self.get_manpage(detail)
        if not man:
            # not available
            nohelp = "No help is available. You're on your own chap."
            self.eprint(nohelp)
        else:
            # manual exists
            if self.get_stdout() is sys.stdout:
                self.interactive_manual(detail, man)
            else:
                self.print(man)

    def interactive_manual(self, detail, manual):
        """Display the manual interactively"""
        man_lines = manual.splitlines() # take each line of the manual
        man_wrapped = []
        for line in man_lines:
            wrap = self.wrap_line(line)
            man_wrapped.extend(wrap)
        lines_per_page = self.get_shell_width()//4
        man_slices = slice_to_list(man_wrapped, lines_per_page)
        man_slices = ['\n'.join(s) for s in man_slices]
        # take into account line lengths

        manpage_prompt = "'{}' manual page: (press space to continue) ".format(detail)
        manpage_prompt = self.colourise(manpage_prompt, self.SEMANTIC_COLOURS['manprompt'])
        for s in man_slices[:-1]:
            self.print(s, flush=True)
            self.print(manpage_prompt, end='', flush=True)
            k = self.read_keypress()
            if self.is_space_read(k):
                self.print()
                continue
            else:
                self.print()
                return
        self.print(man_slices[-1])
        # todo: support 'more' command
        # todo: disable for output redirection
        # todo: clear screen for help page and restore previous screen after exit help
        # todo: handle 'shift' as well

    def get_manpage(self, detail):
        """Get the manual text"""
        if detail == 'manual':
            # full manual
            return self.manualparser.get_manual()
        elif detail in self.toc_commands:
            # command
            attr = 'command-'+detail
            return self.manualparser.get_topic(attr)
        elif detail in self.toc_infotopics:
            # info topic
            return self.manualparser.get_topic(detail)
        else:
            return None

    def section_help(self, header, topics):
        """Help consistent with current format"""
        self.print(header)
        self.print('='*len(header))
        self.columnize(topics)
        self.print()


    # internal commands
    
    def do_test(self):
        """A command that does nothing!"""
        pass

    def do_cd(self, directory=''):
        """Change directory."""
        if directory is '':
            # no directory argument was specified, print the contents of the current directory
            self.do_dir()
        else:
            try:
                os.chdir(directory)
            except FileNotFoundError:
                # directory does not exist
                self.eprint("Can not find directory '{}'".format(directory))
                # todo: stderr support for errors
            except NotADirectoryError:
                # supplied path is not a directory
                self.eprint("The supplied path '{}' is not a directory".format(directory))
            else:
                os.environ['PWD'] = os.getcwd() # update working directory environment variable
                self.update_prompt() # update the prompt
                # todo: update the promp via a 'PWD' "hook" instead of doing it manually
                # todo: user-defined directory bookmarks with #
                # todo: home directory with ~

    def do_dir(self, directory='.', alldetails=False, columnize=False, notall=False, sort=False):
        """List directory contents."""
        try:
            contents = os.listdir(directory)
        except FileNotFoundError:
            self.eprint("Can not find directory '{}'".format(directory))
        except NotADirectoryError:
            self.eprint("The supplied path '{}' is not a directory".format(directory))
            # todo: take out these error messages to somewhere else
        else:
            pretty_contents = self.pretty_dirlist(contents, all_details=alldetails, hide=notall, sorted_order=sort)
            if columnize:
                self.columnize(pretty_contents)
            else:
                self.print('\n'.join(pretty_contents))
        # todo: more ls flags
        # todo: recursive dirlist

    def do_echo(self, comment=None):
        """Print a message / comment."""
        # special processing of the argument
        if comment is None:
            comment = [''] # nothing
        elif isinstance(comment, str):
            comment = [comment] # put into a list

        self.print(*comment)
        # fix: output redirection splits the thing up
        # todo: escape sequences, special symbols

    def do_clr(self, number=None, commands=False, restart=False):
        """Clear the terminal screen."""
        if commands:
            # clear the commands (don't clear the screen)
            self.do_histclear()
            return
        if number is None:
            # clear the full height of the terminal
            lines = self.get_shell_height()
        else:
            # clear a specific amount
            lines = number
        self.print('\n'*lines)
        if restart:
            # restart after clearing the screen
            self.do_restart()
        # todo: add ability to start new terminal window (complete clear)

    def do_environ(self, key=None, value=None):
        """Show a list of environment variables."""
        if key is None and value is None:
            # query all
            self.print(self.pretty_environ(os.environ))
        elif key is not None and value is None:
            # query one
            try:
                value = os.environ[key]
            except KeyError:
                self.eprint("Environment variable '{}' not found.".format(key))
            else:
                self.print('{}: {}'.format(key, value))
        elif key is not None and value is not None:
            # modify one
            os.environ[key] = value
            self.print('{}: {}'.format(key, value))

        # todo: pretty print
        # todo: make variables accessible through $ symbol and all caps (bash style)
        # todo: check sys.implementation, sys.executable, etc...

    def do_shell(self):
        """Show the path where the shell resides."""
        self.print(os.environ['SHELL'])

    def do_pause(self):
        """Pause the shell until ENTER is pressed."""
        self.pause_subprocesses() # this only works on POSIX
        self.get_stdin().readline() # this blocks the parent process / thread
        # todo: ignore other key presses
        self.unpause_subprocesses()

    def do_quit(self):
        """Exit the shell."""
        # print a last newline
        self.print()
        # indicate system exit 
        return True     

    def do_q(self):
        """Quick quit (IPython inspired)."""
        prompt = self.colourise('Do you want to quit? ([y]/n): ', self.SEMANTIC_COLOURS['quit'])
        self.print(prompt, end='', flush=True)
        answer = self.get_stdin().readline().strip()
        # todo: take 'y' or 'n' without enter (raw input)
        if answer == 'y' or answer == '':
            return self.do_quit()

    def do_restart(self):
        try:
            exec_args = [sys.executable]
            argv = self.get_sysargv()
            prog, args = argv[0], argv[1:]
            if os.environ['PWD'] != self.orig_dir:
                prog = os.path.join(self.orig_dir, prog)
                # fix: actually update the PWD in os.environ
            exec_args.append(prog)
            exec_args.extend(args)
            self.print('Restarting the shell')
            self.postloop() # execute the postloop hook just before restarting
            os.execv(sys.executable, exec_args)
        except OSError:
            self.eprint('Could not restart the shell')

    def do_alias(self, symbol, command):
        """Allow custom user-defined aliases"""
        raise NotImplementedError

    # command aliases
    do_cwd = do_cd
    do_ls = do_dir
    do_clear = do_clr
    do_cls = do_clr
    do_exit = do_quit
    do_reload = do_restart
    # do_$PATH = do_shell
    # do_extern = extern # call external program explicitly with the 'extern' command


class PosixSheller(Sheller):
    """Shell for the best OS (POSIX)"""

    # overrides

    def __init__(self, completekey='tab', stdin=None, stdout=None, stderr=None, argv=None, shell_path=None,  batchmode=False, histfile='.shell.hist'):
        super().__init__(completekey=completekey, stdin=stdin, stdout=stdout, stderr=stderr, argv=argv, shell_path=shell_path, batchmode=batchmode)
        self.histfile = os.path.abspath(histfile) # file for list of previously entered commands

        import tty
        self._tty = tty
        import termios
        self._termios = termios
        import pwd
        self._pwd = pwd
        import signal
        self._signal = signal

    def preloop(self):
        super().preloop()
        # get previous history
        import readline
        try:
            readline.read_history_file(self.get_history_file())
        except FileNotFoundError:
            # no history available
            pass

    def postloop(self):
        # update history file
        import readline
        readline.write_history_file(self.get_history_file())
        # todo: handle CTRL+C KeyboardInterrupt kills (still save history)

    @staticmethod
    def colourise(s, colour):
        """Escape sequences for coloured printing.
        'colour' is a key in the COLOURS table."""
        return '\033[' + Sheller.COLOURS[colour] + 'm' + s + '\033[0m'
        # todo: way to disable / strip colour coding for non-standard output

    def is_space_read(self, s):
        return s == ' '

    def read_keypress(self):
        # Based on 'http://code.activestate.com/recipes/134892/''
        fd = self.get_stdin().fileno() # get file descriptor (integer) for stdin
        old = self._termios.tcgetattr(fd) # tty attributes for input descriptor
        try:
            self._tty.setraw(self.get_stdin().fileno()) # change mode of file descriptor to 'raw' (character-by-character input)
            ch = self.get_stdin().read(1) # read a character
        finally:
            self._termios.tcsetattr(fd, self._termios.TCSADRAIN, old) # restore input descriptor attributes, after queued output transmission (TCSADRAIN)
        return ch

    def pause_subprocesses(self):
        for proc in self.subprocesses:
            proc.send_signal(self._signal.SIGSTOP)

    def unpause_subprocesses(self):
        for proc in self.subprocesses:
            proc.send_signal(self._signal.SIGCONT)

    # extra methods

    def get_username(self, uid):
        return self._pwd.getpwuid(uid).pw_name

    def get_history_file(self):
        return self.histfile

    def do_histclear(self):
        import readline
        readline.clear_history()
        readline.write_history_file(self.get_history_file())

    # more todos:
    # todo: bring the terminal prompt line up to the top
    # todo: readline completion for file / directory names


class NtSheller(Sheller):
    """Trash shell for trash OS (Windows)"""
    
    def __init__(self, completekey='tab', stdin=None, stdout=None, stderr=None, argv=None, shell_path=None, batchmode=False):
        super().__init__(completekey=completekey, stdin=stdin, stdout=stdout, stderr=stderr, argv=argv, shell_path=shell_path, batchmode=batchmode)
        import msvcrt
        self._msvcrt = msvcrt            

    def is_space_read(self, s):
        return s == b' '

    def read_keypress(self):
        return self._msvcrt.getch()


class JavaSheller(Sheller):
    pass


platform_shells = {
    'posix': PosixSheller,
    'nt': NtSheller,
    'java': JavaSheller,
}


portable_shell = Sheller


def get_shell():
    """Return a shell class based on the operating system."""
    operating_system = os.name
    # todo: use sys.platform, os.uname for more detailed OS information
    shell = None
    try:
        shell = platform_shells[operating_system]
        message = "On Operating System '{}', using '{}'".format(
            operating_system, shell.__name__)
        # todo: proper logs via the 'logging' module
    except KeyError:
        shell = portable_shell
        message = 'Operating System not detected. Using portable shell {}'.format(
            shell.__name__)
    return shell, message