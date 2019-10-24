package classes.class07;

import com.sun.source.tree.Tree;

import javax.print.DocFlavor;
import java.util.*;

public class Problem06_MaxRevenue {
    public static int [] maxRevenue(int allTime, int [] revenue, int [] times, int [][] dependents){
        int activities = revenue.length;
        int lastNode = -1;

        //将dependents变成关系链表 并且找到最后一个节点
        HashMap<Integer, ArrayList<Integer>> relations = new HashMap<>();
        for(int i = 0; i < activities; i++){
            relations.put(i, new ArrayList<Integer>());
        }
        for(int i = 0; i < dependents.length; i++){
            boolean allZero = true;
            for(int j = 0; j < dependents[0].length; j++){
                if(dependents[i][j] == 1){
                    relations.get(j).add(i);
                    allZero = false;
                }
            }
            if (allZero){
                lastNode = i;
            }
        }

        HashMap<Integer, TreeMap<Integer, Integer>> nodeCostRevenueMap = new HashMap<>();
        for(int i = 0; i < activities; i++){
            nodeCostRevenueMap.put(i, new TreeMap<Integer, Integer>());
        }
        nodeCostRevenueMap.get(lastNode).put(times[lastNode], revenue[lastNode]);
        Queue<Integer> queue = new LinkedList<>();
        ArrayList<Integer> visited = new ArrayList<>();
        queue.add(lastNode);
        while (! queue.isEmpty()){
            int poll = queue.poll();
            visited.add(poll);
            for(int i: relations.get(poll)){
                for(Map.Entry<Integer,Integer> entry : nodeCostRevenueMap.get(poll).entrySet()){
                    int lastTime = entry.getKey() + times[i];
                    int lastRevenue = entry.getValue() + revenue[i];
                    TreeMap<Integer, Integer> curMap = nodeCostRevenueMap.get(i);
                    if(curMap.floorKey(lastTime)== null || curMap.get(curMap.floorKey(lastTime)) < lastRevenue){
                        curMap.put(lastTime, lastRevenue);
                    }
                }

                if(!queue.contains(i) && !visited.contains(i)){
                    queue.add(i);

                }
            }
        }

        TreeMap<Integer, Integer> allMap = new TreeMap<>();
        for(TreeMap<Integer, Integer> curMap : nodeCostRevenueMap.values()){
            for(Map.Entry<Integer,Integer> entry: curMap.entrySet()){
                int time = entry.getKey();
                int money  = entry.getValue();
                if( allMap.floorKey(time) == null || allMap.get(allMap.floorKey(time)) < money ){
                    allMap.put(time, money);
                }
            }
        }




        return new int[] {allMap.floorKey(allTime), allMap.get(allMap.floorKey(allTime))};
    }

    public static void printMatrix(int [][] matrix){
        for(int i = 0; i < matrix.length; i++){
            for(int j = 0; j < matrix[0].length; j++){
                System.out.print(matrix[i][j]);
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int activities = scanner.nextInt();
        int alltime = scanner.nextInt();
        int [] times = new int[activities];
        int [] revenues = new int[activities];
        int [][] dependents = new int[activities][activities];
        for(int i = 0; i < activities; i++){
            times[i] = scanner.nextInt();
            revenues[i] = scanner.nextInt();

            for(int j = 0; j < activities; j++){
                int temp = scanner.nextInt();
                if (temp == 1){
                    dependents[i][j] = 1;
                }
            }
        }
        printMatrix(dependents);
        int[] res = maxRevenue(alltime, revenues, times, dependents);
        System.out.println(res[0] + " , " + res[1]);
    }


}
