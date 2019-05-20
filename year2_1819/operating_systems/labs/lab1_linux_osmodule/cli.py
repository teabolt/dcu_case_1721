"""Type commands to do something (command line interface)"""

import cmd
import os


class CLI(cmd.Cmd):
	intro = """ >>> Hello There <<< """
	prompt = "(cli): "

	def do_hello(self, args):
		"""Greets the caller"""
		print('Hi {}'.format(args))

	def do_quit(self, args):
		"""Quits the program"""
		print('You done now?')
		raise SystemExit

	do_exit = do_quit

	def do_dir(self, args):
		print(os.listdir(args))

	def default(self, line):
		self.stdout.write('No\n')
		

def main():
	CLI().cmdloop()


if __name__ == '__main__':
	main()
