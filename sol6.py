dev1,dev2=map(str,input().split())
if(len(dev1)!=len(dev2)):
     print("no")
else:
     su1=[dev1.count(i) for i in dev1]
     su2=[dev2.count(i) for i in dev2]
if su1==su2:
     print("yes")
else:
     print("no")
