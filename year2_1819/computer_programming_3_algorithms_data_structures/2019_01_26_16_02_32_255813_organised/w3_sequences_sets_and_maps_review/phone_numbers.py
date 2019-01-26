
print('Enter a name and number, or a name and ? to query (!! to exit)')
phone_book = {}
command = input()
while command != '!!':
	name, arg = command.split()
	if arg == '?':
		if name in phone_book.keys():
			print('{} has number {}'.format(name,phone_book[name]))
		else:
			print('Sorry, there is no {}'.format(name))
	else:
		phone_book[name] = arg

	command = input()
print('Bye')