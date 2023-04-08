import java.util.Scanner;

public class Main {	
	
	public static void main(String[] args) {	
		
		Scanner sc = new Scanner (System.in);	
		
		int i;
		
		int m = 0;
		
		long A = sc.nextInt();
		
		long B = sc.nextInt();
			
		if (A <= B) {
			
			for (i=1 ; i <= B ; i++) {
				
				if (A%(i*1.0) == 0.0 && B%(i*1.0) == 0.0) {
					m = i;
				}
				}

		System.out.println((A/m)*(B/m)*m);	
		}
		if (A > B) {
			for (i=1 ; i <= A ; i++) {
				
				if (A%(i*1.0) == 0.0 && B%(i*1.0) == 0.0) {
					m = i;
				}
				
				}

		System.out.println((A/m)*(B/m)*m);	
		}
	}
}
