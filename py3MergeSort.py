def mergeSort(array):
   if len(array) > 1:
       mid = len(array) // 2
       left = array[:mid]
       right = array[mid:]

       mergeSort(left)
       mergeSort(right)

       i = 0
       j = 0
       k = 0

       while i < len(left) and j < len(right):
           if left[i] < right[j]:
               array[k] = left[i]
               i = i + 1
           else:
               array[k] = right[j]
               j = j + 1
           k = k + 1

       while i < len(left):
           array[k] = left[i]
           i = i + 1
           k = k + 1

       while j < len(right):
           array[k] = right[j]
           j = j + 1
           k = k + 1

array = [54, 26, 93, 17, 77, 31, 44, 55, 20]
mergeSort(array)
print(array)

array = [1, 26, 40, 25, 26, 58, 32, 55, 80]
mergeSort(array)
print(array)