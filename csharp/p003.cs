using System;
	
namespace csharp {

	class p003 {
		long smallestFactor(long x) {
			for (int i = 2; i <= Math.Floor(Math.Pow(x, 0.5)); i++) {
				if (x % i == 0) {
					return i;
				};
			};
			return x;  
		}
		public long run() {
			long x = 600851475143;
			while (true) {
				long y = smallestFactor(x);
				if (y < x) {
					x /= y;
				} else {
					return x;
				}
			}
		}
		static void Main(string[] args) {
			Console.WriteLine(new p003().run());	
		}
	}
}