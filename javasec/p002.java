package javasec;

public final class p002 {
	public static void main(String[] args) {
		System.out.println(new p002().calculate());
	}
	public int calculate() {
		int total = 0;
		int a = 1;
		int b = 2;
		while (a <= 4000000) {
			if (a % 2 == 0) {
				total += a;
			}
			int c = a + b;
			a = b;
			b = c;
		}
		return total;
		
	}
}


