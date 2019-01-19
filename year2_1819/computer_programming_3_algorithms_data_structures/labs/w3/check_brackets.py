#!/usr/bin/env python3


class Stack:
#  Stack ADT has three methods: is_empty, push and pop.
#
   def __init__(self):
      self.stack = []
      self.top = 0

   def is_empty(self):
      return self.top == 0

   def push(self, item):
      if self.top < len(self.stack):
         self.stack[self.top] = item
      else:
         self.stack.append(item)

      self.top += 1

   def pop(self):
      if self.is_empty():
         return None
      else:
         self.top -= 1
         return self.stack[self.top]


def check_brackets(line):
	brackets = {
		'(': ')',
		'{': '}',
		'[': ']',
	}
	stack = Stack()
	for c in line:
		if c in brackets.keys():
			stack.push(c)
		elif c in brackets.values():
			if not stack.is_empty():
				opening = stack.pop()
			else:
				return False
			if brackets[opening] != c:
				return False
	if stack.is_empty():
		return True
	else:
		return False


def main():
	print(check_brackets('raabasfda2132(aba[gada]aga)ab{}'))
	assert check_brackets("()")
	assert not check_brackets(")(")
	assert check_brackets("hello(goo(d)bye)")
	assert not check_brackets("hello(goo(d)bye))")
	assert not check_brackets("d(h((e(l))))o)d")
	assert not check_brackets("(d(h((e(l)l))o)d")
	assert not check_brackets('{)')
	assert not check_brackets('(()')
	assert not check_brackets('(((((((([[[{')


if __name__ == '__main__':
	main()