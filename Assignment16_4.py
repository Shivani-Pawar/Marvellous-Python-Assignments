import os
import sys

def WriteNumber(Filename):
    fobj=open(Filename,"w")
    for i in range(1,11):
        fobj.write("\n")
        fobj.write(str(i))

    fobj=open(Filename,"r")
    print(fobj.read())


def main():
    file=sys.argv[1]
    WriteNumber(file)

if __name__=="__main__":
    main()