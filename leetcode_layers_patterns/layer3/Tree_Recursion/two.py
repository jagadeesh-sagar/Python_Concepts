
'''
124. Binary Tree Maximum Path Sum

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
The path sum of a path is the sum of the node's values in the path.
Given the root of a binary tree, return the maximum path sum of any non-empty path.

'''

'''
same logic as above one 

'''
def maxPathSum(self, root) -> int:
    self.value=float('-inf')

    def dfs(root):

        if not root :
            return 0

        left_subtree=max(dfs(root.left),0)
        right_subtree=max(dfs(root.right),0)

        # i used this maximum to avoid negative values but using "0" in max helps that
        # maximum1=max(root.val,root.val+left_subtree+right_subtree)  
        # maximum2=max(maximum1,root.val+right_subtree)
        # maximum3=max(maximum2,root.val+left_subtree)

        self.value=max(self.value,left_subtree+right_subtree+root.val)

        return root.val+max(left_subtree,right_subtree)

    dfs(root)

    return self.value

'''
Same Tree (LC 100) code
'''

def isSameTree(self, p, q) -> bool:

        if  not p and not q:
            return True
        if not p or not q:
            return False
     

        left=self.isSameTree(p.left,q.left)
        right=self.isSameTree(p.right,q.right)

        if p.val!=q.val :
            return False
        
        return left and right

'''

| Order | Problem | Pattern to practise |
|---:|---|---|
| 1 | LC 100 — Same Tree | Boolean return |
| 2 | LC 101 — Symmetric Tree | Compare recursive results |
| 3 | LC 111 — Minimum Depth | Combine subtree values |
| 4 | LC 110 — Balanced Binary Tree | Return multiple pieces of information |
| 5 | LC 563 — Binary Tree Tilt | Return subtree sum |
| 6 | LC 687 — Longest Univalue Path | Downward path versus global answer |
| 7 | LC 113 — Path Sum II | Carry state down the tree |
| 8 | LC 236 — Lowest Common Ancestor | Return a node |
| 9 | LC 700 — Search in a BST | Return a matching subtree |
| 10 | LC 701 — Insert into a BST | Reconnect returned subtrees |
| 11 | LC 450 — Delete Node in a BST | Handle changed subtree roots |
| 12 | LC 105 — Construct Binary Tree | Construct and return a structure |
'''