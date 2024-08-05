import bstConstructor
from collections import deque

class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None


    def isEmpty(self):
        if self.root is None:
            return True
        return False
    
    def getRootData(self):
        if self.root:
            return self.root.value
        return None

    def insert(self, value):
        new_node = bstConstructor.Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.rigth is None:
                    temp.rigth = new_node
                    return True
                temp = temp.rigth


    def __r_insert(self, current_node, value):
        if current_node is None:
            return bstConstructor.Node(value)
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.rigth = self.__r_insert(current_node.rigth, value)
        return current_node



    def r_insert(self, value):
        if self.root is None:
            self.root == bstConstructor.Node(value)
        self.__r_insert(self.root, value)



    




    def contains(self, value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.rigth
            else:
                return True
        return False
    
    def __r_contains(self, current_node, value):
        if current_node == None:
            return False
        if value == current_node.value:
            return True
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        if value > current_node.value:
            return self.__r_contains(current_node.rigth, value)
        

        

    def r_contains(self, value):
        return self.__r_contains(self.root, value)

    def minimum_value(self, curent_node):
        while curent_node.left is not None:
            curent_node = curent_node.left
        return curent_node.value

    def __r_delete_node(self, curent_node, value):
        if curent_node is None:
            return None
        if value < curent_node.value:
            curent_node.left = self.__r_delete_node(curent_node.left, value)
        elif value > curent_node.value:
            curent_node.rigth = self.__r_delete_node(curent_node.rigth, value)
        else:
            if curent_node.left == None and curent_node.rigth == None:
                return None
            elif curent_node.left == None:
                curent_node = curent_node.rigth
            elif curent_node.rigth == None:
                curent_node = curent_node.left
            else:
                sub_tree_min = self.minimum_value(curent_node.rigth)
                curent_node.value = sub_tree_min
                curent_node.rigth = self.__r_delete_node(curent_node.rigth, sub_tree_min)
        return curent_node

    def r_delete_node(self, value):
       self.__r_delete_node(self.root,  value)


    def bfs(self):
        result = []
        level = 1

        def travers(curent_node):
            if not curent_node:
                return
            
            de = deque([curent_node])
            level = 1
            

            while de:
                node = de.popleft()
                result.append(node.value)
                if node.left:
                    de.append(node.left)
                if node.rigth:
                    de.append(node.rigth)
                level = level + 1

        travers(self.root)

        return (result)
    

    def r_preOrder(self):

        result = []
        def travers(curent_node):
            if not curent_node:
                return
            result.append(curent_node.value)
            if curent_node.left is not None:
                travers(curent_node.left)
            if curent_node.rigth is not None:
                travers(curent_node.rigth)

        travers(self.root)
        return result
    

    def pre_order(self):
        de  = deque([self.root])
        result = []
        while de:
            node = de.pop()
            result.append(node.value)
            if node.rigth:
                de.append(node.rigth)
            if node.left:
                de.append(node.left)

        return result
    
    def r_post_order(self):
        result = []
        def traverse(curent_node):
            if not curent_node:
                return
            if curent_node.left is not None:
                traverse(curent_node.left)
            if curent_node.rigth is not None:
                traverse(curent_node.rigth)
            result.append(curent_node.value)
        traverse(self.root)
        return result
    

    def post_order(self):
        if self.root is None:
            return
        temp = deque([self.root])
        out = deque([])

        while temp:
            node =  temp.pop()
            out.append(node.value)
            if node.left:
                temp.append(node.left)
            if node.rigth:
                temp.append(node.rigth)

        while out:
            temp.append(out.pop())
        
        return temp
    

    def r_in_order(self):
        result = []
        def traverse(curent_node):
            if not curent_node:
                return
            if curent_node.left:
                traverse(curent_node.left)
            result.append(curent_node.value)
            if curent_node.rigth:
                traverse(curent_node.rigth)
        traverse(self.root)

        return result
    

    def in_order(self):
        if self.root is None:
            return
        result = []
        temp = deque()
        curent_node = self.root

        while curent_node is not None or temp:
            while curent_node is not None:
                temp.append(curent_node)
                curent_node = curent_node.left
            curent_node = temp.pop()
            result.append(curent_node.value)
            curent_node = curent_node.rigth
        return result
    

    def tree_heigth(self):
        heigth = 0 
        if self.root is None:
            return heigth
        temp = deque([self.root])

        while temp:
            level = len(temp)
            heigth += 1

            for i in range(level):
                node = temp.popleft()

                if node.left:
                    temp.append(node.left)
                if node.rigth:
                    temp.append(node.rigth)

        return heigth

        


        
            

            
            
                
            






    

            
            
        


my_tree = BinarySearchTree()
my_tree.insert(47)            
my_tree.insert(21)                
my_tree.insert(76)          
my_tree.r_insert(18)         
my_tree.r_insert(27)          
my_tree.r_insert(52)
my_tree.r_insert(82)





# my_tree.r_delete_node(199)

# print(my_tree.r_contains(199))

# print(my_tree.isEmpty())

# print(my_tree.getRootData())


print(my_tree.bfs())
print(my_tree.r_preOrder())
print(my_tree.pre_order())
print(my_tree.r_post_order())
print(my_tree.post_order())
print(my_tree.r_in_order())
print(my_tree.in_order())
print(my_tree.tree_heigth())








# print(my_tree.minimum_value(my_tree.root.rigth))





# print(my_tree.root.value)


        