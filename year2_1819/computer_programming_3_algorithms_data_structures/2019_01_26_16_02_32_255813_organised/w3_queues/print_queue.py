
#!/usr/bin/env python3

def print_queue(data, front, back):
	contents = []
	while front != back:
		contents.append(data[front])
		front = (front + 1) % len(data)
	return contents


def main():
	a = [1, 2, 3, 4, 5]
	assert print_queue(a, 0, 4) == [1, 2, 3, 4]
	assert print_queue(a, 1, 1) == []
	assert print_queue(a, 1, 2) == [2]
	assert print_queue(a, 1, 0) == [2, 3, 4, 5]


if __name__ == '__main__':
	main()