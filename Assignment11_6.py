no2=1

def Display(value):
   
    global no2
    print("\n")
    if(no2<=value):
        for i in range(no2):
            print("*",end=" ")
        no2=no2+1
       
        Display(value)
    





def main():
    Display(4)
    


if __name__=="__main__":
    main()