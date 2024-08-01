class HashTable:
    def __init__(self, size = 7) -> None:
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 11) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(f'{i} : {val}')

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i  in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None
    
    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys



def item_in_common(listt1, list2):
    my_dict = {}
    for i in listt1:
        my_dict[i] = True

    for i in list2:
        if i in my_dict:
            return my_dict[i]
    return False


ls1 = [1, 2, 3]
ls2 = [6, 4, 8]

print(item_in_common(ls1, ls2))








my_table = HashTable()
my_table.set_item('davit', 32)
my_table.set_item('artak', 89)
my_table.set_item('lusine', 87)
my_table.set_item('vramshapuh', 21)
my_table.set_item('badik', 88)
my_table.set_item('naposh', 88)

print(my_table.get_item('naposh'))

my_table.print_table()

print(my_table.keys())