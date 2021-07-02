

class HashTable:
    def __init__(self):
        self.MAX = 23
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        hash=key%23
        print("Hash value is: ",hash)
        return hash

    def __getitem__(self, key):
        arr_index = self.get_hash(key)
        for kv in self.arr[arr_index]:
            if kv[0] == key:
                return kv[1]

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) > 0 and element[0] == key:
                print("Collision occured and solved by chaining")
                self.arr[h][idx] = (key, val)
                found = True
        if not found:
            self.arr[h].append((key, val))

    def __delitem__(self, key):
        arr_index = self.get_hash(key)
        for index, kv in enumerate(self.arr[arr_index]):
            if kv[0] == key:
                print("del", index)
                del self.arr[arr_index][index]

t = HashTable()

choice=int(input("enter your choice:- 1:insert 2:search 3:delete "))

if choice == 1:
    rec=int(input("enter the number of records you want to insert: "))
    for repeat in range(rec):
        name=input("enter name: ")
        age=int(input("enter age: "))
        mobile=int(input("enter the mobile number: "))
        vax_name=input("enter vaccine name: ")
        dose1=input("enter dose1 vaccinated date: ")
        dose2=input("enter dose2 vaccinated date: ")
        status=input("enter the vaccine status: ")

        values=[name,age,mobile,vax_name,dose1,dose2,status]

        t[mobile]=values

        print(t.arr)

































