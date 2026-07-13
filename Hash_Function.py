class HashTable:
    def __init__(self):
        self.Max = 100
        self.arr = [None for i in range(self.Max)]
    
    def get_hash(self,key):
        h = 0 
        for char in key:
            h += ord(char)
        return h % self.Max
    
    def __setitem__(self,key,val):
        h = self.get_hash(key)
        self.arr[h] = val
    
    def __getitem__(self,key):
        h = self.get_hash(key)
        return self.arr[h]
    
    def __delitem__(self,key):
        h = self.get_hash(key)
        self.arr[h] = None

t = HashTable()
t['march 6'] = 130 
t['march 5'] = 50
t['jun 5'] = 60 
del t['march 6']
print(t.arr)