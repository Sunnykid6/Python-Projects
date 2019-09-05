'''
Problem
This problem was asked by Uber
.
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6]
'''
import  numpy

def find_products(list_int):	
	if len(list_int) == 0:
		return "Empty array was given"

	answer = 1
	product_list = []

	for num in list_int:
		answer = answer * num

	for num in list_int:
		answer = answer / num
		product_list.append(answer)
		answer = answer * num

	return product_list

def find_products2(list_int):
	product_list = []

	for num in list_int:
		copy_list = list_int.copy()
		copy_list.remove(num)
		product_list.append(numpy.prod(copy_list))

	return product_list


array = [1, 2, 3, 4, 5]
print(find_products2(array))
array = [3, 2, 1]
print(find_products(array))
# Solution 1 doesn't work for 0... array = [1, 2, 3, 4, 0]
array = [-3, 2, -1]
print(find_products(array))
array = [1, 2, 3, 4, 0]
print(find_products2(array))



