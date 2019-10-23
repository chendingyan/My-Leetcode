package classes.class05;

public class Problem03_NearMultiple4Times {
    public static boolean isFourTimes(int [] arr){
        int odd = 0;
        int normalEven = 0;
        int four = 0;

        for(int i : arr){
            if (i % 4 ==0){
                four++;
            }else if(i % 2 == 0){
                normalEven++;
            }else {
                odd++;
            }
        }
        System.out.println(odd+" "+  normalEven+ " "+ four);
        return normalEven == 0 ? (odd <= four+1) : (odd <= four);
    }

    public static void main(String[] args) {
        int [] arr  = {1,2,2,4,4,1,1,4};
        System.out.println(isFourTimes(arr));
    }
}
