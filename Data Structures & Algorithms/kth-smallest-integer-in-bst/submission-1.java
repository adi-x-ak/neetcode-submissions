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
    public int kthSmallest(TreeNode root, int k) {

        //the algorithm inorder traversal of binary search tree is always asccending order 

        //while doing the inorder traversal keep an counter variable so when it reaches k resturn the result 
     List<Integer> arr = new ArrayList<>();
     dfs(root,arr);
     return arr.get(k-1);
        
    }

    public void dfs(TreeNode  node ,List<Integer>arr ){
        if(node == null){
            return;
        }
        dfs(node.left , arr);
        arr.add(node.val);
        dfs(node.right,arr);


    }
}
