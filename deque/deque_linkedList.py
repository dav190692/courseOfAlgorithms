class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None



class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        

    def empty(self):
        return self.size == 0

    def push_back(self, value):
        new_node = Node(value)
        if self.empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1
        
        

    def push_front(self, value):
        new_node = Node(value)
        if self.empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def pop_back(self):
        if self.empty():
            raise IndexError
        value = self.tail.value
        if self.head == self.tail: 
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1
        return value

    def pop_front(self):
        if self.empty():
            raise IndexError
        value = self.head.value
        if self.head == self.tail: 
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1
        return value
    

    def front(self):
        if self.empty():
            return None
        return self.head.value
    

    def back(self):
        if self.empty():
            return None
        return self.tail.value


    def __len__(self):
        return self.size
    

    def clear(self):
        self.head = self.tail = None
        self.size = 0
        return True
    

    def __getitem__(self, index):
        if self.empty():
            raise IndexError('Deque is empty')
        if index < 0 or index >= self.size:
            raise IndexError
        
        mid  = int(self.size // 2)
        temp = self.head
        if temp is None:
            return None
        if index < mid:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.size - 1, index, -1):
                temp = temp.prev
        return temp


    def insert_by_index(self, index, new_value):
        temp = self.__getitem__(index)
        prev = temp.prev
        if temp is None:
            return False
        new_node = Node(new_value)
    

        prev.next = new_node
        new_node.next = temp
        new_node.prev = prev
        temp.prev = new_node
        self.size += 1
        return True
    

    



my_deque = Deque()

my_deque.push_back(12)
my_deque.push_back(14)
my_deque.push_back(66)
# my_deque.pop_back()
# my_deque.pop_front()
# my_deque.clear()
# print(len(my_deque))


# print(my_deque[2].value)


# print(my_deque.front())
# print(my_deque.back())

my_deque.insert_by_index(2, 77)


print(len(my_deque))

print(my_deque[0].value)
print(my_deque[1].value)
print(my_deque[2].value)
print(my_deque[3].value)
# print(my_deque[4].value)







    

