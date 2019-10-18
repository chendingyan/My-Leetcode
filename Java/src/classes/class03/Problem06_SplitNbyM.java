package classes.class03;

public class Problem06_SplitNbyM {
    public static boolean isPrime(int n){
        if (n < 2){
            return false;
        }
        int max = (int)Math.sqrt((double)n);
        for(int i = 2; i <= max; i++){
            if ((n%i) == 0){
                return false;
            }
        }
        return true;
    }

    public static int[] splitNbyM(int n){
        int sum = 0;
        int count = 0;
        for (int i = 2; i <= n; i++) {
            while (n % i == 0) {
                sum += i;
                count++;
                n /= i;
            }
        }
        return new int[] {sum, count};
    }
    public static int minOps(int n) {
        if (n < 2) {
            return 0;
        }
        if (isPrime(n)) {
            return n - 1;
        }
        int [] ans = splitNbyM(n);
        return ans[0]- ans[1];
    }
    public static void main(String[] args) {
        System.out.println(isPrime(3));
    }
}
