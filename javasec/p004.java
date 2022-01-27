package javasec;

import java.util.Collections;
import java.util.ArrayList;
import java.lang.String;

public final class p004 {
	static String reverse(String str) {
		return new StringBuilder(str).reverse().toString();
	}
	public Boolean isPalendromic(Integer n) {
		return n.toString().equals(reverse(n.toString()));
	}
	public Integer compute() {
		ArrayList<Integer> palendromes = new ArrayList<Integer>();
		for (Integer i = 100; i < 1000; i++) {
			for (Integer j = 100; j < 1000; j++) {
				Integer k = i * j;
				if (isPalendromic(k)) {
					palendromes.add(k);
				}
				
			}
			
		}
		return Collections.max(palendromes);
	}
	public static void main(String[] args) {
		System.out.println(new p004().compute());
	}
}
