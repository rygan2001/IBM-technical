def small(a,b):
    if (a[len(a)-1]=="S"):
        if (b[len(b)-1]!="S"):
            return True
        elif (len(a)>=len(b)):
              return True
        else:
            return False
    elif (a=="M"):
        if (b[len(b)-1]=="S"):
            return False
        else:
            return True
    elif (a=="L"):
        if (b[len(b)-1]=="S"):
            return False
        elif (b=="M"):
            return False
        else:
            return True
    elif (a[len(a)-1]=="L"):
        if (b[len(b)-1]!="L"):
            return False
        elif (len(a)>=len(b)):
              return False
        else:
            return True

def order(s):
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if (small(s[i],s[j])==True):
                s[i],s[j]=s[j],s[i]
    return s

text=[]
for i in range(4):
    if (i ==0 ):
        l = int(input())
    elif (i==1):
        l = list(input().split())
    elif (i==2):
        l = int(input())
    elif (i==3):
        l = list(input().split())
    text.append(l)

m=order(text[1])
n=order(text[3])
print(m,n)

judge=0;
for i in range(len(text[3])):
    if (small(n[i],m[i])==False):
        judge=1
        print(n[i])
if (judge==0):
    print("Yes")
else:
    print("No")
