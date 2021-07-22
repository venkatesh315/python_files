t=int(input())

for i in range(1,t+1):
    n,k=map(int,input().split())
    elements=list(map(int,input().split()))
    count=0
    copy=k
    j=0
    while(j<n):
        
        if k == elements[j]:
            k-=1
            j+=1
            if(k==0):
                count+=1
                k=copy
                
        elif(j==0 or copy == k):
            j+=1
            
        
        else: 
            k=copy
           
            
    print("Case #{}: {}".format(i,count))
    
