#code
t=int(input("enter number of cases: "))
for c in range(t):
    arr=[]
    unit=0
    n=int(input("enter number of elements: "))
    arr=list(map(int,input().split()))
    
    for i in range(1,n-1):
        
            left_arr=arr[0:i]
            left_max=max(left_arr)
            right_arr=arr[i+1:]
            right_max=max(right_arr)
            diff=min(left_max,right_max)
            val=diff-arr[i]
            if val >0:
            
                unit+=val
                
            else:
                pass
            
    print(unit)
