class Hashing:
    def __init__(self,key):
        self.hash_value=key%43


    def Insert(self,values):
        fobj=open("patient_details.txt","a")
        pos=500*self.hash_value
        print("inserting at ",self.hash_value)
        fobj.seek(pos)
        print("Current position is ",fobj.tell())

        for ele in values:
            fobj.write(ele)
        fobj.write("\n")
        fobj.write("Hi")






print("enter your choice:- 1:insert 2:search 3:delete ")
choice=int(input())
rrn=0

if choice == 1:
    data = int(input("enter the number of records you want to insert: "))
    for repeat in range(data):
        name = input("enter name: ")
        age = int(input("enter age: "))
        mobile = int(input("enter the mobile number: "))
        vax_name = input("enter vaccine name: ")
        dose1 = input("enter dose1 vaccinated date: ")
        dose2 = input("enter dose2 vaccinated date: ")
        status = input("enter the vaccine status: ")


    details=[rrn,name,age,mobile,vax_name,dose1,dose2,status]
    val=[]
    for item in details:
        item=str(item)+'|'
        val.append(item)

    rrn+=1

    rec=Hashing(mobile)
    rec.Insert(val)




