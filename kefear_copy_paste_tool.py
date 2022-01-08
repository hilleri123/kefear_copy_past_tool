#!/usr/bin/python3

import re
import pyperclip as pc
import sys

def main():
    file_name = 'patterns.txt' if len(sys.argv) < 2 else argv[-1]
    #pc.copy('a   wah')
    text_in = pc.paste()
    print(text_in)
    print('='*50)
    text_out = text_in
    with open(file_name, 'r') as f:
        for idx, line in enumerate(f):
            #print(idx, bool(idx & 1))
            if bool(idx & 1):
                replacement = line[:-1]
            else:
                pattern = line[:-1]
                replacement = None
            #pattern = r'(a)\s*([\w]*)'
            #replacement = r'!\2! !\1!'
            #print(replacement, pattern)
            if replacement and pattern:
                text_out = re.sub(pattern, replacement, text_in)
    print(text_out)
    pc.copy(text_out)



if __name__ == "__main__":
    main()

