package classes.class05;

import java.util.*;

public class Problem07_ChooseWork {
    public static class Job {
        public int money;
        public int hard;

        public Job(int money, int hard) {
            this.money = money;
            this.hard = hard;
        }

        @Override
        public String toString() {
            return "("+ this.hard + " " + this.money+")";
        }
    }

    public static class jobComparator implements Comparator<Job>{
        @Override
        public int compare(Job o1, Job o2) {
            return o1.hard != o2.hard ? (o1.hard - o2.hard) : (o2.money - o1.money);
        }
    }

    public static int [] chooseWork(Job [] jobs, int [] ability){
        Arrays.sort(jobs,new jobComparator());

        TreeMap<Integer, Integer> jobMap = new TreeMap<>();
        int maxMoney = 0;
        for (int i = 0; i < jobs.length; i++){
            if(!jobMap.containsKey(jobs[i].hard) && jobs[i].money > maxMoney){
                jobMap.put(jobs[i].hard, jobs[i].money);
                maxMoney = jobs[i].money;
            }
        }


        int [] result = new int[ability.length];
        for(int i = 0; i < ability.length; i++){
            result[i] = jobMap.get(jobMap.floorKey(ability[i]));
        }
        return result;
    }

    public static void printArr(int [] arr){
        for(int i = 0; i < arr.length; i++){
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }


    public static void main(String[] args) {
        Job job1 = new Job(100,1);
        Job job2 = new Job(1000,10);
        Job job3 = new Job(100,10);
        Job job4 = new Job(1001, 1000000000);
        Job job5 = new Job(99, 100000001);
        Job [] jobArr = {job1, job2,job4};
        int [] ability = {9,10,1000000000};
        int [] result = chooseWork(jobArr, ability);
        printArr(result);
    }
}
