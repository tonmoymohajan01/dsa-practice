class deque:
    
    def __init__(self):
        self.l = []
    
    def isEmpty(self):
        return len(self.l) == 0 
    
    def insert_end(self,vlaue):
        self.l.append(vlaue)

    def delation_front(self):
        if len(self.l) == 0  :
            print("Queue is emptuy")
        else:
            return self.l.pop(0)
        
    def insert_beg(self,data):
        self.l.insert(0,data)

    def deletion_end(self):
        if len(self.l) == 0  :
            print("Queue is emptuy")
        else: 
            return self.l.pop()


dq = deque()
dq.insert_end(10)
dq.insert_beg(20)
dq.insert_end(30)
dq.insert_beg(40)
print(dq.deletion_end())
print(dq.deletion_end())
print(dq.delation_front())