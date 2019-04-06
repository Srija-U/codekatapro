n=int(input())
l=[]
for i in range(0,n):
    l.append(str(input()))

a=[]

l.sort(key=len)
print(l)
ma=len(l[0])

res=[]

for i in range(0,ma):
    te=l[0][i]
    c=0
    for j in range(1,n):
        if(l[j][i]==te):
            c+=1
        else:
            break
    if(c>=1):
        res.append(te)
    if(c==0):
        break
if(len(res)==0):
    exit()
print(*res,sep='')
