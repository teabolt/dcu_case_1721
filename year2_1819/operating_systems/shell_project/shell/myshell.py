#!/usr/bin/env python3
# Done by Tomas Baltrunas, student number 17350793, Computer Applications Year 2. For CA216 2019 shell assignment.

# This project users PYTHON VERSION 3. It has been tested using python 3.7.

"""Interface to the shell"""


import sys
import os
import os.path
from datetime import datetime

from shell import get_shell # function to get a shell suitable for this platform


SHELL_EXECUTABLE_PATH = os.path.realpath(__file__) # used for identifying the location for the shell executable


def main():
    # get an appropriate shell class
    shell_cls, shell_message = get_shell() 
    
    # choose an execution mode based on the arguments supplied to the python script
    if len(sys.argv) == 2: 
        # batch file mode
        
        filename = sys.argv[1]
        try:
            batchfile = open(filename)
        except (FileNotFoundError, IsADirectoryError):
            print("Can not find batch file '{}'".format(batchfile))
        # todo: refactor by making a function that checks the validity of a file/directory path

        # instantiate the shell
        # set the stdin argument to the batchfile and turn on the batchmode flag
        myshell = shell_cls(stdin=batchfile, argv=sys.argv, shell_path=SHELL_EXECUTABLE_PATH, batchmode=True)

        try:
            # begin REPL execution
            myshell.cmdloop()
        finally:
            batchfile.close()

        # todo: support stdin from a batchfile and another file (internal stdin redirection)
        # todo: multiple batch files
    else: 
        # interactive mode

        # instantiate an interactive shell
        myshell = shell_cls(argv=sys.argv, shell_path=SHELL_EXECUTABLE_PATH)

        # set the intro for interactive mode
        b = [] # string builder pattern
        try:
            # POSIX
            username = os.environ['USER']
        except KeyError:
            try:
                # NT / Windows
                username = os.environ['USERNAME']
            except KeyError:
                username = 'spy in an underground bunker with an esoteric os'
        b.append("Welcome ~'{}'".format(username))
        b.append(shell_message)
        b.append("Current datetime: '{}'".format(datetime.now()))
        b.append("I'm sorry that you have been forced to use me")
        intro = '\n'.join(b)
        myshell.set_intro(myshell.colourise(intro, myshell.SEMANTIC_COLOURS['intro']))
        # todo: to refactor, may want to move this into the shell.py module

        # begin interactive prompt-command execution
        myshell.cmdloop()


if __name__ == '__main__':
    main()