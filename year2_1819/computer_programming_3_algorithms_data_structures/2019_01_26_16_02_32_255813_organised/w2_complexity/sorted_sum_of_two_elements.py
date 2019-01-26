
#!/usr/bin/env python3

#A sorted list "lst" is provided
#A sum "k" to locate using two elements from "lst"

def sum_to_k(lst, k):				#we create a new function
	i = 0							#create a counter
	j = len(lst)-i-1				#counter from the end of the list
	while i < len(lst):				#loop to go through the list
		if i == j:
			return False
		v = lst[i] + lst[j]			#variable to be reused
		if v == k:					#check if the sum of the two elements equals "k" 
			return True				
		elif v < k:
			i += 1 					#increment counter i to get a bigger sum
		elif k < v:
			j -= 1 					#move counter j down to get a smaller sum
	return False

# sample scenario
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# k = 0
# print(sum_to_k(lst, k))