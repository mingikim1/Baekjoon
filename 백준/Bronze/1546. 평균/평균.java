import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner (System.in);
		
		int N = sc.nextInt();
		
		double [] score = new double [N];
		
		int i;
		
		for (i = 0 ; i < N ; i++) {
			score[i] = sc.nextInt();
		}
		Loop1 : for (i = 0; i < N ; i++) {
					int count = 0;
					if (i == N-1) {
						break;
					}
			for (int j = i+1 ; j < N ; j++) {
				if (score[i] >= score[j]) {
					count++;
					if (count == N-i-1) {
						break Loop1;
					}
				}
				else {
					continue Loop1;
				}
			}
		}
		double M = score[i];
		
		for (i = 0 ; i < N ; i++) {	
			score[i] = score[i]/(M*1.0)*100;		
		}
		double sum = 0;
		for (double value : score) {
			sum += value;
		}
		System.out.println(sum/N);		
		
	}
		
}