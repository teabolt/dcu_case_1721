
print("Enter numbers (-1 to end): ", end="")

occured = set()
previous = []
num = int(input())
while num != -1:
	if num in occured:
		previous.append(num)
	else:
		occured.add(num)
	num = int(input())

for num in previous:
	print(str(num) + " ", end="")
print()