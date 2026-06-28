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
    private boolean balanced = true;
    public boolean isBalanced(TreeNode root) {
        if(root==null){
            return true;
        }

        dfsHeight(root);

        return balanced;
    }

    int dfsHeight(TreeNode root){

        if(root==null){
            return 0;
        }

     
            int leftHeight= dfsHeight(root.left);
            int rightHeight =dfsHeight(root.right) ;

            int gap=Math.abs(leftHeight-rightHeight);

            if(gap>1){
               this.balanced=false; 
            }

            return Math.max(leftHeight,rightHeight)+1;
        
    }
}
