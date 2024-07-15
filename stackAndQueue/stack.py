import node

class Stack:
    def __init__(self, value):
        new_node = node.Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = node.Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            temp  = self.top
            new_node.next = temp
            self.top = new_node
        self.height += 1

    def pop(self):
        if self.height == 0:
            return None
        temp = self.top
        if self.height == 1:
            self.top = None
        else:
            self.top = temp.next
            temp.next = None
        self.height -= 1
        return temp
        




my_stack = Stack(1)
my_stack.push(2)
my_stack.push(3)
print(my_stack.pop().value)
print(my_stack.pop().value)
print(my_stack.pop().value)
print(my_stack.pop())

print('\n')


my_stack.print_stack()