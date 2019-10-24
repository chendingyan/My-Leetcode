package classes.class07;

public class Problem07Extra_EnvelopesProblems {
    public static class Envelope {
        public int l;
        public int h;

        public Envelope(int weight, int hight) {
            l = weight;
            h = hight;
        }
    }

    public static int maxEnvelopes(int[][] matrix) {
        return -1;
    }

    public static void main(String[] args) {
        int[][] test = { { 3, 4 }, { 2, 3 }, { 4, 5 }, { 1, 3 }, { 2, 2 }, { 3, 6 }, { 1, 2 }, { 3, 2 }, { 2, 4 } };
        System.out.println(maxEnvelopes(test));
    }

}
