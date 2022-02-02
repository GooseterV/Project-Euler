using System;

	
namespace csharp {
	class p004 {
		public bool isPalendromic(int n) {
			string s = n.ToString();
			char[] arr = s.ToCharArray();
			Array.Reverse(arr);
			if ( new string(arr) == s) {
				return true;
			} else {
				return false;
			}
		}
		public int run() {
			LinkedList<int> palendromes = new LinkedList<int>();
			for (int i = 100; i < 1000; i++) {
				for (int j = 100; j < 1000; j++) {
					int prod = i * j;
					if (isPalendromic(prod)) {
						palendromes.AddLast(prod);
					}
				}
			}
			return palendromes.Max();
		}
		static void Main(string[] args) {
			Console.WriteLine(new p004().run());	
		}
	}
}