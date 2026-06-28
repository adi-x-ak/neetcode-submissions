class Solution {
    public int longestConsecutive(int[] nums) {
        //Intialize the max length to keep track of the longest sequence we found 
        //convert the array into hashset as it doesnt allow diplicate and most importtantly the look up time is 0(1)


        
        int maxLength = 0;
        HashSet<Integer> numsSet = new HashSet<>();

        for( int i=0 ;i<nums.length;i++){
            numsSet.add(nums[i]);
        }

        //now for each number in hashset check is num+1 elelemt is there and update the max legth 
        // u need to ckeck if num-1 is there in set , which indiactes if the elemnt is the starting or not of the sequence 
        // if n-1 is not there we move forward and chech num +1  is there are not there if its there update the 
        //length and find the next 
        

        for(int num : numsSet){
            if(!numsSet.contains(num-1)){
                int length=1;
                while(numsSet.contains(num+length)){
                    length++;
                }
                maxLength = Math.max(maxLength , length);
            }
        }

        return maxLength;


        
    }
}
