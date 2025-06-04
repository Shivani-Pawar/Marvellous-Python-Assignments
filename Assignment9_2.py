import multiprocessing

import os

def Square(num):
    for i in range(len(num)):
        s=num[i]**2
        print(s)


def main():
   
    print("enter size of list")
    no=int(input())
    lst=[]
    for i in range(no):
        n=int(input())
        lst.append(n)


    T1 = multiprocessing.Process(target=Square, args=(lst,))
    T2 = multiprocessing.Process(target=Square, args=(lst,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

   

   
    print("end of main")

if __name__ == "__main__":
    main()