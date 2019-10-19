package classes.class04;

public class Problem04_MinPathSum {

    public static int minPathSum1(int [][] matrix){
        int row = matrix.length;
        int col = matrix[0].length;
        int [][] dp = new int [row][col];
        dp[0][0] = matrix[0][0];
        for (int i =1; i < col; i++){
            dp[0][i] = dp[0][i-1] + matrix[0][i];
        }
        for(int i = 1; i < row; i++){
            dp[i][0] = dp[i-1][0] + matrix[i][0];
        }
        for (int i = 1; i < row; i++){
            for(int j = 1; j < col; j++){
                dp[i][j] = Math.min(dp[i-1][j] + matrix[i][j], dp[i][j-1] + matrix[i][j]);
            }
        }
        return dp[row-1][col-1];
    }

    public static int minPathSum2(int[][] m) {
        if (m == null || m.length == 0 || m[0] == null || m[0].length == 0) {
            return 0;
        }
        int more = Math.max(m.length, m[0].length); // �����������ϴ���Ǹ�Ϊmore
        int less = Math.min(m.length, m[0].length); // ������������С���Ǹ�Ϊless
        boolean rowmore = more == m.length; // �����ǲ��Ǵ��ڵ�������
        int[] arr = new int[less]; // ��������ĳ��Ƚ�Ϊ�����������е���Сֵ
        arr[0] = m[0][0];
        for (int i = 1; i < less; i++) {
            arr[i] = arr[i - 1] + (rowmore ? m[0][i] : m[i][0]);
        }
        for (int i = 1; i < more; i++) {
            arr[0] = arr[0] + (rowmore ? m[i][0] : m[0][i]);
            for (int j = 1; j < less; j++) {
                arr[j] = Math.min(arr[j - 1], arr[j])
                        + (rowmore ? m[i][j] : m[j][i]);
            }
        }
        return arr[less - 1];
    }

    // for test
    public static void printMatrix(int[][] matrix) {
        for (int i = 0; i != matrix.length; i++) {
            for (int j = 0; j != matrix[0].length; j++) {
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        // int[][] m = generateRandomMatrix(3, 4);
        int[][] m = { { 1, 3, 5, 9 },
                { 8, 1, 3, 4 },
                { 5, 0, 6, 1 },
                { 8, 8, 4, 0 } };
        printMatrix(m);
        System.out.println(minPathSum1(m));
        System.out.println(minPathSum2(m));

    }
}
