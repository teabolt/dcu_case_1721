#!/usr/bin/env python3
# Done by Tomas Baltrunas, student number 17350793, Computer Applications Year 2. For CA216 2019 shell assignment.

"""Argument parsing engine"""

import argparse
from collections import namedtuple
import xml.etree.ElementTree as ET

from utils import index_any, delist_singleton, strip_around, strip_around_lines


class InternalCommandParser(object):
    """Parser for internal commands"""

    def __init__(self):
         # initialise parser objects: optimisation - don't load all parsers
        self.parsercache = {} # mapping from method names (str) to parser objects (argparse instances)

        # attach docstrings the parser initialisers
        parsers = filter(lambda t: t[0].startswith('init_'), vars(InternalCommandParser).items())
        for name, parser in parsers:
            parser.__doc__ = """Return an instance of the argument parser for the command"""

    def get_parser(self, cmd):
        """Return a parser tuple, initialising a fresh parser if needed."""
        try:
            # parser has already been initialised
            parser, positional, keyword = self.parsercache[cmd]
        except KeyError:
            # parser needs to be initialised
            parser, positional, keyword = getattr(self.InternalParserInitializer, cmd)()
            self.parsercache[cmd] = parser, positional, keyword
        return parser, positional, keyword

    def parse_pos_kw(self, cmd, arg, stdout=None):
        """Return an (args, kwargs) tuple
        'stdout' indicates where error messages go to."""
        args, kwargs = [], {}
        if hasattr(self.InternalParserInitializer, cmd):
            parser, positional, keyword = self.get_parser(cmd)
            try:
                if stdout:
                    old_stderr = argparse._sys.stderr
                    argparse._sys.stderr = stdout
                namespace = parser.parse_args(arg)
            except SystemExit:
                # argparse showed errors
                raise SystemExit("See ArgumentParser help")
            else:
                # successfully parsed
                for pos in positional:
                    positional_val = getattr(namespace, pos)
                    args.append(delist_singleton(positional_val))
                for kw in keyword:
                    keyword_val = getattr(namespace, kw)
                    kwargs[kw] = delist_singleton(keyword_val)
            finally:
                if stdout:
                    argparse._sys.stderr = old_stderr

        # if there is no parser, return empty results
        return args, kwargs

    class InternalParserInitializer(object):
        """Return a tuple of `parser object, positional required arguments (in order), keyword optional arguments`"""

        @staticmethod
        def help():
            parse_help = argparse.ArgumentParser(prog='help')
            parse_help.add_argument('detail', nargs='?', default='')
            return parse_help, [], ['detail'] # not an ideal solution (easy to miss this part)

        @staticmethod
        def cd():
            parse_dir = argparse.ArgumentParser(prog='cd')
            # todo: add description='something'
            parse_dir.add_argument('directory', nargs='?', default='')
            return parse_dir, [], ['directory']

        @staticmethod
        def dir():
            parser_dir = argparse.ArgumentParser(prog='dir')
            parser_dir.add_argument('directory', nargs='?', default='.')
            parser_dir.add_argument('-a', '-d', '-l', '--alldetails', action='store_true', help="Display detailed entry information.")
            parser_dir.add_argument('-c', '--columnize', action='store_true', help="Display the entries in columns")
            parser_dir.add_argument('-n', '--notall', action='store_true', help="Do NOT list entries that start with a '.' or '_'.")
            parser_dir.add_argument('-s', '--sort', action='store_true', help="Sort the directory entries.")
            return parser_dir, [], ['directory', 'alldetails', 'columnize', 'notall', 'sort']

        @staticmethod
        def echo():
            parser_echo = argparse.ArgumentParser(prog='echo')
            parser_echo.add_argument('comment', nargs='*', default=None)
            # todo: add support for escaping input
            return parser_echo, [], ['comment']

        @staticmethod
        def clr():
            parser_clr = argparse.ArgumentParser(prog='clr')
            parser_clr.add_argument('-n', '--number', nargs=1, type=int, help="Specify the amount of lines to clear.")
            parser_clr.add_argument('-c', '--commands', action='store_true', help="Clear the commands history.")
            parser_clr.add_argument('-r', '--restart', action='store_true', help="Clear the screen and restart the shell.")
            return parser_clr, [], ['number', 'commands', 'restart']

        @staticmethod
        def environ():
            parser_environ = argparse.ArgumentParser(prog='environ')
            parser_environ.add_argument('key', nargs='?', default=None)
            parser_environ.add_argument('value', nargs='?', default=None)
            return parser_environ, [], ['key', 'value']

        @staticmethod
        def alias():
            parser_alias = argparse.ArgumentParser(prog='alias')
            parser_alias.add_argument('symbol', nargs='?')
            parser_alias.add_argument('command', nargs='?')
            return parser_alias, ['symbol', 'command'], []


class SpecialCharacterParser(object):
    """Parser for special commands of the form
    arg1 arg2 ... argn [<|>|>> (filename)] [&]
    """
    # todo: more advanced pattern parsing

    def parse_io(self, tokens):
        try:
            i = index_any(tokens, ['<', '>', '>>'])
        except ValueError:
            # no special redirection symbols were entered
            return tokens, None, None
        else:
            # get the arguments for the redirection symbol
            try:
                return tokens[:i]+tokens[i+2:], tokens[i], tokens[i+1]
            except IndexError:
                # a file argument for the redirection was not found
                # todo: check if the filename is not another symbol
                raise IndexError('Redirection argument not found')

    def parse_bg(self, tokens):
        return (tokens[:-1], True) if tokens and tokens[-1] == '&' else (tokens, False)


class ManualParser(object):
    """Parser for an XML manual"""

    def __init__(self, manual):
        try:
            self.manxml = ET.parse(manual)
        except ET.ParseError:
            self.manxml = None
            with open(manual) as f:
                self.mans = f.read()
        else:
            self.manroot = self.manxml.getroot()

    def get_table_of_contents(self):
        if self.manxml:
            toc = [] 
            # may want to use a set if there are many topics
            for e in self.manroot.findall(".//topic"):
                titles = list(e.attrib.values())
                toc.extend(titles)
            return toc
            # todo: structured and nested, not just flat, table of contents
        else:
            return None

    def get_manual(self):
        if self.manxml:
            man = []
            for text in self.manroot.itertext():
                text = [strip_around(line) for line in text.splitlines()]
                man.append('\n'.join(text))
            return '\n'.join(man)
        else:
            return self.mans

    def get_topic(self, topic_name):
        if self.manxml:
            try:
                e = self.manroot.find(".//topic[@name='{}']".format(topic_name))
                texts = []
                for text in e.itertext():
                    if len(text) == 1:
                        text = strip_around_lines(text[0])
                    else:
                        text = [strip_around(line) for line in text.splitlines()]
                    texts.append('\n'.join(text))
                return '\n'.join(texts)
            except AttributeError:
                return None
        else:
            return self.mans

    def get_by_text(self, text):
        raise NotImplementedError