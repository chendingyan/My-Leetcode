public class Problem48_rotateImage {

    public static void rotate(int[][] matrix) {
        int ax= 0, ay = 0;
        int bx = matrix.length-1;
        int by = matrix[0].length-1;
        while (bx > ax){
            rotateCircle(matrix, ax++, ay++, bx--, by--);
        }
        printMatrix(matrix);

    }

    public static void rotateCircle(int [][] matrix, int ax, int ay, int bx, int by){
        for(int i = 0; i < by-ay; i++){
            int temp = matrix[ax+i][by];
            matrix[ax+i][by] = matrix[ax][ay+i];
            matrix[ax][ay+i] = matrix[bx-i][ay];
            matrix[bx-i][ay] = matrix[bx][by-i];
            matrix[bx][by-i] = temp;
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
        int [][] matrix = new int[][]   {{1,2,3},
                                        {4,5,6},
                                        {7,8,9}};
        rotate(matrix);
    }
}
