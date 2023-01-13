/*
 * brute.c by Jigsy (https://github.com/Jigsy1) released under the Unlicense.
 *
 * Compiled on Windows 8.1 using TCC available from: https://bellard.org/tcc/
 *
 * How to:
 * ----------
 * ...> tcc -c fizzBuzz.c
 * ...> tcc -run fizzBuzz.o
 *
 *
 * Note: 26^4 (or any number higher than four will not work). It'll get to about eomb and just end.
 *	 That said, this is only a demo.
 */

#include <stdio.h>
#include <string.h>

void rotateChar(int stringIndex, int mapIndex, int again);

/* END OF PROTOTYPES */

int breakFlag = 0;
const char CHAR_MAP[] = "abcdefghijklmnopqrstuvwxyz";
char string[] = "aaa";

void rotateChar(int stringIndex, int mapIndex, int again) {
	if (string[stringIndex] == CHAR_MAP[(strlen(CHAR_MAP) - 1)]) {
		mapIndex = 0;
		int newIndex = (stringIndex + 1);
		string[stringIndex] = CHAR_MAP[mapIndex];
		if (newIndex < strlen(string)) {
			char *tempChar;
			int tempIndex;
			tempChar = strchr(CHAR_MAP, string[newIndex]);
			tempIndex = (int) (tempChar - CHAR_MAP);
			rotateChar(newIndex, (tempIndex + 1), 0);
		}
		else {
			breakFlag = 1;
			printf("\nEnd.\n");
		}
	}
	string[stringIndex] = CHAR_MAP[mapIndex];
	if (again > 0) {
		if (breakFlag == 0) {
			printf("%s\n", string);
			rotateChar(stringIndex, (mapIndex + 1), 1);
		}
	}
}

int main(void) {
	rotateChar(0, 0, 1);	// Start from 0, from the 1st character ("a", which is 0 in the array), and rotate again.
	return 0;
}

// EOF
