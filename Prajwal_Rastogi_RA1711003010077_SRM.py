s=input()
d=[]
mx=0
for x in s:
    if x in d:
        d=d[d.index(x)+1:]
    else:
        d.append(x)
    if len(d)>mx:
        mx=len(d)
print(mx)
