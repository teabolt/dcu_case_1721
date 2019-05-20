#!/usr/bin/env python3

from __future__ import print_function
import os
import os.path
import sys


def item_info(path):
	b = []	# string builder
	inode = os.stat(path)
	b.append(path)	# name
	if os.path.isfile(path):
		b.append('file') 
	elif os.path.isdir(path):
		b.append('dir')
	b.append('f' if inode.st_mode & 0b0100_0000 else '-')
	b.append('d' if inode.st_mode & 40_0000 else '-')
	b.append(inode.st_size)
	b.append(os.path.getsize(path))
	b.append(inode.st_atime)
	b.append(inode.st_mtime)
	b.append(inode.st_ctime)
	return ' '.join(map(lambda s: '{:<15}'.format(str(s)), b))


def print_dir_items(names, path):
	for name in names:
		full_path = os.path.join(path, name)
		print(item_info(full_path))	


def main():
	if len(sys.argv) == 2:
		path = sys.argv[1]
	else:
		path = '.'
	header = 'Name, ...'
	files = os.listdir(path)
	print(header)
	for i in range(0, len(files)-1, 20):
		print_dir_items(files[i:i+20], path)
		line = input('Press spacebar to continue ')
		key = line.replace(' ', '*').strip()
		if key != '*':
			break


if __name__ == '__main__':
	main()