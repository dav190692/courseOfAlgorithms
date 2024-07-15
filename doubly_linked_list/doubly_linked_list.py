import node

class DoublyLinkedList:
    def __init__(self, value):
        new_node = node.Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


    def append(self, value):
        new_node = node.Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.head is None:
            return None
        temp  = self.tail
        if self.length == 1:
            self.tail = None
            self.head = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None

        self.length -= 1
        return temp
    
    def prepend(self, value):
        new_node = node.Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:

            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp  = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return  temp
    

    def get_by_index(self, index):
        if index < 0 or index >= self.length:
            return None
        mid  = int(self.length // 2)
        temp = self.head

        if index < mid:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp
    

    def get_by_value(self, value):
        if not isinstance(value, int):
            raise ValueError
        if self.length == 0:
            return None
        temp = self.head
        mid = int(self.length // 2)

        result = False


        for _ in range(mid):
            if temp.value == value:
                result = True
                return temp
            else:
                temp = temp.next
        
        
        temp = self.tail


        for _ in range(self.length -1, mid-1, -1):
            if temp.value == value:
                result = True
                return temp
            else:
                temp = temp.prev

        if result is False:
            return None
        

    def set_by_index(self, index, new_value):
        temp = self.get_by_index(index)
        if temp is None:
            return False
        temp.value = new_value
        return True

    def set_by_value(self, value, new_value):
        temp = self.get_by_value(value)
        if temp is None:
            return False
        temp.value = new_value
        return True


    def insert_by_index(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0 :
            return self.prepand(value)
        if index == self.length:
            return self.append(value)
        new_node = node.Node(value)
        before = self.get_by_index(index - 1)
        after = before.next

        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node

        self.length += 1

        return True
    
    def insert_by_value(self, value, new_value):
        if value == self.head.value:
            return self.prepand(new_value)
        new_node = node.Node(new_value)
        after = self.get_by_value(value)
        if after is not None:
            before = after.prev
            new_node.prev = before
            new_node.next = after
            before.next = new_node
            after.prev = new_node
            return True
        else:
            return False    
        
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        temp = self.get_by_index(index)
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.next = None
        temp.prev = None
        self.length -= 1
        return temp

        ##Swap First and Last##
    def swap(self):
        new_tail = self.pop_first()
        new_head = self.pop()
        new_head.next = self.head
        self.head = new_head
        new_tail.prev = self.tail
        self.tail.next = new_tail
        self.tail = new_tail

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        for _ in range(self.length):
            after = temp.next
            temp.next = temp.prev
            temp.prev = after
            temp = after
    
    def is_palindrome(self):
        if self.head is None:
            return None
        

        temp1 = self.head
        temp2 = self.tail

        while temp1 and temp2:
            if temp1.value == temp2.value:
                temp1 = temp1.next
                temp2 = temp2.prev
            else:
                return False
        return True
        
    def swap(self):
        if self.length == 0:
            return None
        if self.length == 1:
            return
        temp1 = self.head
        temp2 = temp1.next
        temp3 = self.head

        while  temp1 is not None and temp2 is not None:
            temp1.next = temp2.next
            if temp1.next is not None:
                temp1.next.prev = temp1
            temp2.prev = temp1.prev

            temp2.next = temp1
            temp1.prev = temp2

            if temp2.prev is not None:
                temp2.prev.next = temp2
            

            temp1 = temp1.next
            if temp1 is not None:
                temp2 = temp1.next

        self.head = temp3.prev

        
            























my_doubly_linked_list = DoublyLinkedList(1)
# my_doubly_linked_list.pop()
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)
my_doubly_linked_list.append(5)
my_doubly_linked_list.append(6)

# my_doubly_linked_list.append(6)
my_doubly_linked_list.append(7)
my_doubly_linked_list.append(8)
my_doubly_linked_list.append(9)
my_doubly_linked_list.append(10)
# my_doubly_linked_list.append(999)



my_doubly_linked_list.print_list()

print('\n')
print('\n')

# print(my_doubly_linked_list.is_palindrome())


my_doubly_linked_list.swap()

print('\n')
print('\n')

my_doubly_linked_list.print_list()




