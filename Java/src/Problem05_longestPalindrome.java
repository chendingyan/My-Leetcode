//给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
//Manacher算法
//首先 我们要考虑四个遍历 回文半径 回文半径数组 R（最右回文右边界） C（最右回文右边界的对称中心）
//然后对于这个问题 进行分类
//1)i在R外 我们没有办法加速 只能暴力破解 尝试以这个点为中心左右扩展
//2)i在R内
//L  i'  C   i   R
//那我们还有三种情况 和i'有关
//L （ i' ）  C   i   R
// 情况2：i'的回文半径左右 都在L和C之间 说明是一个大回文里面的小回文 通过分析 说明i的回文半径 = i'的回文半径 pArr[i] = pArr[i']
//（ L  i'    ） C   i   R
//情况三：i' 的回文左侧 超出了 L 那么pArr[i] = i...R的距离
//情况四：i'的回文左侧刚好压线 那么pArr[i]至少是i...R 的距离 但外面是不是还是回文不知道 要暴力扩
//最后我们返回的是这个子串String
public class Problem05_longestPalindrome {
    public static char[] addSharp(String s){
        char [] str = s.toCharArray();
        char [] res = new char[str.length * 2 + 1];
        int index = 0;
        for(int i = 0; i < res.length; i++){
            res[i] = (i & 1) == 0? '#': str[index++];
        }
        return res;
    }
    public static String longestPalindrome(String s) {
        if (s == null || s.length()==0){
            return "";
        }
        char [] str = addSharp(s);
        int [] pArr = new int[str.length];
        int C = -1;
        int R = -1; //这里R是最右回文右边界位置的下一个位置 方便下标计算
        int max_R = Integer.MIN_VALUE;
        int max_R_index = -1;
        for(int i = 0; i < str.length; i++){
            // i' = C - (i-C) = 2* C - i
            pArr[i] = (i < R)? Math.min(pArr[2*C-i], R-i): 1;

            while(i + pArr[i] < str.length && i- pArr[i] >= 0){
                if(str[ i+ pArr[i] ]== str[i-pArr[i]]){
                    pArr[i]++;
                }else {
                    break;
                }
            }
            if (i + pArr[i] > R){
                R = i + pArr[i];
                C = i;
            }
            if (pArr[i] > max_R){
                max_R = pArr[i];
                max_R_index = i;
            }
        }
        System.out.println( max_R_index+", " + (max_R-1));
        String ans = String.valueOf(str);
        System.out.println(ans);
        return ans.substring(max_R_index-max_R+1, max_R_index + max_R).replaceAll("#", "");
    }

    public static void main(String[] args) {
        //#b#b#
        String s = "bb";
        System.out.println(longestPalindrome(s));
    }
}
