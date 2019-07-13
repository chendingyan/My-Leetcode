package class02;

public class Problem06_Eat {

	public static void printWinner(int n) {
		if (n % 5 == 0 || n % 5 == 2) {
			System.out.println("yang");
		} else {
			System.out.println("niu");
		}
	}
	public static void main(String[] args) {
		for (int i = 1; i < 20; i++){
			printWinner(i);
		}
	}
}
