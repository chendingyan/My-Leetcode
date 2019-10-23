package classes.class06;

public class Problem04_PreAndInArrayToPosArray {
    public static int [] getPosArray(int [] pre, int [] in){
        if (pre == null || in == null) {
            return null;
        }
        return null;

    }


    public static void printArray(int[] arr) {
        if (arr == null) {
            return;
        }
        for (int i = 0; i != arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        int[] pre = { 1, 2, 4, 5, 3, 6, 7 };
        int[] in = { 4, 2, 5, 1, 6, 3, 7 };
        int[] pos = getPosArray(pre, in);
        printArray(pos);

    }
}
