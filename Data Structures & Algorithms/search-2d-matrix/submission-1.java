class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {

        //binary search in 2 d matrix , the core idea is count number of elemnts in the ,matrix
        //apply binary search from 0 to length ;and for each mid find the correspoding insex in 2d matei x and find the number than 
        //compare and use regular vinary search 

        int row = matrix.length;
        int col = matrix[0].length;

        int length = row*col -1;
        int low =0;
        int high = length;

        while (low<=high){
            int mid = (low+high)/2;
            int r = mid/ col; int c = mid%col;
            if(target>matrix[r][c]){
                low= mid+1;
            }
            else if(target< matrix[r][c]){
                high = mid-1;
            }
            else {
                return true;
            }
        }

        return false ;

        
        
        
    }
}