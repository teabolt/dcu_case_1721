
def get_evenodd_list():
	odds, evens = [], []
	num = int(input())
	while num != -1:
		if num % 2 == 0:
			evens.append(num)
		else:
			odds.append(num)
		num = int(input())
	return (odds, evens)