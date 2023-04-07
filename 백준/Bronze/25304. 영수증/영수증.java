import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {	
		
		Scanner sc = new Scanner (System.in);
		
		int X = sc.nextInt();
					
		int N = sc.nextInt();
		
		int i;
		
		int a;
		
		int b;
		
		int sum = 0;
		
		for (i=1 ; i <= N ; i++) {
			a = sc.nextInt();
			b = sc.nextInt();
			int price = a * b;
			sum += price;
		}
		
		if (X == sum) {
			System.out.println("Yes");
		}
		else
			System.out.println("No");
		
	}
}