class Solution {
    public int calPoints(String[] operations) {
        // this question me mainly trying to get use to solve stack propblems ans to increase my speed of coding 

        //create a stack ds 
        Stack<Integer> stack = new Stack<>();

        int result =0;

        for(String op : operations){
            if(op.equals("+")){
                int top = stack.pop();
                int newtop = top + stack.peek();
                stack.push(top);
                stack.push(newtop);
                result += newtop;
            } else if(op.equals("D")){
                stack.push(2*stack.peek());
                result += stack.peek();
               
            }
            else if (op.equals("C")){
                result -= stack.pop();
            }
            else{
                stack.push(Integer.parseInt(op));
                result += stack.peek();
            }
        }
        return result;

        
    }
}