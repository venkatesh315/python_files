n,a=map(int,input().split())
temp=str(n)
numb=[]
for i in temp:
    numb.append(i)
total=len(numb)
while(a>=1):
    x=numb[total-1]
    x=int(x)
    if x == 0:
        del(numb[total-1])
        a-=1
        total-=1
     
        
    else:
        numb[total-1]=int(numb[total-1])-1
        numb[total-1]=str(numb[total-1])
        
        a-=1
      
temp=""
for i in numb:
    temp=temp+i

n=int(temp)

print(n)