package javasec;

public class p003 {
	public long smallestFactor(long x) {
		for (int i = 2; i <= Math.floor(Math.pow(x, 0.5f)); i++) {
			if (x % i == 0) {
				return i;
			}
		}
		return x;  
	}
	public long run() {
		long x = 600851475143L;
		while (true) {
			long y = smallestFactor(x);
			if (y < x)
				x /= y;
			else
				return x;
		}
	}
	public static void main(String[] args) {
		System.out.println(new p003().run());
	}
}
