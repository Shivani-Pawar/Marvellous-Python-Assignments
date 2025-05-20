


def CheckVowel(character):
    if(character=='a'or character=='e'or character=='i'or character=='o'or character=='u'or character=='A' or character=='E' or character=='I'or character=='O' or character=='U' ):
        print("the alphabet is Vowel")
    else:
        print("The alphabet is consonent")

    

def main():

    print("enter alphabet")
    alpha=input()
    CheckVowel(alpha)
    

if __name__=="__main__":
    main()