class  Deque:
    def __init__(self):
        self.items = []
        # self.length = len(self.items)

    def push_front(self, data):
        if self.items:
            self.items.insert(0, data)
            return True
        self.items.append(data)
        return True
        
    def push_back(self, data):
        self.items.append(data)
        return True
    
    def pop_front(self):
        if self.items:
            temp = self.items[0]
            del self.items[0]
            return temp
        return None
    
    def pop_back(self):
        if self.items:
            temp = self.items[len(self.items) -1]
            del self.items[len(self.items) -1]
            return temp
        return None
    
    def front(self):
        if self.items:
            return self.items[0]
        return None
    

    def back(self):
        if self.items:
            return self.items[len(self.items) - 1]
        return None
    
    def empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    

    def clear(self):
        if self.items:
            while self.items:
                del self.items[len(self.items) -1]
            return True
        return 'deque is alredy empty'
    
    def insert_byIndex(self, index, data):
        if index < 0 or index > len(self.items) -1:
            raise IndexError
        self.items.insert(index, data)
        return True
    

    def __getitem__(self, index):
        return self.items[index]
    
    def del_byIndex(self, index):
        if index < 0 or index > len(self.items) -1:
            raise IndexError
        del self.items[index]
        return True



        






my_deque = Deque()


my_deque.push_front(12)
my_deque.push_front(14)




# my_deque.push_back(17)
# my_deque.push_back(19)
# print(my_deque.pop_front())
# print(my_deque.pop_back())

# print(my_deque.front())
# print(my_deque.back())

# print(my_deque.empty())

# print(my_deque.size())


# print(my_deque.clear())
# print(my_deque.clear())



my_deque.insert_byIndex(0, 56)
# my_deque.insert_byIndex(-1, 56)


print(my_deque[1])

my_deque.del_byIndex(1)
print(my_deque[1])















