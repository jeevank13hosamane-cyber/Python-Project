class HashTable():
    def __init__(self):
        self.collection=dict()
    def hash(self,string):
        sum=0
        for i in string:
            sum+=ord(i)
        return sum    
    def add(self,key,value):
        x=self.hash(key)
        if x not in self.collection:
            self.collection[x]={}
        self.collection[x][key]=value
    def remove(self,key):
        x=self.hash(key)
        if x in self.collection:
            if key in self.collection[x]:
                del self.collection[x][key]

    def lookup(self,key):
        hash_val=self.hash(key)  
        if hash_val in self.collection:
            if key in self.collection[hash_val]:
                return self.collection[hash_val][key]
         

ht=HashTable()                       
print(ht.hash('fcc'))       

print(ht.add('fcc', 'hi'))
print(ht.lookup('golf'))
