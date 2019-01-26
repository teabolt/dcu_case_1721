
def get_sliced_lists(li):
	no_last = li[:-1]
	middle = li[1:-1]
	reverse = li[::-1]
	gen_li = [no_last, middle, reverse]
	return gen_li