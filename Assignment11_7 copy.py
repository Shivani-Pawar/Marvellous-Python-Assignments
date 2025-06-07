
i = 1

def PrintStar(no):


    global i
    print("\n")
    
    if (i <= no):
        for j in range(i):

            print("*",end=" ")
   
        i = i + 1
        
        PrintStar(no)


    
 

def main():
    print("enter number")
    no = int(input())
    
    PrintStar(no)



if __name__ == "__main__":
    main()

