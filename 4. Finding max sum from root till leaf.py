#Trees
#Problem Statement:
# Given a tree with N nodes and N-1 edges,
# calculate the maximum sum of the node values 
# from root to any of the leaves without re-visiting any node.
#I/p: 3, 2, 1, 10, 1, 3, 9, 1, 5, 3, 4, 5, 9, 8
			 3
		/    |	 \
		2    1	10
	   / \  /
	   1  3 
	  / \

#o/p:22

class Node:
	def __init__(self,value):
		self.value=value
		self.children = [] #Empty list for children nodes

def solve(root,prevSum,res):
	''' Arguments:
		root: Node
		prevSum: is the current running sum 
		res: list element of size 1 that stores max value for path from root till lead node
		
		Return type:
		None
		(ans is stored in res) 
	'''
	if root.children == [] :
		res[0] = max(res[0],prevSum+root.value)

	for child in children:
		solve(child,prevSum+root.value,res)
def getRootSum(root):
	'''Arguments: 
		root:Node -Root of the tree

		Return:the max sum from the root till the leaf
	'''
	res=[0]
	solve(root,0,res)

	return res[0]


