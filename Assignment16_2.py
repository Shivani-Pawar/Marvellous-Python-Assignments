import os
import sys
def FileWrite(filename):


    


    fobj=open(filename,"w")
    fobj.write("I LOVE INDIA")
      

    fobj=open(filename,'r')
    print(fobj.read())
    fobj.close()
        


def main():
    file=sys.argv[1]
    FileWrite(file)

if __name__=="__main__":
    main()