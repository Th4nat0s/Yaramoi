#!/usr/bin/env python3
# coding=utf-8
import sys
import base64


# Functions
def getparam(count):
    if len(sys.argv) != count + 1:
        print('Decode autolog strings')
        print('To Use: %s .509 file' % sys.argv[0])
        sys.exit(1)
    else:
        return sys.argv[1]


def swap(ins):
    ins = list(ins)
    for c in range(0, len(ins), 2):
        tmp = ins[c]
        ins[c] = ins[c + 1]
        ins[c + 1] = tmp
    return "".join(ins)


# Main Code #####
def main():
    param = getparam(1)

    arr = open(param, 'rb').readlines()
    for line in arr:
        line = line.decode('ascii', 'ignore').strip()
        try:
            # If the decode or the b64 faild... probably a straight line
            linec = swap(line)
            linec = base64.b64decode(linec)
            line = linec.decode('utf-8')
        except:
            pass
        finally:
            print (line)

if __name__ == '__main__':
    main()
