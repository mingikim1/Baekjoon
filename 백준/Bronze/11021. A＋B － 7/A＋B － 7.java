import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {	
		
		Scanner sc = new Scanner (System.in);
		
		int A;
		
		int B;
		
		int T = sc.nextInt();
		
		int result = 0;
		
		int i;
		
		for (i=1 ; i <= T ; i++) {
			A = sc.nextInt();
			B = sc.nextInt();
			System.out.printf("Case #%d: %d\n", i, A+B);
		}
}
}
