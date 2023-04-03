import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {	
		
		Scanner sc = new Scanner (System.in);
		
		int H = sc.nextInt();
		
		int M = sc.nextInt();
		
		if (((60*H + M)-45) < 0) {
			System.out.println(23 + " " + (60-(45-M)));
		}
		
		else
		System.out.println(((60*H + M)-45)/60 + " " + (((60*H + M)-45)%60));
	}
}
