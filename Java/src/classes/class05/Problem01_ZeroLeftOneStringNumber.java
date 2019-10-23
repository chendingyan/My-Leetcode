package classes.class05;

public class Problem01_ZeroLeftOneStringNumber {
    public static int numPower(int base, int n){
        int temp = base;
        int num = 1;
        while(n > 0 ){
            if((n & 1)!= 0){
                num *= temp;
            }
            temp *= temp;
            n = (n >> 1 );
        }
        return num;
    }

    public static int[][] matrixPower(int [][]base, int n){
        int [][] temp = base;
        int [][] num = new int [base.length][base[0].length];
        for(int i = 0; i < base.length; i++){
            num[i][i] = 1;
        }
        while(n > 0){
            if((n&1)!=0){
                num = matrixMulti(num, temp);
            }
            temp = matrixMulti(temp,temp);
            n = (n>>1);
        }
        return num;
    }

    public static int[][] matrixMulti(int [][] m1, int [][] m2){
        int [] [] res = new int[m1.length][m2[0].length];
        for(int i = 0; i < m1.length;i++){
            for(int j = 0; j < m2[0].length; j++){
                for(int k = 0; k < m2.length; k++){
                    res[i][j] += m1[i][k] * m2[k][j];
                }
            }
        }
        return res;
    }

    public static int fib(int n){
        if(n<1){
            return 0;
        }
        if(n==1 || n ==2){
            return 1;
        }
        int [][]base = {{1,1,},{1,0}};
        int [][] pre = {{1,1}};

        int [][]res = matrixMulti(pre , matrixPower(base, n-2));
        return res[0][0];
    }

    public static void printMatrix(int[][] matrix) {
        for (int i = 0; i != matrix.length; i++) {
            for (int j = 0; j != matrix[0].length; j++) {
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println();
        }
    }


    public static int fib2(int n){
        if(n<1){
            return 0;
        }
        if(n==1 || n ==2){
            return 1;
        }
        return fib2(n-1) + fib2(n-2);
    }


    public static void main(String[] args) {

        for(int i = 5; i <20; i++){
            System.out.println(fib(i) == fib2(i));
        }
    }
}
