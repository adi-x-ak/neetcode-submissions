# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        q=[(root,1)]
        maxdepth=1

        while q:
            ele , level = q.pop(0)
            maxdepth = max(maxdepth,level)
            if ele.left:
                q.append((ele.left,level+1))
            if ele.right:
                q.append((ele.right , level+1))
            
            

        return maxdepth
            



       
        