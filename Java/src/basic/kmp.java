package basic;

public class kmp {
    public static int KMP(String t, String p) {
        char[] target = t.toCharArray();
        char[] pattern = p.toCharArray();
        int i = 0;
        int j = 0;
        int[] next = getNext(pattern);

        while (i < target.length && j < pattern.length) {
            if (j == -1 || target[i] == pattern[j]) {
                i++;
                j++;
            } else {
                j = next[j];
            }
        }
        if (j == pattern.length)
            return i - j;
        else
            return -1;
    }

    public static int[] getNext(char [] p){

        int[] next = new int[p.length];
        next[0] = -1;
        int i = 0;
        int j = -1;

        while(i < p.length - 1) {
            if (j == -1 || p[i] == p[j]) {
                i++;
                j++;
                next[i] = j;
            } else {
                j = next[j];
            }
        }

        return next;
    }
    public static void printArr(int [] arr){
        for(int i = 0; i < arr.length; i++){
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        String t = "abcabcdefgh";
        String p = "abcabcd";
        int [] next = getNext(p.toCharArray());
        printArr(next);

    }
}
