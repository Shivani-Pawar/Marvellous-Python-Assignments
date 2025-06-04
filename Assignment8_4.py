import threading
def is_digit(s):
    print("Thread ID of digit thread is : ",threading.get_ident())
    dcount=0
    for i in range(len(s)):
        if s[i].isdigit():
            dcount=dcount+1
    print(dcount)

def is_capital(s):
    
    ccount=0
    print("Thread ID of capital thread is : ",threading.get_ident())
    for i in range(len(s)):
        
        if s[i].isdigit()==False and s[i].isupper():
            
            ccount=ccount+1
    print(ccount)


def is_lower(s):
    lcount=0
    print("Thread ID of lower thread is : ",threading.get_ident())
    for i in range(len(s)):
        if s[i].isdigit()==False and s[i].islower():
            lcount=lcount+1
    print(lcount)   


def main():
    print("enter String")
    s1=input()
    
    T1=threading.Thread(target=is_digit,args=(s1,))
    T2=threading.Thread(target=is_capital,args=(s1,))
    T3=threading.Thread(target=is_lower,args=(s1,))
    T1.start()
    T2.start()
    T3.start()
    T1.join()
    T2.join()
    T3.join()


if __name__=="__main__":
    main()