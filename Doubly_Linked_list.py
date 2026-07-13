class Node:
    def __init__(self,value = None):
        self.data = value
        self.previous = None
        self.next = None
class DoublyLinked_list:
    def __init__(self):
        self.head = None
    
    def Insert_End(self,value):
        temp = Node(value)
        if (self.head == None):
            self.head = temp
            return  
        else:
            t1 = self.head 
            while (t1.next != None):
                t1 = t1.next 
            t1.next = temp 
            temp.previous = t1
    
    def Insert_Beg(self,value):
        temp = Node(value)
        if (self.head == None):
            self.head = temp 
            return 
        else:
            temp.next = self.head 
            self.head.previous = temp 
            self.head = temp 
    
    def Insert_Mid(self,value,loc):
        t1 = self.head
        while(t1.next != None):
            if(t1.data == loc):
                break 
            else:
                t1 = t1.next 
        temp = Node(value)
        temp.next = t1.next 
        t1.next.previous = temp 
        t1.next = temp 
        temp.previous = t1

    def deletell(self,value):
        temp = Node(value)
        if (self.head == None):
            print("Linked list is empty")
            return 
        
        t1 = self.head
        if (t1.data == value):
            self.head = t1.next
            self.head.previous = None
            return 
        while (t1.next != None):
            if (t1.data == value):
                t1.previous.next = t1.next 
                t1.next.previous = t1.previous
                return 
            else:
                t1 = t1.next
        if (t1.data == value):
            t1.previous.next = None


        


    def printll(self):
        t1 = self.head 
        while(t1.next != None):
            print(t1.data,end = " <--> ")
            t1 = t1.next 
        print(t1.data)

obj = DoublyLinked_list()
obj.Insert_End(10)
obj.Insert_End(20)
obj.Insert_End(30)
obj.Insert_Beg(8)   
obj.Insert_Mid(50,20)   
obj.deletell(30)
obj.printll()

        