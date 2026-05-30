from collections import deque
graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6],
    4: [7],
    5: [7, 8],
    6: [8],
    7: [],
    8: []
}


def bfs(start,graph):

    visited=set([start])
    queue=deque([start])

    while queue:
        node=queue.popleft()
        print(node)

        for i in graph[node]:
            if i not in visited:
                visited.add(i)
                queue.append(i)


# bfs(start=1,graph=graph)

def dfs(start,graph):

    visited=set()
    stack=[start]

    while stack:
        node=stack.pop()
        if node in visited:
            continue
        visited.add(node)

        print(node)

        for i in graph[node]:
            if i not in visited:
                stack.append(i)

# dfs(start=1,graph=graph)

graph1 = {
    1: [2, 3],  # 5 -> [4, 8]
    2: [4],     # 4 -> [11]       (Right child was null)
    3: [5, 6],  # 8 -> [13, 4]
    4: [7, 8],  # 11 -> [7, 2]
    5: [],      # 13 has no children
    6: [9],     # 4 -> [1]        (Left child was null)
    7: [],      # Leaf node
    8: [],      # Leaf node
    9: []       # Leaf node
}

def dfs_recursive(graph,node,visited=None):

    if visited is None:
        visited=set()
    visited.add(node)

    print(node)

    for i in graph[node]:
        if i not in visited:
            dfs_recursive(graph,i,visited)


# dfs_recursive(graph=graph,node=1,visited=None)

# import sys
# print(sys.getrecursionlimit())

'''
112 . path sum 
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(5)

root.left = TreeNode(4)
root.right = TreeNode(8)

root.left.left = TreeNode(11)

root.right.left = TreeNode(13)
root.right.right = TreeNode(4)

root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)

root.right.right.left=TreeNode(5)
root.right.right.right = TreeNode(1)

def hasPathSum(root, targetSum):
        result=[]
        def dfs(node,sum_path,current):
      
            if not node:
                return False
            
            sum_path+=node.val
            current.append(node.val) #choose

            if not node.left and not node.right:
            
                if sum_path == targetSum:
                       result.append(current.copy())
                current.pop()
                
                return 

            dfs(node.left,sum_path,current) #explore
            dfs(node.right,sum_path,current)

            current.pop()   #unchoose

        return result


# print(hasPathSum(root,targetSum=22))

'''
this one of the solution without recursion
'''
# without recursion

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# # class Solution:

def hasPathSum_2(root,targetSum) -> bool:
        
        if not root:
            return False
        stack = [(root, root.val)]

        while stack:
            node, target = stack.pop()

            if not node.left and not node.right and target == targetSum:
                return True

            if node.left:
                stack.append((node.left, target + node.left.val))

            if node.right:
                stack.append((node.right, target + node.right.val))
    
        return False

# print(hasPathSum_2(root,targetSum=23))

'''
113. Path Sum II

'''

def pathSum(root,targetSum)->list[list[int]]:

    result=[]

    if not root:
        return []
    
    stack=[(root,root.val,[root.val])]

    while stack:
        node,target,path=stack.pop()

        if not node.left and not node.right :
            if  target==targetSum:
             result.append(path)
        
        if node.left:
            stack.append((node.left,target+node.left.val,path+[node.left.val]))

        if node.right:
            stack.append((node.right,target+node.right.val,path+[node.right.val]))
    
    return result

print(pathSum(root,targetSum=22))