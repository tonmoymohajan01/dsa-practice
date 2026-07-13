#Preorder_Traversal < -- > InOrder_Traversal < -- > PostOrder_Traversal 
class Node :
    def __init__(self,value):
        self.left = None
        self.right = None
        self.data = value

def Pre_Order(root):
    if (root != None):
        print(root.data, end = " ")
        Pre_Order(root.left)
        Pre_Order(root.right)

def In_Order(root):
    if (root != None):
        In_Order(root.left)
        print(root.data, end = " ")
        In_Order(root.right)

def Post_Order(root):
    if (root != None):
        Post_Order(root.left)
        Post_Order(root.right)
        print(root.data, end = " ")

root = Node(1)
root.left = Node(3)
root.right  = Node(5)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.right = Node(8)

Pre_Order(root)