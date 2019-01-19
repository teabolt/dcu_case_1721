#!/usr/bin/env python3

from string import ascii_letters


add = ('ch', 'sh', 'x', 's', 'z', 'o')
rem_all = ['f', 'fe']
rem_last = [c+'y' for c in ascii_letters if c not in 'aeiou']


def get_plural(s):
	for c in add:
		if s.endswith(c):
			return s+'es'
	for c in rem_all:
		if s.endswith(c):
			return s[:-len(c)]+'ves'
	for c in rem_last:
		if s.endswith(c):
			return s[:-1]+'ies'
	return s+'s'


def main():
	assert get_plural('beach') == 'beaches'
	assert get_plural('elf') == 'elves'
	assert get_plural('knife') == 'knives'
	assert get_plural('lady') == 'ladies'
	assert get_plural('boy') == 'boys'
	# assert get_plural('chloy') == 'chloyes'


if __name__ == '__main__':
	main()