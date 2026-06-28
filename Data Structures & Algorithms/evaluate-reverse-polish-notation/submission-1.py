class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        '''
        when we see the numbers we need to push into the stack , when we find
        an operator we need to take the previously pushed two values and do the following operation
        and push to stack and continuue till the end pop the final result out '''
        for c in tokens:
            if c== "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a,b =stack.pop() , stack.pop()
                stack.append(b-a)
            elif c == "*":
                stack.append(stack.pop()*stack.pop())
            elif c == "/":
                a,b = stack.pop() , stack.pop()
                stack.append(int(float(b)/a))
            else:
                stack.append(int(c))
        return stack[0]
            
        