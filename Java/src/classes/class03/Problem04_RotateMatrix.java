package classes.class03;

public class Problem04_RotateMatrix {
    public static void rotateMatrix(int [][]matrix){
        int ax = 0;
        int ay = 0;
        int bx = matrix.length-1;
        int by = matrix[0].length-1;
        while (ax < bx){
            rotateCircle(matrix,ax++,ay++,bx--,by--);

        }
    }
    public static void rotateCircle(int [][] matrix, int ax, int ay, int bx, int by){
        int temp = 0;
        for(int i = ax; i != bx; i++){
            temp = matrix[ax][ay+i];
            matrix[ax][ay+i] = matrix[bx-i][ay];
            matrix[bx-i][ay] = matrix[bx][by-i];
            matrix[bx][by-i] = matrix[ax+i][by];
            matrix[ax+i][by] = temp;
        }
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
        int[][] matrix = { { 1, 2, 3, 4 }, { 5, 6, 7, 8 }, { 9, 10, 11, 12 },
                { 13, 14, 15, 16 } };
        printMatrix(matrix);
        System.out.println();
        rotateMatrix(matrix);
        printMatrix(matrix);
    }
}
