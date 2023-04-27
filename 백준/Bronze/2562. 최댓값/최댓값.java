import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner (System.in);
		
		int [] num = new int [9];
		
		int i, j;
		
		for (i = 0 ; i < 9 ; i++) {
			num[i] = sc.nextInt();
		}
		Loop1 : for (i = 0 ; i < 8 ; i++) {
			int count = 0;
			for (j = 1 ; j < 8-i+1 ; j++) {
				if (num[i] >= num[i+j]) {
					count++;
					if (count==8-i) {
						break Loop1;
					}
				}
				else {
					continue Loop1;
				}
			}
		}
		System.out.print(num[i] + "\n" + (i+1));

	}
		
}