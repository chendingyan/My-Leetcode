package classes.class04;

import java.util.Stack;

public class Problem02_GetMinStack {
    public static class myStack{
        private Stack<Integer> stack;
        private Stack<Integer> minStack;
        public myStack(){
            this.stack = new Stack<Integer>();
            this.minStack = new Stack<Integer>();
        }

        public void push(int num){
            if (this.stack.isEmpty()){
                this.minStack.push(num);
            }else if (this.minStack.peek() >= num){
                this.minStack.push(num);
            }
            this.stack.push(num);

        }

        public int pop(){
            if(this.stack.isEmpty()){
                throw new RuntimeException("Stack is Empty");
            }
            int value = this.stack.pop();
            if  (value == this.minStack.peek()){
                this.minStack.pop();
            }
            return value;
        }

        public int getMin(){
            if(this.minStack.isEmpty()){
                throw new RuntimeException("Stack is Empty");
            }
            return minStack.peek();
        }
    }
}
