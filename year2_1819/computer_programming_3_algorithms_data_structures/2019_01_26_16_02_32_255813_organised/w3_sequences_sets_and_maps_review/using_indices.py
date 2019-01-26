
def get_counts(words):
	counts = [0]*10
	for word in words:
		length = len(word)
		counts[length] += 1
	return counts