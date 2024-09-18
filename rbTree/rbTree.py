from enum import Enum
from collections import deque



class Color(Enum):
    red  = 'red'
    black = 'black'





class TreeNode:
    def __init__(self, key) -> None:
        self.key = key
        self.parent = None
        self.left = None
        self.rigth = None
        self.color = Color.red


class RBTree:
    def __init__(self) -> None:
        
        self.nil = TreeNode(None)
        self.nil.color = Color.black
        self.root = self.nil



    def __clear(self, current_node):
        if current_node is not self.nil:
            self.__clear(current_node.left)
            self.__clear(current_node.rigth)
            del current_node
        


    def clear(self):
        self.__clear(self.root)


    def left_rotate(self, current_node):
        temp = current_node.rigth
        current_node.rigth = temp.left
        if temp.left is not self.nil:
            temp.left.parent = current_node
        temp.parent = current_node.parent
        if current_node.parent is self.nil:
            self.root = temp
        elif current_node is current_node.parent.left:
            current_node.parent.left = temp
        else:
            current_node.parent.rigth = temp
        temp.left = current_node
        current_node.parent = temp


    def rigth_rotate(self, current_node):
        temp = current_node.left
        current_node.left = temp.rigth
        if temp.rigth is not self.nil:
            temp.rigth.parent = current_node
        temp.parent = current_node.parent
        if current_node.parent is self.nil:
            self.root = temp
        elif current_node is current_node.parent.left:
            current_node.parent.left = temp
        else:
            current_node.parent.rigth = temp
        temp.rigth = current_node
        current_node.parent = temp


    def insert_fixup(self, new_node):
        while new_node.parent.color.value == 'red':
            if new_node.parent == new_node.parent.parent.left:
                uncle = new_node.parent.parent.rigth
                if uncle.color.value == 'red':
                    new_node.parent.color = Color.black
                    uncle.color = Color.black
                    new_node.parent.parent.color = Color.red
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.rigth:
                        new_node = new_node.parent
                        self.left_rotate(new_node)
                    new_node.parent.color = Color.black
                    new_node.parent.parent.color = Color.red
                    self.rigth_rotate(new_node.parent.parent)
            else:
                uncle = new_node.parent.parent.left
                if uncle.color.value == 'red':
                    new_node.parent.color = Color.black
                    uncle.color  = Color.black
                    new_node.parent.parent.color = Color.red
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.left:
                        new_node = new_node.parent
                        self.rigth_rotate(new_node)
                    new_node.parent.color = Color.black
                    new_node.parent.parent.color = Color.red
                    self.left_rotate(new_node.parent.parent)
        self.root.color = Color.black
                



    def insert(self, data):
        new_node = TreeNode(data)
        parent_node = self.nil
        current = self.root

        while current is not self.nil:
            parent_node = current
            if new_node.key < current.key:
                current = current.left
            else:
                current = current.rigth

        new_node.parent = parent_node

        if parent_node is self.nil:
            self.root = new_node
        elif new_node.key < parent_node.key:
            parent_node.left = new_node
        else:
            parent_node.rigth = new_node


        new_node.left = self.nil
        new_node.rigth = self.nil
        self.insert_fixup(new_node)



    def __search(self, current_node, key):
        if current_node is self.nil:
            return self.nil
        if current_node.key == key:
            return current_node
        if current_node.key > key:
            return self.__search(current_node.left, key)
        if current_node.key < key:
            return self.__search(current_node.rigth, key)
        
    def search(self, key):
        return self.__search(self.root, key)
    


    def transplant(self, target_node, with_node):
        if target_node.parent == self.nil:
            self.root = with_node
        elif target_node.parent.left == target_node:
            target_node.parent.left = with_node
        else:
            target_node.parent.rigth = with_node
        with_node.parent = target_node.parent



    def tree_minimum(self, current_node):
        while current_node.left is not self.nil:
            current_node = current_node.left
        return current_node
    

    def tree_maxsimum(self, current_node):
        while current_node.rigth is not self.nil:
            current_node = current_node.rigth
        return current_node
    


    def delete_fixup(self, current_node):
        while current_node != self.root and current_node.color.value == 'black':
            if current_node == current_node.parent.left:
                sibling = current_node.parent.rigth
                if sibling.color.value == 'red':
                    sibling.color = Color.black
                    current_node.parent.color = Color.red
                    self.left_rotate(current_node.parent)
                    sibling = current_node.parent.rigth
                if sibling.left.color.value == 'black' and sibling.rigth.color.value == 'black':
                    sibling.color = Color.red
                    current_node = current_node.parent
                else:
                    if sibling.rigth.color.value == 'black':
                        sibling.left.color = Color.black
                        sibling.color = Color.red
                        self.rigth_rotate(sibling)
                        sibling = current_node.parent.rigth
                    sibling.color = current_node.parent.color
                    current_node.parent.color = Color.black
                    self.left_rotate(current_node.parent)
                    x = self.root
            else:
                sibling = current_node.parent.left
                if sibling.color.value == 'red':
                    sibling.color = Color.black
                    current_node.parent.color = Color.red
                    self.rigth_rotate(current_node.parent)
                    sibling = current_node.parent.left
                if sibling.rigth.color.value == 'black' and  sibling.left.color.value == 'black':
                    sibling.color = Color.red
                    current_node = current_node.parent
                else:
                    if sibling.left.color.value == 'black':
                        sibling.rigth.color = Color.black
                        sibling.color = Color.red
                        self.left_rotate(sibling)
                        sibling = current_node.parent.left
                    sibling.color = current_node.parent.color
                    current_node.parent.color = Color.black
                    sibling.left.color = Color.black
                    self.rigth_rotate(current_node.parent)
                    current_node = self.root
        current_node.color = Color.black



        

    

    def delete(self, key):
        target_node = self.search(key)

        if target_node is self.nil:
            return
        
        nodeToBeDel = target_node
        replacement = None
        original_color = nodeToBeDel.color.value


        if target_node.left is self.nil:
            replacement = target_node.rigth
            self.transplant(target_node, target_node.rigth)

        elif target_node.rigth == self.nil:
            replacement = target_node.left
            self.transplant(target_node, target_node.left )
        else:
            # nodeToBeDel = self.tree_minimum(target_node.rigth)
            nodeToBeDel = self.tree_maxsimum(target_node.left)

            original_color = nodeToBeDel.color.value
            # replacement = nodeToBeDel.rigth
            replacement = nodeToBeDel.left

            if nodeToBeDel.parent == target_node:
                replacement.parent = nodeToBeDel
            else:
                # self.transplant(nodeToBeDel, nodeToBeDel.rigth)

                self.transplant(nodeToBeDel, nodeToBeDel.left)

                # nodeToBeDel.rigth = target_node.rigth
                nodeToBeDel.left = target_node.left

                # nodeToBeDel.rigth.parent = nodeToBeDel
                nodeToBeDel.left.parent = nodeToBeDel


            self.transplant(target_node, nodeToBeDel)

            # nodeToBeDel.left = target_node.left
            nodeToBeDel.rigth = target_node.rigth

            # nodeToBeDel.left.parent = nodeToBeDel
            nodeToBeDel.rigth.parent = nodeToBeDel

            nodeToBeDel.color = target_node.color



        del target_node

        if original_color == 'black':
            self.delete_fixup(replacement)


    def bfs(self):
            result = {}
            level = 1

            def travers(curent_node):
                if not curent_node:
                    return
                
                de = deque([curent_node])
                level = 1
                

                while de:
                    node = de.popleft()
                    if node != self.nil:
                        result[node.key] = node.color.value
                    if node.left:
                        de.append(node.left)
                    if node.rigth:
                        de.append(node.rigth)
                    level = level + 1

            travers(self.root)

            return (result)
    


    def r_preOrder(self):

        result = {}
        def travers(curent_node):
            if not curent_node:
                return
            if curent_node != self.nil:
                result[curent_node.key] = curent_node.color.value
            if curent_node.left is not None:
                travers(curent_node.left)
            if curent_node.rigth is not None:
                travers(curent_node.rigth)

        travers(self.root)
        return result
    
    def r_post_order(self):
        result = {}
        def traverse(curent_node):
            if not curent_node:
                return
            if curent_node.left is not None:
                traverse(curent_node.left)
            if curent_node.rigth is not None:
                traverse(curent_node.rigth)
            if curent_node != self.nil:
                result[curent_node.key] = curent_node.color.value
        traverse(self.root)
        return result
    

    def r_in_order(self):
        result = {}
        def traverse(curent_node):
            if not curent_node:
                return
            if curent_node.left:
                traverse(curent_node.left)           
            if curent_node != self.nil:
                result[curent_node.key] = curent_node.color.value
            if curent_node.rigth:
                traverse(curent_node.rigth)
        traverse(self.root)

        return result



    






myTree = RBTree()

myTree.insert(12)
myTree.insert(19)
myTree.insert(43)
myTree.insert(21)
myTree.insert(38)
myTree.insert(48)
myTree.insert(40)
myTree.insert(36)
myTree.insert(39)
myTree.insert(56)
myTree.insert(50)
myTree.insert(60)










myTree.delete(43)


print(myTree.bfs())
print(myTree.r_preOrder())
print(myTree.r_post_order())
print(myTree.r_in_order())



# print(myTree.root.key)










    










