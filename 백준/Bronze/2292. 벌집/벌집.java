import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner (System.in);
		
		int N = sc.nextInt();
		
		int f = 1;
		
		while (true) {
			if (3*f*(f-1) + 2 > N) {
				break;
			}
			f++;
		}
		System.out.println(f);
		
	}

}
