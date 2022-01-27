package javasec;

public final class p001 {
	public static void main(String[] args) {
		System.out.println(new p001().calculate());
	}
	public int calculate() {
		int total = 0;
		for (int i = 0; i < 1000; i++) {
			if (i % 3 == 0 || i % 5 == 0) {
				total += i;
			}
		}
		return total;
	}
}