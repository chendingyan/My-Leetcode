//给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
//'.' 匹配任意单个字符
//'*' 匹配零个或多个前面的那一个元素
//所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。
//s 可能为空，且只包含从 a-z 的小写字母。
// p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。

//这居然是一道动态规划的题目
//首先new一个dp数组
//dp[i][j]代表 在s的前i个和p的前j个是否能匹配
//初始化： dp[0][2...j] = (p[j] == "*" && dp[0][i-2]) 我们希望 都是* 而且要dp[0][i-2]也要是true的才行
//然后进行动态规划状态转移 除了正常匹配的情况之外 我们要看p[j] 是不是遇到了特殊字符
//if p[j] == "*" 我们要看前一个位置 if p[j-1] == s[i]  or p[j-1] == "." 说明这个情况等价于 没有看s[i]的情况 dp[i][j] = dp[i-1][j]
// 当然也有可能这个看到的字符一次都没用 dp[i][j] = dp[i][j-2]
// else dp[i][j] = dp[i][j-2]
//if p[j] == "." 或者 s[i] == p[j] dp[i][j] = dp[i-1][j-1]
public class Problem10_RegularExpMatching {
    public static boolean isMatch(String s, String p) {
        char [] str = s.toCharArray();
        char [] pattern = p.toCharArray();

        int len_s  = str.length;
        int len_p = pattern.length;
        boolean [][] dp = new boolean[len_s+1][len_p+1];
        dp[0][0] = true;
        for(int i = 2; i < len_p+1; i++){
            dp[0][i] = (pattern[i-1] == '*' && dp[0][i-2]);
        }

        for(int i = 1; i < len_s+1; i++){
            for(int j = 1; j < len_p+1; j++){
                int m = i-1;
                int n = j-1;
                if (pattern[n] =='*'){
                    if (pattern[n-1] == str[m] || pattern[n-1] =='.'){
                        dp[i][j] = (dp[i-1][j] || dp[i][j-2]);
                    } else {
                        dp[i][j] = dp[i][j-2];
                    }
                }else if (pattern[n] == '.' || pattern[n] == str[m]){
                    dp[i][j] = dp[i-1][j-1];
                }
            }
        }
        return dp[len_s][len_p];
    }

    public static void main(String[] args) {
        String s = "a";
        String p = "ab*a";
        System.out.println(isMatch(s, p ));
    }
}
