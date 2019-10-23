package classes.class05;
//设计并实现TopKRecord结构，可以不断地向其中加入字符串，并且可以根据字符串出现的情况随时打印加入次数最多的前k个字符串。
// 具体为: 1)k在TopKRecord实例生成时指定，并且不再变化(k是构造TopKRecord的参数)。
//        2)含有 add(String str)方法，即向TopKRecord中加入字符串。
//        3)含有 printTopK()方法，即打印加入次数最多的前k个字符串，打印有哪些 字符串和对应的次数即可，不要求严格按排名顺序打印。
//        4)如果在出现次数最多的前k个字符串中，最后一名的字符串有多个，比如出 现次数最多的前3个字符串具体排名为:
//        A 100次 B 90次 C 80次 D 80次 E 80次，其他任何字符串出现次数都 不超过80次
//        那么只需要打印3个，打印ABC、ABD、ABE都可以。也就是说可以随意抛弃最 后一名，只要求打印k个
//        要求:
//        1)在任何时候，add 方法的时间复杂度不超过 O(logk)
//        2)在任何时候，printTopK方法的时间复杂度不超过O(k)


import java.util.HashMap;

// 维持三个结构 map1 关于字符串的计数器
// 自己实现的heap 最小堆排列
// map2 关于字符串在最小堆位置的记录器
public class Problem05_TopKTimesRealTime {

    public class Node{
        public String str;
        public int times;

        public Node(String str, int times){
            this.str = str;
            this.times = times;
        }
    }

    public class TopKRecord{
        public int k;
        private Node[] heap;
        private HashMap<String, Node> map1;
        private HashMap<Node, Integer> map2;




        public TopKRecord(int k){
            this.heap = new Node[k];
            map1 = new HashMap<>();
            map2 = new HashMap<>();
        }

        public void add(String str){
            Node curNode= null;
            if(!map1.containsKey(str)){
                curNode = new Node(str, 1);
                map1.put(str, curNode);

            }
        }


    }
}
