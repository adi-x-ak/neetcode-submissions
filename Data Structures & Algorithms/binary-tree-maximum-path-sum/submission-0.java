/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public int maxPathSum(TreeNode root) {
        int[] ans = new int[1];
         ans[0] = Integer.MIN_VALUE;
        dfs(root,ans);
        return ans[0];





       
        
    }

    public int dfs(TreeNode root, int[]res){
        if(root==null) return 0;

        int left = dfs(root.left,res);
        int right = dfs(root.right,res);
        left = Math.max(0,left);
        right = Math.max(0,right);
        res[0] = Math.max(res[0] , left+right+root.val);

        return root.val+Math.max(left,right);
    }
}
