n=int(input())
l=[]
for i in range(0,n):
    t=str(input())
    l.append(t)
le=len(l)
a=[]
for i in range(0,le):
    a.append(len(l[i]))
ma=max(a)
for i in range(0,ma):
    te=l[0][i]
    try:
        for j in range(1,le):
            if(l[j][i]==te):
                te=te
            else:
                exit()
    except:
        no=i
        print(l[0][:no])
        exit()
