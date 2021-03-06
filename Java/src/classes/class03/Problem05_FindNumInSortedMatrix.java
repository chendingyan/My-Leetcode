package classes.class03;

public class Problem05_FindNumInSortedMatrix {
    public static boolean isContains(int[][]matrix, int target){
        int x = 0;
        int y = matrix[0].length-1;
        while (x < matrix.length && y >=0){
            if (matrix[x][y] == target){
                return true;
            }else if (matrix[x][y] > target){
                y-=1;
            }else if (matrix[x][y] < target){
                x+=1;
            }
        }
        return false;
    }
    public static void main(String[] args) {
        int[][] matrix = new int[][] { { 0, 1, 2, 3, 4, 5, 6 },// 0
                { 10, 12, 13, 15, 16, 17, 18 },// 1
                { 23, 24, 25, 26, 27, 28, 29 },// 2
                { 44, 45, 46, 47, 48, 49, 50 },// 3
                { 65, 66, 67, 68, 69, 70, 71 },// 4
                { 96, 97, 98, 99, 100, 111, 122 },// 5
                { 166, 176, 186, 187, 190, 195, 200 },// 6
                { 233, 243, 321, 341, 356, 370, 380 } // 7
        };
        int K = 234;

        System.out.println(isContains(matrix,K));
    }
}
