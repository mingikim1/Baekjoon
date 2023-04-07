import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {	
		
		Scanner sc = new Scanner (System.in);
		
		String lo = "long";
		
		String in = "int";
		
		int N = sc.nextInt();
		
		int i;
		
		for (i=1 ; i <= N/4 ; i++) {
			System.out.print(lo + " ");
		}
		System.out.print(in);
	}
}