def knap01(C):
    for i in range(0, len(w)):
        for c in range(C, w[i]-1, -1):
            f[c]=max(f[c], f[c-w[i]] + v[i])
    return f[-1]
for x in range(int(input())):
    v=[]
    w=[]
    c=[]
    res=0
    for y in range(int(input())):
        a,b=map(int,input().split(" "))
        v.append(a)
        w.append(b)
    for z in range(int(input())):
        c.append(int(input()))
    c.sort()
    f=[0 for i in range(0,c[-1]+1)]
    knap01(c[-1])
    for bag in c:
        res+=f[bag]
    print(res)
    
    
