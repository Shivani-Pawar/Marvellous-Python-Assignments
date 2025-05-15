def CheckPrime(value):
    count=0

    for i in range(2,value,1):
        
        if (value%i) == 0:
            count=count +1
    return count   

    
    




