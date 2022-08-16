/*	lettersum.c

	For: https://old.reddit.com/r/dailyprogrammer/comments/onfehl/20210719_challenge_399_easy_letter_value_sum/

	Compiled under TCC.
*/

#include <ctype.h>
#include <stdio.h>
#include <string.h>

int getAlphaNumber(char thisLetter) {
	if (!isalpha(thisLetter)) {
		return 0;
	}
	char alphabet[] = "abcdefghijklmnopqrstuvwxyz";
	if (isupper(thisLetter)) {
		thisLetter = tolower(thisLetter);
	}
	int thisLoop = 0, thisPos = 0;
	for (thisLoop = 0; thisLoop <= strlen(alphabet); thisLoop++) {
		if (thisLetter == alphabet[thisLoop]) {
			thisPos = (thisLoop + 1);
			break;
		}
	}
	return thisPos;
}
int lettersum(char *thisString) {
	int thisLoop = 0, thisSum = 0;
	for (thisLoop = 0; thisLoop <= strlen(thisString); thisLoop++) {
		thisSum += getAlphaNumber(thisString[thisLoop]);
	}
	return thisSum;
}

int main() {
	char string1[] = "";
	printf("%s = %d\n", string1, lettersum(string1));
	char string2[] = "a";
	printf("%s = %d\n", string2, lettersum(string2));
	char string3[] = "z";
	printf("%s = %d\n", string3, lettersum(string3));
	char string4[] = "cab";
	printf("%s = %d\n", string4, lettersum(string4));
	char string5[] = "excellent";
	printf("%s = %d\n", string5, lettersum(string5));
	char string6[] = "microspectrophotometries";
	printf("%s = %d\n", string6, lettersum(string6));
	// Own entries below:
	char string7[] = "antidisestablishmentarianism";
	printf("%s = %d\n", string7, lettersum(string7));
	char string8[] = "pneumonoultramicroscopicsilicovolcanoconiosis";
	printf("%s = %d\n", string8, lettersum(string8));
	char string9[] = "floccinaucinihilipilification";
	printf("%s = %d\n", string9, lettersum(string9));
}

// EOF
