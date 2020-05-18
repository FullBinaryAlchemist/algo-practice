#Problem statement : Sum up all elements of a branch upto the leaf of that branch and display it in a list in order
#						of leftmost leaf being the first element and rightmost leaf being the last
#		   1
	# 	  / \
	#    2   3
	#   / \  / \
	#  4  5 6  7
	# / \ / 
	# 8 9 10
	# Answer= [15,16,18,10,11]

#Solution Pardigm: Recursive
#Time Complexity: O(n) - where n is the number of nodes in the tree
#		Explaination: Since we'll have to traverse over n nodes to get all the nodes in the branches
#Space Complexity: O(n) 
# 		Explaination: #1 There are going to be atmost n elements in the leaf so the list will be of O(N)
#					  #2 At any point of time in the recursive call stack there are going to be log N call stack since
#							half tree of that node will be in the call stack so O(log N) for non skewed binary tree and
#							at each leaf level the binary tree will have approx half of the all nodes in tree. So O(N/2)=>O(N)

def calculatebranchsum(curNode,curSum,sums):
	#check if curNode is not None
	if curNode is None:
		return
	curSum += cur.value

	#check if  leaf node
	if curNode.left==None and curNode.right==None:
		sums.append(curSum)
		return
	calculatebranchsum(curNode.left,curSum,sums)
	calculatebranchsum(curNode.right,curSum,sums)

def main():
	sums=[]
	curSum=0
	calculatebranchsum(root,curSum,curNode)

	return sums
