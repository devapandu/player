dj=input()
dj=list(dj)
res=""
for i in range(0,len(dj)-1,2):
    temp=dj[i+1]
    dj[i+1]=dj[i]
    dj[i]=temp
print(res.join(dj))
