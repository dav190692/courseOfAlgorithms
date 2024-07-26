from collections import deque

class Stack:
    def __init__(self):
        self.items = deque()
        self.length = len(self.items)


    def push(self, value):
        self.items.append(value)
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return False 
        self.items.pop()
        self.length -= 1
        return True
    
    def top(self):
        if self.length == 0:
            return None
        return self.items[len(self.items) -1]
    
    def isEmpty(self):
        return self.length == 0
    
    def size(self):
        return self.length







my_stack = Stack()
my_stack.push(67)
my_stack.pop()
my_stack.push(78)
print(my_stack.top())
my_stack.pop()
my_stack.push(567)
my_stack.push(567)
my_stack.push(9999)

print(my_stack.top())



print(my_stack.isEmpty())


print(my_stack.size())






    

    