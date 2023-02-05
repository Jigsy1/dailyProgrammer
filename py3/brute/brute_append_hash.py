# brute.py (Rev.2) - APPEND VERSION - by Jigsy (https://github.com/Jigsy1) released under the Unlicense.
#
# Just a demo of looping through letter(s). A->B->C->...->AA->BA->CA->...->...->XZZZ->YZZZ->ZZZZ->...
# ...and cracking a hash.

import hashlib
import time

def rotate(index):
    """Rotate characters by one."""
    char = CHAR_MAP.rfind(STRING[index])
    STRING[index] = CHAR_MAP[(char + 1) % len(CHAR_MAP)]
    if CHAR_MAP[char] == CHAR_MAP[-1]:
        STRING[index] = CHAR_MAP[0]
        if (index + 1) == len(STRING):
            STRING.append(CHAR_MAP[0])
            return
        rotate((index + 1))

# CHAR_MAP = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
# END_STRING = list(CHAR_MAP[-1] * len(CHAR_MAP))
# >-> If you want the insanely long version, comment out CHAR_MAP and END_STRING below and uncomment the two above.
CHAR_MAP = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
STRING = list(CHAR_MAP[0] * 1)
END_STRING = list(CHAR_MAP[-1] * 3)

THIS_HASH = "a61a40943e07257e084ea3f62dfdb1c8"

def main():
    index = 0
    thisChar = 0
    while 1:
        print("".join(STRING))
        encodedString = "".join(STRING).encode("UTF-8")
        # `-> String needs to be encoded to use hashlib.
        hashOutput = hashlib.md5(encodedString).hexdigest()
        # `-> If you change the hash to sha1, sha256, etc, just remember to change this from md5.
        if hashOutput == THIS_HASH:
            print("Match: {} -> {}".format("".join(STRING), hashOutput))
            break
        if "".join(STRING) == "".join(END_STRING):
            break
        if STRING[index] == CHAR_MAP[-1]:
            if (index + 1) == len(STRING):
                STRING.append(CHAR_MAP[0])
            else:
                rotate((index + 1))
        thisChar += 1
        STRING[index] = CHAR_MAP[thisChar % len(CHAR_MAP)]
        # time.sleep(1)
    print("End")

if __name__ == "__main__":
    main()

# EOF
