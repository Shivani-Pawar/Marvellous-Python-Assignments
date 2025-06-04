import threading


def sumeven(value1):
    sum1=0
    for i in range(1,value1):
        if(i%2==0) and (value1%i==0):
            
         sum1=sum1+i
    return sum1
       

def sumodd(value2):
    sum2=0
    for i in range(1,value2):
      if(i%2!=0) and (value2%i==0):
         sum2=sum2+i
    return sum2

def main():     
    print("Demonstration of serial execution")
    no1=int(input("enter number"))

    T1 = threading.Thread(target=sumeven,args=(no1,))
    T2 = threading.Thread(target=sumodd, args=(no1,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()
    print("exit from main")

if __name__ == "__main__":
   main()