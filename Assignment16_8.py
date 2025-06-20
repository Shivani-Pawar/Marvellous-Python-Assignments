
fobj=open("Data.txt", "r")
content=fobj.read()



cleaned_content = ''.join(content.split())       
fobj=open("Data.txt","w")
fobj.write(cleaned_content)
fobj.close()