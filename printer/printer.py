import queue_deque


class Printer:
    def __init__(self) -> None:
        self.print_queue = queue_deque.Queue()



    def add_print_job(self, value):
        self.print_queue.enqueue(value)

    def print_job(self):
        print(self.print_queue.peek())
        self.print_queue.dequeue()

    def peek(self):
        print(self.print_queue.peek())

    def isEmpty(self):
        return self.print_queue.isEmpty()
    
    def size(self):
        return self.print_queue.size()
    

my_printer = Printer()


print(my_printer.print_queue)
my_printer.add_print_job("Barev")
my_printer.add_print_job("Vlad")

my_printer.print_job()
my_printer.print_job()

# my_printer.print_job()
my_printer.peek()

# print(my_printer.isEmpty())
# print(my_printer.size())
# print(my_printer.print_queue[0])