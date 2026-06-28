class Solution {
    public int majorityElement(int[] nums) {
        int count =0;
        int variable =0;

        for(int i=0;i<nums.length;i++){
            if(count==0){
                count =1;
                variable = nums[i];
            }
            else if(nums[i] == variable){
                count++;
            }
            else {
                count--;
            }
        }
        int count1=0;

        for(int i=0;i<nums.length;i++){
            if(variable==nums[i]){
                count1++;
            }

        }

        if(count1>nums.length/2){
            return variable;
        }

        return -1;
        
    }
}