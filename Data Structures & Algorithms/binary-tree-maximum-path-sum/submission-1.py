# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ''' the idea to for each node include node left , right update the result 
        return the node + max of leftmax , right max 
        if any negative value found just amke it zero
        dfs
        o(n)
        start at root find the max u can get from left 
        now go to right do the same 
    
        '''
        res=[root.val]

        def dfs(root):
            if not root:
                return 0
            leftmax=dfs(root.left)
            rightmax=dfs(root.right)

            leftmax=max(leftmax,0)
            rightmax=max(rightmax,0)

            #compute max path sum with split 
            res[0]=max(root.val+leftmax+rightmax,res[0])

            return root.val+max(leftmax,rightmax)
        dfs(root)
        return res[0]


        