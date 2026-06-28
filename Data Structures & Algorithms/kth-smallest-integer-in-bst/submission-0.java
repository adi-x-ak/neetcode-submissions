class Solution {
    int count = 0;
    int result = -1;

    public int kthSmallest(TreeNode root, int k) {
        inorder(root, k);
        return result;
    }

    public void inorder(TreeNode root, int k) {
        if (root == null || count >= k) {
            return;
        }

        // Traverse the left subtree
        inorder(root.left, k);
        
        // Process the current node
        count++;
        if (count == k) {
            result = root.val;
            return;
        }

        // Traverse the right subtree
        inorder(root.right, k);
    }
}
