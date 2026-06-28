class Solution {
    public int minEatingSpeed(int[] piles, int h) {
      int max = Arrays.stream(piles).max().getAsInt();

      int left=1;

      int right=max;
      int ans=Integer.MAX_VALUE;
    
    while(left<=right){
        int mid = (left+right)/2;
        int time=0;
        for (int i=0;i<piles.length;i++){
            time += (int) Math.ceil((double) piles[i] / (double) mid);
        }
            
        if(time<=h){
            ans=Math.min(ans,mid);
            right=mid-1;
        }
        else {
            left=mid+1;
        }

        



    }

    return ans ;
    





        
        
        
    }
}
