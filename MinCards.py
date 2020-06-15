# cook your dish here
n=int(input())
s=input()
r=1
b=1
g=1
for i in ('R','B','G'):
    for j in range(len(s)-1):
        if i == 'R':
            if s[j]==s[j+1]=='R':
                r+=1
                
            
        elif i == 'B':
            if s[j]==s[j+1]=='B':
                b+=1
                
        
        else:
            if s[j]==s[j+1]=='G':
                g+=1
              
         
print((r-1)+(b-1)+(g-1))