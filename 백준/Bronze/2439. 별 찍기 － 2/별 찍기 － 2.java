import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {	
		
		Scanner sc = new Scanner (System.in);
		
		int num = sc.nextInt();
		
		int i;
		
		int j;
		
		int k;
		
		String blank;
		
		String star = "*";
		
		for (k=1 ; k <= num ; k++) {
			blank = "";
		for (i=k ; i <= num-1 ; i++) {
			blank += " ";
		}
		for (j=1 ; j <= k ; j++) {
			blank += star;
		}
		System.out.println(blank);
	}	
}
}