# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root == None:
            return 0
        q = [(root,1)]
        maxx = 0

        while q:
            node,lvl = q.pop(0)
            maxx = max(maxx,lvl)

            if node.left:
                q.append((node.left,lvl+1))

            if node.right:
                q.append((node.right, lvl+1))

        return maxx
        