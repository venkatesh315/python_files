
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class CircularSLL:
    def __init__(self):
        self.head=None
        self.tail=None
        
        
    def append(self,node):
        
        if self.head == None:
            self.head=node
            self.tail=node
            self.tail.next=self.head
        else:
            
            self.tail.next=node
            self.tail=node
            self.tail.next=self.head
            
    def display(self):
        
        count=0
        temp=self.head
        
        if temp.next == self.head:
              print(temp.data,end=" ")
              return
            
        while(count != num):
            print(temp.data,end=" ")
            count+=1
            temp=temp.next
        print("\n")
        return
    
    
    def joseph(self,num,m):
        
        k=num
        first=obj_l.head
        while(k != 1):
            for i in range(m-1):
                prev=first
                first=first.next
            temp=first.next
            prev.next=temp
            k-=1
            first=prev
        return first.data    

            
            
                
        
        
    
    


if __name__ == '__main__':
    
    num=int(input())
    node_val=list(map(int,input().strip().split()))
    obj_l=CircularSLL()
    for j in node_val:
        obj_n=Node(j)
        obj_l.append(obj_n)
    m=int(input())
    print(obj_l.joseph(num,m))
    
