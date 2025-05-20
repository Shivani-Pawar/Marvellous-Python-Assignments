



def Tempconverter(cel):
    far=(cel*9/5)+32
    return far

def main():
    print("Enter tempreature in celcius")
    c=int(input())
    
    f=Tempconverter(c)
    print("the fahrenheit temp is",f)

if __name__=="__main__":
    main()