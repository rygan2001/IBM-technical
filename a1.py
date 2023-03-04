s=input ()
slist1=list(s)
slist2=[]
slist3=[]
i=len(slist1)
while i>0:
    slist3.append(slist1[i-1])
    i=i-1
for i in slist3:
    if (i=="A"):
        slist2.append("T")
    if (i=="T"):
        slist2.append("A")
    if (i=="C"):
        slist2.append("G")
    if (i=="G"):
        slist2.append("C")
print("".join(slist2))
