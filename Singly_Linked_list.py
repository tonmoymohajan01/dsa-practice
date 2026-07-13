class Node:
    def __init__(self,info,next = None):
        self.data = info 
        self.next = next 

class singlyLinked_list:
    def __init__(self,head = None):
        self.head = head 

    def Insert_End(self,value):
        temp = Node(value)
        if (self.head != None):
            t1 = self.head
            while (t1.next != None):
                t1 = t1.next 
            t1.next = temp
        else:
            self.head = temp 
    
    def Insert_Beg(self,value):
        temp = Node(value)
        temp.next = self.head 
        self.head = temp 
    
    def Insert_Mid(self,value,loc):
        temp = Node(value)
        t1 = self.head
        while (t1.next != None):
            if (t1.data == loc):
                temp.next = t1.next 
                t1.next = temp
                break
            t1 = t1.next

    def deletell(self,value):
        t1 = self.head 
        previous = t1 
        if (t1.data == value):
            self.head = t1.next 
            return 
        while (t1.next != None):
            if (t1.data == value):
                previous.next  = t1.next 
                return 
            else:
                previous = t1 
                t1 = t1.next
        if (t1.data == value) :
            previous.next = None

    def print_LL(self):
        t1 = self.head
        while (t1.next != None):
            print(t1.data, end = " <--> ")
            t1 = t1.next
        print(t1.data)

obj = singlyLinked_list()
obj.Insert_End(10)
obj.Insert_End(20)
obj.Insert_Beg(5)
obj.Insert_Mid(15,10)
obj.deletell(15)
obj.print_LL()
    