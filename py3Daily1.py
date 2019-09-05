'''
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
'''

def has_sum(check_array, the_sum):
	seen = []
	count = 0
	for value in check_array:
		if value in seen:
			print("The indexes %d and %d of the array add up to %d" % (seen.index(value), count, the_sum))
			print("The two numbers are %d and %d" % (check_array[seen.index(value)], check_array[count]))
			return True
		seen.append(the_sum - value)
		count = count + 1
	print("No numbers in the array add up to %d" % (the_sum))
	return False

array = [1, 2, 3, 4, 0]
has_sum(array, 8)