public class Problem64_minimumPathSum {
    public static int minPathSum(int[][] grid) {
        int [][] dp = new int[grid.length][grid[0].length];
        dp[0][0] = grid[0][0];
        for(int i = 1; i < grid.length; i++){
            dp[i][0] = dp[i-1][0] + grid[i][0];
        }
        for(int i = 1; i < grid[0].length; i++){
            dp[0][i] = dp[0][i-1] + grid[0][i];
        }

        for(int i = 1; i < grid.length; i++){
            for(int j = 1; j < grid[0].length; j++){
                dp[i][j] = Math.min(dp[i-1][j], dp[i][j-1]) + grid[i][j];
            }
        }
        return dp[grid.length-1][grid[0].length-1];
    }

    public static int minPathSum2(int[][] grid) {
        int row = grid.length;
        int col = grid[0].length;
        int [] dp = new int[col];
        int [] left = new int[row];
        dp[0] = grid[0][0];
        for(int i = 1; i < col; i++){
            dp[i] = dp[i-1] + grid[0][i];
        }
        left[0] = grid[0][0];

        for(int i = 1; i < row; i++){
            left[i] = left[i-1] + grid[i][0];
        }
        for(int i = 1; i < row; i++){
            for(int j = 1; j < col; j++){
                int temp = j == 1? left[i] : dp[j-1];
                dp[j] = Math.min(dp[j], temp)+ grid[i][j];
            }
        }
        return dp[col-1];
    }


    public static void main(String[] args) {
        int [][] grid = new int[][]{{1,3,1}, {1,5,1}, {4,2,1}};
        System.out.println(minPathSum2(grid));
    }
}
