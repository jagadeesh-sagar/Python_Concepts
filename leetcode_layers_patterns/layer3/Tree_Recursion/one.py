
'''
104. Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node. 

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

'''

def maxDepth(root):

    if not root:
        return 0

    return 1+max(maxDepth(root.left),maxDepth(root.right))

'''
112. Path Sum

Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.
'''

def hasPathSum(root,targetSum)->bool:

    if not root :
        return False
        
    if root.left is None and root.right is None:
        return targetSum-root.val==0
    
    return hasPathSum(root.left,targetSum-root.val) or hasPathSum(root.right,targetSum-root.val)


def hasPathSum(self, root, targetSum) -> bool:

    def dfs(node,sum_path):

        if not node:
            return False
        sum_path+=node.val

        if not node.left and not node.right:
            return targetSum==sum_path

        return (
            dfs(node.left,sum_path)
            or
            dfs(node.right,sum_path)
        )
    
    return dfs(root,0)



'''
226. Invert Binary Tree

Given the root of a binary tree, invert the tree, and return its root.

Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:
Input: root = [2,1,3]
Output: [2,3,1]
'''

def invertTree(root):


    if not root :
        return None

    root.left,root.right=root.right,root.left
    invertTree(root.left) 
    invertTree(root.right)
    
    return root

'''
543. Diameter of Binary Tree

Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.

Example 1:
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:
Input: root = [1,2]
Output: 1
'''
'''

here the diameter is the longest path in tree (in all circles world)
where the path nodes cant be repeated
1.we calculated the height of the each subtree and that becomes the diameter for that node
2.height of the tree is max height of the each subtree(we done a pblm on it)
3.we maintain the max diameter and return that(most of the times diameter goes through the root node but not always)

'''
def diameterOfBinaryTree(root) -> int:
    self.diameter=0

    def dfs(root):
        if not root:
            return 0

        left_height=dfs(root.left)
        right_height=dfs(root.right)
        
        self.diameter=max(self.diameter,left_height+right_height)

        return 1+max(left_height,right_height)

    dfs(root)

    return self.diameter
