import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner (System.in);
		
		int N = sc.nextInt();
		
		int [] array = new int [N];
		
		int i;
		
		for (i = 0 ; i < array.length ; i++) {
			array[i] = sc.nextInt();
		}
		
		for (i = array.length-1 ; i > 0 ; i--) {
			if (array[i] < array[i-1]) {
				int tmp = array[i-1];
				array[i-1] = array[i];
				array[i] = tmp;
			}
		}
		System.out.print(array[0] + " ");
		
		
		for (i = 0 ; i < array.length-1 ; i++) {
			if (array[i] > array[i+1]) {
				array[i+1] = array[i];
				}
		}
		System.out.print(array[array.length-1]);
	}
		
}