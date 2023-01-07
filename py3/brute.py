# brute.py by Jigsy (https://github.com/Jigsy1) released under the Unlicense.
#
# Just a demo of looping through letter(s). aaaa->zzzz


# import sys
import time


# define

# CHAR_MAP = "abcdefghijklmnopqrstuvwxyz"
CHAR_MAP = "abcd"
# STR_LEN = 2
STR_LEN = len(CHAR_MAP)


# Core

# sys.setrecursionlimit(20000)
# `-> I would avoid increasing this beyond 20,000. And 4^4 is about 256, so that should be enough for this demo.

string = list(CHAR_MAP[0] * STR_LEN)

def rotateChar(stringIndex, mapIndex, again):
        if string[stringIndex] == CHAR_MAP[(len(CHAR_MAP) - 1)]:
                mapIndex = 0
                tempIndex = CHAR_MAP.rfind(string[(stringIndex + 1)])
                string[stringIndex] = CHAR_MAP[mapIndex]
                rotateChar((stringIndex + 1), (tempIndex + 1), 0)
        string[stringIndex] = CHAR_MAP[mapIndex]
        if again > 0:
                print(string)
                rotateChar(stringIndex, (mapIndex + 1), 1)
        # `-> This will keep going until it IndexErrors. I couldn't find a way to "break" in an except, so whatever.
        #       "return," "raise" and "pass" didn't help either.

def main():
        rotateChar(0, 0, 1)

if __name__ == "__main__":
	main()


# EOF
