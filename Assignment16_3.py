import os
import sys
def FileWrite(filename):
    fobj=open(filename,'r')

    #print(len(fobj.read()))
    linecount=fobj.readlines()
    
    charcount=0
    wordcount=0






    for i in linecount:
        for j in i:
            if(j != " "):
              charcount=charcount+1
          
    
   


    fobj=open(filename,"r")
    content=fobj.read()
    print("Line count",(len(linecount)))
    print("letter count",charcount)
    print("word count of file",len(content.split()))

    fobj.close()
        


def main():
    file=sys.argv[1]
    FileWrite(file)

if __name__=="__main__":
    main()