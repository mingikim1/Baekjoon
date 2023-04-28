import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner (System.in);
		
		int N = sc.nextInt();
		
		int M = sc.nextInt();
		
		int [] basket = new int [N];
		
		int i, j;
		
		for (int k = 0 ; k < N ; k++) {
			basket[k] = k+1;
		}
		
		for (int k = 1 ; k <= M ; k++) {
			i = sc.nextInt();
			j = sc.nextInt();
			int tmp = basket[i-1];
			basket[i-1] = basket[j-1];
			basket[j-1] = tmp;
		}
		for (int k = 0 ; k < N ; k++) {
			System.out.print(basket[k] + " ");
		}
		
	}
		
}
