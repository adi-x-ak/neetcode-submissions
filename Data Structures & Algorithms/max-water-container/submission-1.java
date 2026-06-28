class Solution {
    public int maxArea(int[] heights) {

        int i=0;
         int j = heights.length-1;
         int maximun_area = 0;
         while(i<j){
            int area = Math.min(heights[i] , heights[j]) *(j-i);
            maximun_area = Math.max(maximun_area , area );

            if(heights[i]<=heights[j]){
                i++;
            }
            else {
                j--;
            }
            
         }

         return maximun_area;
        
    }
}
