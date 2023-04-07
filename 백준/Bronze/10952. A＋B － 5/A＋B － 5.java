import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {	
		
		Scanner sc = new Scanner (System.in);
		
		int i;
		
		int A = 1;
		
		int B = 1;
		
		for (i=1 ; A!=0 || B!=0 ; i++) {
		
		A = sc.nextInt();
			
		B = sc.nextInt();	
		
		if (A==0 && B==0) {		
		}
		else
			System.out.println(A + B);
	}	
}
}