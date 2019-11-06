import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

public class Problem56_mergeIntervals {
    public static int[][] merge(int[][] intervals) {
        List<int[]> result = new ArrayList<>();
        Arrays.sort(intervals, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return o1[0] - o2[0];
            }
        });

        int i = 0;
        while (i < intervals.length){
            int left = intervals[i][0];
            int right = intervals[i][1];

            while (i < intervals.length-1 && right >= intervals[i+1][0] ){
                i++;
                right = Math.max(right, intervals[i][1]);
            }
            int [] temp = new int[]{left, right};
            result.add(temp);
            i++;
        }

        return result.toArray(new int[result.size()][]);
    }
    public static void printMatrix(int[][] matrix) {
        for (int i = 0; i != matrix.length; i++) {
            for (int j = 0; j != matrix[0].length; j++) {
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        int [][] intervals = new int[][]{{2,6},{1,3}, {8,10}, {15,18}};
        System.out.println(intervals[0].length);
        printMatrix(merge(intervals));
    }
}

