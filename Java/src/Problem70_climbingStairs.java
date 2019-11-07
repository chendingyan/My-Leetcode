public class Problem70_climbingStairs {
    public static int climbStairs(int n) {
        if(n == 1){return 1;}
        int [][] base = new int[][]{{1,1}, {1,0}};
        int [][] pre = new int[][]{{2,1}};
        int [][] res = matrixMulti(pre, matrixPower(base, n-2));

        return res[0][0];
    }

    public static int numPower(int base, int n){
        int temp = base;
        int res = 1;
        while (n > 0){
            if ((n & 1) != 0){
                res *= temp;

            }
            temp *= temp;
            n = (n >> 1);
        }
        return res;

    }

    public static int [][] matrixPower(int[][] base, int n){
        int [][] temp = base;
        int [][] res = new int[base.length][base[0].length];
        for(int i = 0; i < base.length; i++){
            res[i][i] = 1;
        }
        while (n > 0){
            if ((n & 1) != 0){
                res = matrixMulti(res, temp);
            }
            temp = matrixMulti(temp, temp);
            n = (n >> 1);
        }
        return res;
    }
    public static int [][] matrixMulti(int [][] m1, int [][] m2){
        int row = m1.length;
        int col = m2[0].length;
        int [][] res = new int[row][col];
        for(int i = 0; i < row; i++){
            for(int j = 0; j < col; j++){
                for(int m = 0; m < m1[0].length; m++){
                    res[i][j] += m1[i][m] * m2[m][j];
                }
            }
        }
        return res;
    }

    public static void main(String[] args) {
        for(int i = 1; i< 20; i++){
            System.out.println(climbStairs(i));
        }
    }
}
