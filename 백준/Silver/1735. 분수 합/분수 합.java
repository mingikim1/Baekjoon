import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner (System.in);
		
		int [] mol_de = new int [4];
		
		for (int i = 0 ; i < 4 ; i++) {
			mol_de[i] = sc.nextInt();
		}
		
		int gcd = 1;
		int mole = mol_de[1]*mol_de[3];
		int denomi = mol_de[0]*mol_de[3] + mol_de[2]*mol_de[1];
		
		
		for (int i = mole ; i >= 1 ; i--) {
			if (mole%(i*1.0)==0.0 && denomi%(i*1.0)==0.0) {
				gcd = i;
				break;
			}
		}
		System.out.println(denomi/gcd + " " + mole/gcd);		
	}		
}