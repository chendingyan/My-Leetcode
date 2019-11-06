import java.util.Arrays;

public class Problem62_UniquePaths {
    public static int uniquePaths(int m, int n) {
        int [][] dp = new int[n][m];
        for(int i =0; i < n; i++){
            dp[i][0] = 1;
        }
        for(int i = 0; i < m; i++){
            dp[0][i] = 1;
        }

        for(int i = 1; i < n; i++){
            for(int j = 1; j < m; j++){
                dp[i][j] = dp[i-1][j] + dp[i][j-1];
            }
        }
        return dp[n-1][m-1];
    }

    //方法的优化 动态规划的空间压缩技巧！
    // 优化1：记录两行
    public static int uniquePaths2(int m, int n) {
        int pre [] = new int[m];
        int cur [] = new int[m];
        Arrays.fill(pre, 1);
        Arrays.fill(cur, 1);


        for(int i = 1; i < n; i++){
            for(int j = 1; j < m; j++){
                cur[j] = pre[j] + cur[j-1];
            }
            pre = cur.clone();
        }
        return cur[m-1];
    }

    //优化2：记录一行
    public static int uniquePaths3(int m, int n) {
        int dp [] = new int[m];
        Arrays.fill(dp, 1);
        for(int i = 1; i < n; i++){
            for(int j = 1; j < m; j++){
                dp[j] += dp[j-1];
            }
        }
        return dp[m-1];
    }
    public static void main(String[] args) {
        System.out.println(uniquePaths(3,2));
        System.out.println(uniquePaths(7,3));
    }


}
