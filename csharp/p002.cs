using System;
	
namespace csharp {
	class p002 {
		public int run() {
			int total = 0;
			int a = 1;
			int b = 2;
			while (a <= 4000000) {
				if (a % 2 == 0) {
					total += a;
				};
				int c = a + b;
				a = b;
				b = c;
			};
			return total;
		}
		static void Main(string[] args) {
			Console.WriteLine(new p002().run());	
		}
	}
}