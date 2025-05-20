


def main():
    print("Enter size")
    no=int(input())
    print("enter numbers")
    l=[]
    for i in range(no):
        numbers=int(input())
        l.append(numbers)
    print(l)
    print(l[0])

   
    
    max=l[0]


    for i in l:
        if i > max:
            max=i

    print(max)



    




if __name__=="__main__":
    main()