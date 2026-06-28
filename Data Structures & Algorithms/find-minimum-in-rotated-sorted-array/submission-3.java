class Solution {
    public int findMin(int[] nums) {
        int left = 0;
        int right =nums.length-1;

        if(nums[left] <= nums[right]){
            return nums[left];
        }

        while(left<=right){
            int mid = (left+right)/2;
            if((mid+1<nums.length && nums[mid]>nums[mid+1])){
                return nums[mid+1];
            }
            else if((mid-1>=0 && nums[mid]<nums[mid-1])){
                return nums[mid];
            }
            else if(nums[mid]>=nums[left]){
                left=mid+1;
            }
            else {
                right=mid-1;
            }
        }

        return -1;
        
        
    }
}
