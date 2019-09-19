'''
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
'''

def lowest_positive(nums):
	'''
	count = 1
	new_nums = []
	for num in nums:
		if num >= 0:
			new_nums.append(num)

	return new_nums.index(min(new_nums))
	
	***
	understood the problem wrong so this does something 
	completely different. Returns the index of the lowest
	positive number
	***
	
	new_nums = []
	for num in nums:
		if num >= 0:
			new_nums.append(num)

	missing_sum = sum(new_nums)
	true_sum = (max(new_nums) * (max(new_nums) + 1)) / 2

	return(true_sum - missing_sum)
	
	***
	doesn't work for the list [1, 2, 0] since all the numbers are present.
	doesn't return 3 since it would just be 0
	***
	'''

	count = 1
	new_nums = []
	for num in nums:
		if num >= 0:
			new_nums.append(num)

	while count in new_nums:
		count = count + 1

	return count

array = [3, 4, -1, 1]
print(lowest_positive(array))

array = [1, 2, 0]
print(lowest_positive(array))

array = [3, 4]
print(lowest_positive(array))

array = [-1, -2]
print(lowest_positive(array))
