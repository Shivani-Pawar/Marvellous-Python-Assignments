import os
import sys


def CopyFile(filename1,filename2):
    fobj1=open(filename1,"w")
    fobj1.write("Shivani")

    fobj1=open(filename1,"r")
    content=fobj1.read()

    fobj2=open(filename2,"w")

    fobj2.write(content)
    fobj1.close()
    fobj2.close()








def main():
    file1=sys.argv[1]
    file2=sys.argv[2]
    CopyFile(file1,file2)





if __name__=="__main__":
    main()