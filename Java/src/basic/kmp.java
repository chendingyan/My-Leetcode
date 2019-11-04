package basic;

public  class kmp {
    public static int KMP(String t, String p) {
        char[] target = t.toCharArray();
        char[] pattern = p.toCharArray();
        int i = 0;
        int j = 0;
        int [] next = getNext(pattern);
        while (i < target.length && j < pattern.length){
            if(j == -1 || target[i] == pattern[j]){
                i++;
                j++;
            }else {
                j = next[j];
            }
        }
        if(j == pattern.length){
            return i-j;
        }
        return -1;
    }

    public static int[] getNext(char [] p){

        int[] next = new int[p.length];
        next[0] = -1;
        next[1] = 0;
        int i = 2;
        int cn = 0;
        while (i < p.length){
            if(p[i-1] == p[cn]){
                next[i++] = ++cn;
            }else {
                if(cn > 0){
                    cn = next[cn];
                }else if(cn == 0){
                    next[i++] = 0;
                }
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
        String t = "123abcabcdefgh";
        String p = "abcabcd";
        int [] next = getNext(p.toCharArray());
        printArr(next);
        System.out.println(KMP(t, p));

    }
}
