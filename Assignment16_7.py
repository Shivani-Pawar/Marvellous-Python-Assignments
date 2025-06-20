fobj=open("marks.txt", "w")
fobj.write("Shivani 85\n")
fobj.write("Sangram 92\n")
fobj.write("Rahul 78\n")
fobj.write("Shivendra 95\n")
fobj.write("San 88\n")

MaXMarks = 0
top_student=""
fobj=open("marks.txt", "r")

for line in fobj:
   
    name,marks= line.strip().split()
    #print(name)
    marks=int(marks)
        
       
       
    
    if marks > MaXMarks:
            MaXMarks = marks
            top_student = name

print(f"The student with the highest mark is {top_student} with {MaXMarks} marks.")
