#Author: Siddhartha

class Node(object):

    def __init__(self, data):

        self.data = data
        self.left = None
        self.right = None

    
    def insert(self,data):
        if self.data == data:
            return False 
        elif data < self.data:
            if self.left:
                return self.left.insert(data)
            else:
                self.left = Node(data)
                return True

        else:
            if self.right:
                return self.right.insert(data)

            else:
                self.right = Node(data)
                return True

    
    def findval(self,data):
        if data < self.data:
            if self.left is None:
                return str(data)+ "not found"
            return self.left.findval(data)
        
        elif data > self.data:
            if self.right is None:
                return str(data) + " not found"
            return self.right.findval(data)
        else:
            print(str(self.data) + " is found")


    def PrintTree(self):

        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()


root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)

root.PrintTree()

print(root.findval(7))
print(root.findval(14))