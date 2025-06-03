import threading


def DisplayEven():
    
    for i in range(1,11):
        if(i%2==0):
            
         print(i)
       

def DisplayOdd():
    for i in range(1,11):
      if(i%2!=0):
         print(i)

def main():
    print("Demonstration of serial execution")

    T1 = threading.Thread(target=DisplayEven)
    T2 = threading.Thread(target=DisplayOdd)

    T1.start()
    T2.start()

    T1.join()
    T2.join()
    print("end of main")

if __name__ == "__main__":
    main()