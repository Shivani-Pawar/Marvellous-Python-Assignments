import os
import sys



def CountWriteNumber(Filename):
    count=0
    fobj=open(Filename,"r")
    for line in fobj:
       
        wordinline=[]
        for word in line.split():
            wordinline.append(word)
            if len(wordinline) == 5:
                print(line)
            
       
            
    #print(count)



  



  
    


def main():
    file=sys.argv[1]
    CountWriteNumber(file)

if __name__=="__main__":
    main()