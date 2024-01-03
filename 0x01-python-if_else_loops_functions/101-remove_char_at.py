#!/usr/bin/python3
def remove_char_at(str, n):
    removed = ''
    be = 0
    for c in str:
        if be != n:
            removed += str[be]
        be += 1
    return removed