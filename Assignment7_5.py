
def main():
    print("enter string")
    word=input()
    print(word[0])
    print("length",len(word))
   
    
    rev=[]
    for i in range(len(word)-1,-1,-1):


        print(i)

        rev.append(word[i])
    print(rev)
    st=[]

    for i in range(0,len(word),1):
        st.append(word[i])
    print(st)











    if rev == st:
        print("pallindrome")
    else:
        print("not pallindrome")


if __name__=="__main__":
    main()