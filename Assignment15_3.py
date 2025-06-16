
import os
import sys
def FileExistance(filename):
    fobj=open(filename,'w')
    nobj=open("Demo.txt",'r')
    content=nobj.read()
    fobj.write(content)


def main():
    file=sys.argv[1]
    FileExistance(file)

if __name__=="__main__":
    main()

