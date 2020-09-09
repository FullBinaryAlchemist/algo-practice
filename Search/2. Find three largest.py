###Problem statement
#Given an array containing int value. Find the 3 largest values and return then 
#Test case #1
# I/p: [-1,-8,32,2,2,2,-3,-3,145,154,12]
# O/p: [32,145,154]
#Test cae #2
# I/p: [2,2]
# O/p: [None,2,2]
###

###Approach #1 
#using Inbuilt methods
#1. First convert the array to dictionary to remove the duplicate elements
#2. Convert the keys to array and then perform sorting on this array
#3. Slice the last three elements if 3 elements are there otherwise check there 

def largest_three_num1(arr):
	'''Arguments:
		arr: i/p array

		Return:
		Return the list of three largest elements
	'''
	num_dict={}
	
	for num in arr:
		if num in num_dict:
			num_dict[num]+=1
		else:
			num_dict[num]=1

	nums= list(num_dict.keys())
	
	nums.sort()
	counts=[0,0,0]
	#check if num length is greater than 3
	if len(nums)>=3:
		return nums[-3:]
	else:
		ans=[None,None,None]

		#replicating the largest number
		counts[-1] = 3 if num_dict[nums[-1]] >3 else num_dict[nums[-1]]  
		ans[-counts[-1]:] = [nums[-1]]*counts[-1]

		if 3-counts[-1] == 0:
			return ans

	if len(nums)>1:
		counts[-2]= 3-counts[-1] if num_dict[nums[-2]]> 3-counts[-1] else num_dict[nums[-2]]
		ans[-counts[-2]-counts[-1]:-counts[-1]] = [nums[-2]]*counts[-2]

	return ans

#Space Complexity: o(n) 
#Explanation: We're building a dictionary which may end up containing n elements in worst case
#Time Complexity: O(nlogn)
#Explanation: 1.Building the Dicitionary and Getting the keys array will be O(n)
#			  2. Inbuilt sorting will take O(nlogn) so overall O(nlogn)

#Better Solution
#Using IN PLACE TRAVESAL
#Space:O(1) as no extra space that is dependent on the input is required
#Time:O(n) as we have to travese the array at least once and the other operations are constant(for the given problem)

def shift_and_set(arr,num,idx):
	''' Shifts the elements to left and place the element at index	
	'''
	for i in range(idx+1):
		if i==idx:
			arr[idx]=num
		else:
			arr[i]=arr[i+1]


def compare_and_set(res,num):
	'''Compares the num with elements in res for condition and updates res accordingly
		Arguments: 
		num: int to be compared against
		res: result array in which the num is to be updated

		Returns:
		None
	'''
	for idx in range(len(res)-1,-1,-1):
		#print(idx)
		if res[idx]==None:
			res[idx]=num
			return
		if res[idx]<num:
			shift_and_set(res,num,idx) #shift the elements to left and places the current element
			return

def largest_three_num2(arr):
	
	ans=[None,None,None]

	for num in arr:
		#print(num)
		compare_and_set(ans,num)
		#print("\n")
	return ans


print( largest_three_num2([-1,-8,32,2,2,2,-3,-3,145,154,12]) )
print(largest_three_num2([2,3]))
print(largest_three_num2([2,3,4,4]))
print(largest_three_num2([2,2]))

print( largest_three_num1([-1,-8,32,2,2,2,-3,-3,145,154,12]) )
print(largest_three_num1([2,3]))
print(largest_three_num1([2,3,4,4]))
print(largest_three_num1([2,2]))
