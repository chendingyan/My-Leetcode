public class Problem32_LongestValidParentheses {
    public int longestValidParentheses(String s) {
        int left = 0;
        int right = 0;
        int maxlength = 0;
        for(int i = 0; i < s.length(); i++){
            char c = s.charAt(i);
            if(c == '('){
                left++;
            }else if(c ==')'){
                right++;
            }

            if (left == right){
                maxlength = Math.max(maxlength, 2 * left);
            }else if(left < right){
                left = 0;
                right = 0;
            }
        }
        left = 0;
        right = 0;
        for(int i = s.length()-1; i > -1; i--){
            char c = s.charAt(i);
            if(c == '('){
                left++;
            }else if(c ==')'){
                right++;
            }

            if (left == right){
                maxlength = Math.max(maxlength, 2 * left);
            }else if(left > right){
                left = 0;
                right = 0;
            }
        }
        return maxlength;
    }
}
