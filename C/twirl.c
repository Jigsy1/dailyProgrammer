/*
 * twirl.c by Jigsy (https://github.com/Jigsy1) released under the Unlicense.
 *
 * Compiled on Windows 8.1 using TCC available from: https://bellard.org/tcc/
 *
 * How to:
 * ----------
 * ...> tcc -c twirl.c
 * ...> tcc -run twirl.o
 *
 * NOTE: You will need to CTRL+C (^C) to terminate the program.
 */

#include <stdio.h>
#include <winapi/windows.h>

#define sleepTime 500
// 500 = 0.5s on Windows

int main(void) {
	int twirlCount = 1;
	for (;;) {
		// Infinite loop
		switch(twirlCount) {
			case 1:
				printf("\b|");
				twirlCount += 1;
				Sleep(sleepTime);
			case 2:
				printf("\b/");
				twirlCount += 1;
				Sleep(sleepTime);
			case 3:
				printf("\b-");
				twirlCount += 1;
				Sleep(sleepTime);
			case 4:
				printf("\b\\");
				twirlCount = 1;		// Reset
				Sleep(sleepTime);
		}
	}
	return 0;
}

// EOF
