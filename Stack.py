class stack :
    def __init__(self):
        self.l = []
    
    def push(self,value):
        self.l.insert(0,value)

    def length(self):
        return len(self.l)
    
    def peak(self):
        if len(self.l) == 0 :
            raise Exception("stack is empty")
        else:
            return self.l[0]
    
    def pop(self):
        if len(self.l) == 0 :
            raise Exception("stack is empty")
        else:
            return self.l.pop(0)
s = stack()
s.push(10)
s.push(20)
s.push(30)
s.pop()
s.pop()
s.pop()
s.pop()
print(s.length())