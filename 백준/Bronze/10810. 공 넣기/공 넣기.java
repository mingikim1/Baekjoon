import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner (System.in);
		
		int N = sc.nextInt();
		
		int M = sc.nextInt();
		
		int i, j, k;
		
		int [] basket = new int [N];
		
		for (int m = 1 ; m <= M ; m++) {
			i = sc.nextInt();
			j = sc.nextInt();
			k = sc.nextInt();
			for (int n = i-1 ; n <= j-1 ; n++) {
				basket[n] = k;
			}
		}
		for (int m = 0 ; m < N ; m++) {
			System.out.print(basket[m] + " ");
		}
	}
		
}