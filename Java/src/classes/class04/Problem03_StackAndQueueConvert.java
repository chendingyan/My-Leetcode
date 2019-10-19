package classes.class04;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

public class Problem03_StackAndQueueConvert {
    public static class StacktoQueue{
        private Stack<Integer> stackpush;
        private Stack<Integer> stackpop;

        public StacktoQueue(){
            this.stackpush = new Stack<Integer>();
            this.stackpop = new Stack<Integer>();
        }

        public void Enqueue(int num){
            stackpush.push(num);
        }

        public int Dequeue(){
            if (stackpop.isEmpty() && stackpush.isEmpty()){
                throw new RuntimeException("Empty!");
            }else if (stackpop.isEmpty()){
                while (! stackpush.isEmpty()){
                    stackpop.push(stackpush.pop());
                }
            }
            return stackpop.pop();
        }
    }

    public static class QueuetoStack{
        private Queue<Integer> queue;
        private Queue<Integer> help;

        public QueuetoStack(){
            this.queue = new LinkedList<Integer>();
            this.help = new LinkedList<Integer>();

        }
        public void push(int num){
            this.queue.add(num);
        }

        public int pop(){
            while(this.queue.size()>1) {
                this.help.add(this.queue.poll());

            }
            int res = this.queue.poll();
            swap();
            return res;
        }
        public void swap(){
            Queue<Integer> temp = this.help;
            this.help = this.queue;
            this.queue = temp;

        }
    }

    public static void main(String[] args) {
        QueuetoStack stack = new QueuetoStack();
        stack.push(1);
        stack.push(2);
        stack.push(3);
        System.out.println(stack.pop());

    }
}

