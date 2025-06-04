import os
import time
import multiprocessing

def factorial(no):
    print("PID is : ",os.getpid())
    fact = 1
    for i in range(1,no):
        fact = fact * i 
    return fact

def main():
    print("enter size")
    no=int(input())
    data=[]
    for i in range(no):
        n=int(input())
        data.append(n)
    

    
    result = []

    p = multiprocessing.Pool()
    result = p.map(factorial,data)

    p.close()
    p.join()
    
    print(result)

    

if __name__ == "__main__":
    main()