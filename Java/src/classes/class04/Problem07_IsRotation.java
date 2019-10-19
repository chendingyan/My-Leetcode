package classes.class04;
//double一下词语 然后看一下是不是子字符串就好了 可以用KMP检查

public class Problem07_IsRotation {
    public static int KMP(String s1, String s2){
        char [] target = s1.toCharArray();
        char [] pattern = s2.toCharArray();

        int i = 0;
        int j = 0;
        int [] next = getNext(s2);
        while(i < target.length && j < pattern.length){
            if(target[i] == pattern[j]){
                i++;
                j++;

            }else if(j > 0){
                j = next[j];
            }else{
                i++;
            }
        }
        return j == pattern.length? i-j : -1;
    }

    public static int [] getNext(String s){
        char [] pattern = s.toCharArray();
        int [] next = new int[pattern.length];
        next[0] = -1;
        int i = 0;
        int j = -1;
        while(i < pattern.length-1){
            if(j == -1 || pattern[i] == pattern[j]){
                i++;
                j++;
                next[i] = j;

            }else {
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
        String s = "abaabaabbabaaabaabbabaab";
        String p = "abaabbabaab";
        printArr(getNext(p));
        System.out.println(KMP(s, p));

    }
}
