import node

class Queue:
    def __init__(self, value) -> None:
        new_node = node.Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp:
            print(temp.value)
            temp = temp.next

    def enqueue(self, value):
        new_node = node.Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            temp = self.last
            temp.next = new_node
            self.last = new_node
        self.length += 1
        return True

    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = temp.next
            temp.next = None
        self.length -= 1
        return temp



my_queue = Queue(7)
my_queue.enqueue(8)
my_queue.enqueue(9)


my_queue.dequeue()
my_queue.enqueue(8)



my_queue.print_queue()
        