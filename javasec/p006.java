package javasec;

public class p006 {
	public double run() {
		int total = 0;
		int total2 = 0;
		for (int i = 1; i <= 100; i++) {
			total += Math.pow(i, 2);
			total2 += i;
		};
		return (Math.pow(total2, 2) - total);
	}
	public static void main(String[] args) {
		System.out.println(new p006().run());
	}
}