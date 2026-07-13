class queue:
    def __init__(self):
        self.l = []
    
    def isEmpty(self):
        return len(self.l) == 0 
    
    def push(self,vlaue):
        self.l.append(vlaue)

    def pop(self):
        if len(self.l) == 0  :
            print("Queue is emptuy")
        else:
            return self.l.pop(0)

q = queue()
q.isEmpty()