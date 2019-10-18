package classes.class03;

import java.util.Comparator;
import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;

//top k 问题

public class Problem07_TopKTimes {
    public static class Node {
        String str;
        int times;

        public Node(String str, int times) {
            this.str = str;
            this.times = times;
        }

        @Override
        public String toString() {
            return this.str + "+" + this.times;
        }
    }

    public static class NodeComparator implements Comparator<Node>{
        @Override
        public int compare(Node o1, Node o2) {
            return o1.times - o2.times;
        }
    }

    public static void topK(String[] str, int K){
        HashMap<String, Integer> map = new HashMap<>();
        for(String s : str){
            if (!map.containsKey(s)){
                map.put(s, 0);
            }
            map.put(s, map.get(s)+1);
        }

        PriorityQueue<Node> heap = new PriorityQueue<>(new NodeComparator());
        for(Map.Entry<String, Integer> entry : map.entrySet()){
            Node node = new Node(entry.getKey(), entry.getValue());
            if (heap.size() >= K){
                System.out.println(heap.peek().times + " " + node.times);
                if(heap.peek().times < node.times){
                    heap.poll();
                    heap.add(node);
                    System.out.println(heap);
                }
            }else {
                heap.add(node);
                System.out.println(heap);
            }

        }
        while (!heap.isEmpty()) {
            System.out.println(heap.poll().str);
        }
    }

    public static String[] generateRandomArray(int n, int max){
        String[] res =new String[n];
        for (int i = 0; i < n; i++){
            res[i] = String.valueOf((int) (Math.random() * (max + 1)));

        }
        return res;
    }

    public static void printArray(String[] arr) {
        for (int i = 0; i != arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        String[] arr1 = { "0", "3", "3", "7", "8", "8" };
        topK(arr1, 3);
        String[] arr2 = { "A", "B", "A", "C", "A", "C", "B", "B", "K" };
        topK(arr2, 3);
//        String [] arr2 = generateRandomArray(6,10);
//        printArray(arr2);
//        topK(arr2, 3);

    }
}
