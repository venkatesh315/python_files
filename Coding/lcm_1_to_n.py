# LCM OF 1ST N Numbers
class Solution:
    def getSmallestDivNum(self, n): 
        # code here 
        self.num=n
        self.j=2
        self.ans=self.num*self.j
        self.count=0
        self.i=1
        while(self.i<=self.num):
            if self.ans % self.i == 0:
                if self.count == self.num:
                    break
                else:
                    self.count+=1
                    self.i+=1
                    continue
                
            else:
                self.i=1
                self.count=0
                self.j+=1
                self.ans=self.num*self.j
        return self.ans   

ele=int(input("enter a number: "))
obj=Solution()
res=obj.getSmallestDivNum(ele)
print("Result is ",res)

            
