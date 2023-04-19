import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner (System.in);
		
		int N = sc.nextInt();
		
		int [] numArr = new int [N]; 
		
		for (int i = 0 ; i < N ; i++) {
			numArr[i] += sc.nextInt();
		}
		int v = sc.nextInt();
		
		int result = 0;
		
		for (int i = 0 ; i < N ; i++) {
			if (numArr[i] == v) {
				result++;
			}
		}
		System.out.println(result);
		
	}
		
}