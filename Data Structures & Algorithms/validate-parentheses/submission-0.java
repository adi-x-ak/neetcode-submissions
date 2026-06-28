class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        //create a hashmap more like lookup 
        Map<Character , Character> closeToopen = new HashMap<>();

        closeToopen.put(')' , '(');
        closeToopen.put(']' , '[');
        closeToopen.put('}' , '{');

        //loop throuch each character in a string 
        for (char ch : s.toCharArray()){
            if(closeToopen.containsKey(ch)){
                if(!stack.isEmpty() && stack.peek() == closeToopen.get(ch)){
                    stack.pop();
                }
                else{
                    return false;
                }
            }
            else{
                stack.push(ch);
            }
        }

        return stack.isEmpty();

        
    }
}