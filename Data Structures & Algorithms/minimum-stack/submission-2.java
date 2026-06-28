class MinStack {
    Stack<Long> stack;
    long min;

    public MinStack() {
        stack = new Stack<>();
    }
    
    public void push(int val) {
      if(stack.isEmpty()){
        min=(long)val;
        stack.push(0L);
      }
      else {
        stack.push((long)val - min);
        if (val < min) min = (long)val;
      }
    }
    
    public void pop() {
      if(stack.isEmpty()) return;
      long pop = stack.pop();
      if (pop < 0) min = min - pop;
    }
    
    public int top() {
        long top = stack.peek();
        if (top > 0) {
          return (int)(top + min);
        } else {
          return (int)min;
        }
    }
    
    public int getMin() {
      return (int)min;
    }
}