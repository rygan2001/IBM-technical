
f=open('input')
line=int(f.readline())
for i in range(line):
    lines=f.readlines(line)
f.close()

allValid= True
errorCodes=[]

for j in lines:
    l=list(j.split())
    if (l[1]=="false"):
        allValid=False
        errorCodes.append(l[2])
if (allValid==True):
    print("Yes")
else:
    print("No")
    print(" ".join(errorCodes))
