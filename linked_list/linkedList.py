import my_node


class LinkedList:
    def __init__(self, value) -> None:
        new_node = my_node.Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append_node(self, value : int) -> bool:
        new_node = my_node.Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

        return True
    

    def pop_node(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next :
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    

    def prepend(self, value): 
        new_node = my_node.Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        new_node.next = self.head
        self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):

        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp
    
    def get (self, index):
        if index > self.length or index < 0:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
            
        return temp
    
    def set_value(self, index, value):
        temp = self.get(index)
        if not temp:
            return None
        temp.value = value
        return True
    

    def insert(self, index, value):
        if index < 0 or index > self.length:
            raise IndexError
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append_node(value)
        new_node = my_node.Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next  = new_node
        self.length += 1
        return True
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop_node()
        prev = self.get(index-1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        print(self.length)
        return temp
        

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        after = temp.next
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    def find_middle_node(self):
        if self.length == 1:
            return self.head
        if self.head is None:
            return None
        low = self.head
        fast = self.head
        
        for _ in range(self.length):
            if fast.next is None or fast.next.next is None:
                return low.value
            fast = fast.next.next
            low = low.next


    def has_loop(self):
        low = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            low = low.next
            if fast == low:
                return True
        return False
    
    def find_kth_from_end (self, k):
        if self.head is None:
            return None
        fast = self.head
        low = self.head
        if k < 0 or k >  self.length:
            return None
        while ( k-1 )   > 0:
            fast = fast.next
            if fast is None:
                return None
            k -= 1
        print(fast.value)
        while fast.next is not None:
            low = low.next
            fast = fast.next

        return low.value

    def partition_list(self, x):
        if not self.head:
            return None
    
        dummy1 = my_node.Node(0)
        dummy2 = my_node.Node(0)
        prev1 = dummy1
        prev2 = dummy2
        current = self.head
    
        while current:
            if current.value < x:
                prev1.next = current
                prev1 = current
            else:
                prev2.next = current
                prev2 = current
            current = current.next
    
        prev1.next = None
        prev2.next = None
        prev1.next = dummy2.next
    
        self.head = dummy1.next


        
    

my_linked_list = LinkedList(1)
my_linked_list.append_node(2)
my_linked_list.append_node(14)
my_linked_list.append_node(45)
my_linked_list.append_node(53)
my_linked_list.append_node(6)
my_linked_list.append_node(73)
my_linked_list.append_node(8)
my_linked_list.append_node(13)
my_linked_list.append_node(119)
my_linked_list.append_node(19)
my_linked_list.append_node(16)

# my_linked_list.tail.next = my_linked_list.head


my_linked_list.print_list()
print('\n')
print('\n')

my_linked_list.partition_list(14)


print('\n')
print('\n')

my_linked_list.print_list()


# print(my_linked_list.find_middle_node())

# print(my_linked_list.has_loop())

# print(my_linked_list.find_kth_from_end(12))







        

