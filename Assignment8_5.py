import threading
def Display():
 
    for i in range(51):
        print(i)

def Displayrev():
    
    for i in range(51,0,-1):
        print(i)
    
    



def main():
    
    
    
    T1=threading.Thread(target=Display)
    T2=threading.Thread(target=Displayrev)
   
    T1.start()
    T1.join()
    T2.start()
    T2.join()
    


if __name__=="__main__":
    main()