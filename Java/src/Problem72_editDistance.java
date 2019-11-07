public class Problem72_editDistance {
    public int minDistance(String word1, String word2) {
        int [][] dp = new int[word1.length()+1][word2.length()+1];
        for(int i = 0; i < word1.length()+1; i++){
            dp[i][0] = i;
        }

        for(int i = 0; i < word2.length()+1; i++){
            dp[0][i] = i;
        }
        helper.printMatrix(dp);
        char [] w1 = word1.toCharArray();
        char [] w2 = word2.toCharArray();
        for(int i = 1; i < word1.length()+1; i++){
            for(int j = 1; j < word2.length()+1; j++){
                if(w1[i-1] == w2[j-1]){
                    dp[i][j] = dp[i-1][j-1];
                }else {
                    dp[i][j] = Math.min(dp[i-1][j-1], Math.min(dp[i-1][j], dp[i][j-1]))+1;
                }
            }
        }
        return dp[word1.length()][word2.length()];
    }
}
