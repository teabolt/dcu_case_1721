#!/usr/bin/env python3

import sys


def is_palindrome(s):
	if len(s) <= 1: # 1st base
		# eg: 'c', 'a', '', etc (singleton, empty)
		return True
	elif len(s) == 2: # 2nd base
		# eg: 'aa', 'ca', 'as', 'ss'
		return s[0] == s[1]

	assert len(s) > 2
	# recursive
	return is_palindrome(s[0]+s[-1]) and is_palindrome(s[1:-1])
	# eg: 'sacas' -> 'ss' and 'aca' -> True and ('aa' and 'c') -> True and True and True -> True!
	# eg: 'abbca' -> 'aa' and 'bbc' -> True and ('bc' and 'b') -> True and False and True -> Faaaaaaaaaalse!

	# return s[0] == s[-1] and is_palindrome(s[1:-1])
	# 'ab' -> 'a' == 'b' and '' -> False!
	# 'aa' -> 'a' == 'a' and '' -> FAlse?@#


def main():
	s = sys.argv[1]
	print(is_palindrome(s))


if __name__ == '__main__':
	main()