class Solution {
    public int numRescueBoats(int[] people, int limit) {

        //Sort the array

        Arrays.sort(people);
        int left =0;
        int right =people.length-1;

        int boat_counter = 0;

        while(left<=right){

            int sum = people[left] + people[right];
            if(sum<=limit){
                boat_counter++;
                left++;
                right--;

            }
            else {
                boat_counter++;
                right--;
            }

            
        }

        return boat_counter;



        
    }
}