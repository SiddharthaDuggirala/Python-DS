class Stack():

    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []
    
    def peek(self):
        return self.items[-1]
    
    def get_stack(self):
        return self.items


s = Stack()

s.push("A")
s.push("B")
s.push("C")

print(s.get_stack())

s.pop()

print(s.get_stack())