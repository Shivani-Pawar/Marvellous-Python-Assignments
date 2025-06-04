import threading


def sumeven(list1):

    sum1=0
    for i in range(0,len(list1)):
        if(list1[i]%2==0):
            
         sum1=sum1+list1[i]
    print(sum1)
       

def sumodd(list2):

    sum2=0
    for i in range(0,len(list2)):
        if(list2[i]%2!=0):
            
         sum2=sum2+list2[i]
    print(sum2)

def main():
    print("Demonstration of serial execution")
    no1=int(input("enter number"))

    print("enter input")
    l=[]
    for i in range(0,no1):
       no=int(input())
       l.append(no)
  

    


    T1 = threading.Thread(target=sumeven,args=(l,))
    T2 = threading.Thread(target=sumodd, args=(l,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()
    print("exit from main")

if __name__ == "__main__":
    main()