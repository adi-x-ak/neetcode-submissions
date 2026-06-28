class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<>();

        for(String str : tokens){
            if(str.equals("+")){
                stack.push(stack.pop()+stack.pop());
            }
            else if(str.equals("-")){
                int a = stack.pop();
                int b = stack.pop();
                stack.push(b-a);
            }

            else if(str.equals("*")){
                stack.push(stack.pop() * stack.pop());
            }
            else if(str.equals("/")){
                int c = stack.pop();
                int d = stack.pop();
                stack.push(d/c);
            }
            else{
                stack.push(Integer.parseInt(str));
            }


        }
        return stack.pop();
        
    }
}
