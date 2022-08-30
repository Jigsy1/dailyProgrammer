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
 *
 * Note: You will need to do CTRL+C to terminate the program in the Command Prompt.
 *
 */

#include <stdio.h>
#include <winapi/windows.h>

#define SLEEP_TIME 500
// `-> 500 is equal to 0.5s on Windows.

int main(void) {
	int twirlCount = 1;
	for (;;) {
		// `-> Infinite loop.
		switch(twirlCount) {
			case 1:
				printf("\b|");
				twirlCount += 1;
				Sleep(SLEEP_TIME);
			case 2:
				printf("\b/");
				twirlCount += 1;
				Sleep(SLEEP_TIME);
			case 3:
				printf("\b-");
				twirlCount += 1;
				Sleep(SLEEP_TIME);
			case 4:
				printf("\b\\");
				twirlCount = 1;		// -> Reset.
				Sleep(SLEEP_TIME);
		}
	}
	return 0;
}

// EOF
