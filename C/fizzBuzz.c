/*
 * fizzBuzz.c by Jigsy (https://github.com/Jigsy1) released under the Unlicense.
 *
 * Compiled on Windows 8.1 using TCC available from: https://bellard.org/tcc/
 *
 * How to:
 * ----------
 * ...> tcc -c fizzBuzz.c
 * ...> tcc -run fizzBuzz.o
 *
 */

#include <stdio.h>

#define buzz "Buzz"
#define fizz "Fizz"
#define fizzBuzz "Fizz Buzz"

int main() {
	int thisLoop;
	for (thisLoop = 1; thisLoop <= 100; thisLoop++) {
		if (thisLoop % 5 == 0 && thisLoop % 3 == 0) {
			printf("%s, ", fizzBuzz);
			continue;
		}
		else if (thisLoop % 5 == 0) {
			printf("%s, ", buzz);
			continue;
		}
		else if (thisLoop % 3 == 0) {
			printf("%s, ", fizz);
			continue;
		}
		else {
			printf("%d, ", thisLoop);
		}
		// The output symmetry is quite interesting.
	}
	return 1;
}

// EOF