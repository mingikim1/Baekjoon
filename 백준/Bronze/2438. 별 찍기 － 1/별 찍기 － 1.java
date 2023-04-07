import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {	
		
		Scanner sc = new Scanner (System.in);
		
		int num = sc.nextInt();
		
		int i;
		
		String star = "";
		
		for (i=1 ; i <= num ; i++) {
			star += "*";
			System.out.println(star);
		}
		
		
}
}
