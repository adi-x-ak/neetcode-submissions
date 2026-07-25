# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''algorithm 
        i am planning to a bfs traversal where i travserese each level and 
        note the level of the tree until the queue becomes empty and process the nodes 
        '''
        #first check base case 
        if not root:
            return 0
        queue=[] #intializing queue 
        #push the root and level as one 
        queue.append((root ,1))
        maxlevel=1
        while queue:
            #pop the current element and level
            ele,level=queue.pop(0)
            maxlevel=max(maxlevel,level)
            if ele.left:
                queue.append((ele.left,level+1))
            if ele.right:
                queue.append((ele.right, level+1))

        return maxlevel
        
    
        