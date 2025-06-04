import os
import time
import multiprocessing
import threading

def Sumnormal():
    sum=0
    for i in range(1,10000000):
        sum=sum+i
    print(sum)

def main():
    start_time1=time.time()
    Sumnormal()
    end_time1=time.time()

    normal_time=end_time1-start_time1


    T1=threading.Thread(target=Sumnormal)

    start_time2=time.time()
    T1.start()
    T1.join()
    end_time2=time.time()

    thread_diff=end_time2-start_time2


    P1 = multiprocessing.Process(target=Sumnormal)

    start_time3=time.time()
    P1.start()
    P1.join()
    end_time3=time.time()

    processdiff=end_time3-start_time3


    print(normal_time)
    print(thread_diff)
    print(processdiff)


if __name__ == "__main__":
    main()