#		   S			  E
# array = [8, 5, 2, 8, 5, 6, 3]
#		   P  L			  R

# if  s >= e : r
# 	assigning p, l, r -variables
# while r >= e
# if l >= p & r <= p
# 	swap
# l <= p -  l+
# r >= p -  r-
# leftsubarrayissmaller = r - 1 - s < e - (r + 1)
# (p , s, r - 1)
# (p, r + 1, e)

# Worst : time - O(n^2),Space- O(log(n)) # in input - swap all positions
# Best: time - O(nlog(n)),Space- O(log(n)) # in input - swap postions for left and right subarray
# Avg: time - O(nlog(n)),Space- O(log(n))

def quickSort(array):
	quickSortHelper(array, 0, len(array) - 1)
	return array
	
def quickSortHelper(array, startIdx, endIdx):
	if startIdx >= endIdx:
		return
	pivotIdx = startIdx # assuming far left of the array
	leftIdx = startIdx + 1
	rightIdx = endIdx
	while rightIdx >= leftIdx:
		if array[leftIdx] > array[pivotIdx] and array[rightIdx] < array[pivotIdx]:
			swap(leftIdx, rightIdx, array)
		if array[leftIdx] <= array[pivotIdx]:
			leftIdx += 1
		if array[rightIdx] >= array[pivotIdx]:
			rightIdx -= 1
	swap(pivotIdx, rightIdx, array) # R < L
	# leftSubarray = (rightIdx - 1) -> pivot is located here
	# rightSubarray = endIdx - (rightIdx + 1)
	leftSubarrayIsSmaller = rightIdx - 1 - startIdx < endIdx - (rightIdx + 1)
	if leftSubarrayIsSmaller:
		quickSortHelper(array, startIdx, rightIdx - 1) # leftSubarray
		quickSortHelper(array, rightIdx + 1, endIdx) # rightSubarray
	else:
		quickSortHelper(array, rightIdx + 1, endIdx) # rightSubarray
		quickSortHelper(array, startIdx, rightIdx - 1) # leftSubarray
	
def swap(i, j, array):
	array[i], array[j] = array[j], array[i]
