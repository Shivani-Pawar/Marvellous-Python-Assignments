import os
import sys
def FileWrite(filename):


    
    

    print("enter student name")
    lst=[]
    for string in range(1,5):
        name=input()
        lst.append(name)

    fobj=open(filename,"w")
    fobj.write(str(lst))
      

    fobj=open(filename,'r')
    print(fobj.read())
    fobj.close()
        


def main():
    file=sys.argv[1]
    FileWrite(file)

if __name__=="__main__":
    main()