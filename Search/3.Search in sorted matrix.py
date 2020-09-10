###Problem Statement:
# We're given a 2D array that consists of elements sorted row wise as well the elements of the sorted column wise
#Given an element , we need to find whether it exists in the matrix and return the index if it does exist
#I/p:
# [1,2,3,4,10]
# [4,5,6,7,11]
# [8,9,11,12,13]
# Target: 12
#O/p : [2,3]

###Naive approach:
# Iterate all the row and for each row iterate all the elements
# Time:O(N*M)

# ###Better approach:
# For each row, apply binary search 
# Time: O(n*log(m)) as we are travesing through all n rows and performing binary search with time Complexity of O(log a)
# 				Therefore O(n*logm)

####Solution:
1. Compare with the last element of the first row
2. If greater then eliminate the elements preceding it and increment the row to as it is in sorted order
	Else decrement the column index and compare with it
3. Repeat 2 till column<0 or row>n 
#Complexity Analysis:
# 
# Space Complexity: O(1) as no inplace searching with no variable space that depends on the size of the input
# 
# Time Complexity: O(N+M) where N is the no of rows and M is the no of column
#  	  Explanation: We re moving either downwards or leftwards . Therefore in worst case scenario we'll move down 
# 					the entire column and leftwards movements would at most sum to the number of elements in a row
def searchSortedMatrix(matrix,target):
	'''Arguments:
		matrix: 2-D array(list) of sorted integers
		target: int to be searched

		Return:
		Either list of length=2 or None in case the element is not found
	'''
	row=0
	col=len(row[0])-1

	while(row<n and col>=0):
		if matrix[row][col]<target:
			row+=1
		elif matrix[row][col]>target:
			col-=1
		else:
			return [row,col]

	return None