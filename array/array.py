import array


class DynamicArray:
    def __init__(self, capacity : int = 2):
        self.__cap = capacity
        self.__size = 0
        self.__resize = 2
        self.__arr = array.array('i', [0] * self.__cap)




    def resize(self, new_cap):
        tmp = array.array('i', [0] * new_cap)
        for i in range(self.__size):
            tmp[i] = self.__arr[i]
        self.__arr = tmp
        self.__cap = new_cap
        


    


    def insert(self, position, value):
        if self.__size == self.__cap:
            self.resize(self.__cap * self.__resize)
        if position < 0 or position > self.__size:
            raise IndexError

        if self.__size == 0:
            self.__arr[position] = value
            self.__size += 1
        else:
            for i in range(self.__size, position, -1):
                self.__arr[i] = self.__arr[i -1]
            self.__arr[position] = value
            self.__size += 1

    def print_arr(self):
        print(self.__arr)


    def push_back(self, value):
        if self.__size == self.__cap:
            self.resize(self.__cap * self.__resize)
        self.__arr[self.__size] = value
        self.__size += 1


    def remove(self, index):
        if index < 0 or index >= self.__size:
            raise IndexError
        for i in range(index, self.__size):
            self.__arr[i] = self.__arr[i+1]
        self.__size -= 1


    def contains(self, value):
        if self.__arr:
            for i in range(self.__size):
                if self.__arr[i] == value:
                    return True
        return False
    
    def __getitem__(self, key):
        # if key < 0 or key >= self.__size:
        #     raise IndexError
        if isinstance(key, slice):
            return self.__arr[key]
        elif isinstance(key, int):
            return self.__arr[key]
        else:
            raise TypeError
    
    def __setitem__(self, key, value):
        if key < 0 or key >= self.__size:
            raise IndexError
        self.__arr[key] = value






my_arr = DynamicArray()
my_arr.insert(0, 134)
my_arr.insert(1, 135)
my_arr.insert(2, 136)
my_arr.insert(3, 137)
my_arr.insert(4, 139)
my_arr.push_back(111)
my_arr.push_back(222)
my_arr.push_back(333)
my_arr.push_back(444)
my_arr.insert(8, 1000)

my_arr.remove(0)

print(my_arr[0 : 3])
# my_arr.remove(8)
# my_arr.remove(7) 
# my_arr.remove(0) 













my_arr.print_arr()



        




            


