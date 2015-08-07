subs = int(raw_input("Enter No. of Subjects: "));
marksList = []

for i in range(0,int(subs)):
    sub = raw_input("Enter Subject Name: ");
    marks = int(raw_input("Enter Marks: "));
    marksList.append({sub:marks})

print marksList

print "-----------------------"

for j in range(0,len(marksList)):
    for key,value in marksList[j].items():
        print key+":"+str(value)
    
