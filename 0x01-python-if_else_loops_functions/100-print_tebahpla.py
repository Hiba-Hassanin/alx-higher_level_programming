#!/usr/bin/python3
for pha in range(ord('z'), ord('a') - 1, -2):
    print("{:c}{:s}".format(pha, chr(pha - 33)), end="")
