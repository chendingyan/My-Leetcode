package classes.class06;

public class Problem07_SubMatrixMaxSum {
    public static int maxSum(int [][] matrix){
        int row = matrix.length;
        int col = matrix[0].length;
        int cur = 0;
        int max = 0;
        for(int i = 0; i < row; i++ ){
            int[] s = new int[col];
            for (int j = i; j < row; j++){
                cur = 0;
                for(int k = 0; k < s.length; k++){
                    s[k] += matrix[j][k];
                    cur +=s[k];
                    max = Math.max(max, cur);
                    cur = (cur < 0)?  0: cur;
                }
            }
        }
        return max;
    }

    public static void main(String[] args) {
        int[][] matrix = { { -90, 48, 78 }, { 64, -40, 64 }, { -81, -7, 66 } };
        System.out.println(maxSum(matrix));

    }
}
