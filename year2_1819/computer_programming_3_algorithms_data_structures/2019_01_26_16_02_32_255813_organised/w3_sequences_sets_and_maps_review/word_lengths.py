
def get_counts_dict(words):
	counts = {}
	for word in words:
		length = len(word)
		if length in counts:
			counts[length] += 1
		else:
			counts[length] = 1
	return counts