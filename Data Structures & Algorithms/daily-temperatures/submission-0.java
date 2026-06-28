class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        //create a list result with zero
        int[] result = new int[temperatures.length];
        Stack<Pair> stack = new Stack<>();

        //loop through the temperatures array

        for(int i=0;i<temperatures.length;i++){
            int t=temperatures[i];
            while(!stack.isEmpty() && t>stack.peek().temp){
                Pair p = stack.pop();
                result[p.index] = i-p.index;

            }

            stack.push(new Pair(t, i));
        }

        return result;
        
        
    }



}


//create a pair class easy understanding than the array method for me 

class Pair{
    int temp;
    int index;

    Pair( int temp, int index){
        this.temp=temp;
        this.index=index;
    }
}
