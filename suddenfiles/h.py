u = list(input().split(" "))
n = int(u[0])
k = int(u[1])

l = []

for i in range(n):
    m = list(input().split(" "))
    m = [word.lower() for word in m]
    l.append(m)

r = []
A=input()
for y in range(k):
    q = list(input().split(" "))
    a = q[-1].lower()#g
    r.append(a)
S=[]
for s in  range(0,k,2):
    LL=[]
    LL.append(r[s])
    LL.append(r[s+1])
    S.append(LL)
print(r)
print(S)
print(l)
kk=[]
for o in S:
    pp=[]
    for z in o: 
        flag = 0
        for j in range(len(l)):
            if z in l[j]:
                flag = 1
                # print(chr(65+j))
                pp.append(chr(65+j))
                # print(chr(65 + j), end="")
                break
        if flag == 0:
            kk.append('X')
            kk.append('X')
            # print('X', end="")
            # print('X', end="")
            break
    if len(pp)!=0:
        kk.append(pp[0])
        kk.append(pp[1])
        # print(pp[0], end="")
        # print(pp[1], end="")
s=''
for i in range(len(kk)):
    s=s+kk[i]
print(s)
