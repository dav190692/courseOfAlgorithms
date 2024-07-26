from collections import deque


class Queue:
    def __init__(self):
        self.items = deque()
        self.length = len(self.items)

    def enqueue(self, value):
        self.items.append(value)
        self.length += 1
        return True
    
    def dequeue(self):
        if self.length == 0:
            return False
        self.items.popleft()
        self.length -= 1
        return True
    
    def peek(self):
        if self.length == 0:
            return None
        return self.items[0]
    
    def isEmpty(self):
        return self.length == 0
    
    def size(self):
        return self.length
    

    