package javasec;

public class p005 {
	public int gcd(int a, int b) {
		while (b != 0) {
			int c = a % b;
			a = b;
			b = c;
		}
		return a;
	}
	public int lcm(int a, int b) {
		return a / gcd(a, b) * b;
	}

	public int run() {
		int count = 1;
		for (int i = 1; i < 21; i++) {
			count *= (int)Math.floor(i / gcd(i, count));
		}
		return count;
	}
	public static void main(String[] args) {
		System.out.println(new p005().run());
	}
}
