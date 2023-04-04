import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {	
		
		Scanner sc = new Scanner (System.in);
		
		int H = sc.nextInt();
		
		int M = sc.nextInt();
		
		int add = sc.nextInt();
		
		if (M + add < 60) {
			System.out.println(H + " " + (M + add));
		}
		else if (M + add == 60) {
			if (H == 23) {
				System.out.println(0 + " " + 0); 
			}
			else
				System.out.println(H+1 + " " + 0);
		}
		else if (M + add > 60) {
			if (H + ((M + add)/60) >= 24) {
				System.out.println((H + ((M + add)/60)-24) + " " + (M + add)%60);
			}
			else
				System.out.println(H + (M + add)/60 + " " + (M + add)%60);
		}
		
	}
}