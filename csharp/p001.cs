using System;
	
namespace csharp {
	class p001 {
		public int run() {
			int total = 0;
			for (int i = 0; i < 1000; i++) {
				if (i % 5 == 0 || i % 3 == 0) {
					total += i;
				}
			}
			return total;
		}
		static void Main(string[] args) {
			Console.WriteLine(new p001().run());	
		}
	}
}