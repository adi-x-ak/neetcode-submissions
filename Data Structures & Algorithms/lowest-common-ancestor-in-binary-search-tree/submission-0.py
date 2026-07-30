# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root is None:
            return None  #empty tree
        #we found either p or q
        if root==p or root==q:
            return root

        #recursively call left subtree and right subtree
        leftresult=self.lowestCommonAncestor(root.left,p,q)
        rightresult=self.lowestCommonAncestor(root.right,p,q)

        #if both leftresult and rightresult found return root that particular one is te
        if leftresult is not None and rightresult is not None:
            return root


        #only if left reuslt found return 
        if leftresult is not None:
            return leftresult
        return rightresult
        