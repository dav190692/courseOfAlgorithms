from collections import deque
import avl_node
class AVL:
    def __init__(self) -> None:
        self.root = None


    


    def preOrderTraversal(self):
        result = []
        def traversal(node):
            if not  node:
                return
            result.append(node.data)
            traversal(node.left)
            traversal(node.right)
        traversal(self.root)
        return result
    
    def inOrderTraversal(self):
        result = []
        def traversal(node):
            if not node:
                return
            traversal(node.left)
            result.append(node.data)
            traversal(node.right)
        traversal(self.root)
        return result
    


    


    def postOrder(self):
        result = []
        def traversal(node):
            if not node:
                return
            traversal(node.left)
            traversal(node.right)
            result.append(node.data)
        traversal(self.root)
        return result
    


    def levelOrderTraversal(self):
        result = []

        def travers(curent_node):
            if not curent_node:
                return
            
            de = deque([curent_node])
            

            while de:
                node = de.popleft()
                result.append(node.data)
                if node.left:
                    de.append(node.left)
                if node.right:
                    de.append(node.right)
                # print(result)

        travers(self.root)


        return (result)
    

    def __contains(self, current_node, data):
        if current_node == None:
            return False
        if data == current_node.data:
            return True
        if data < current_node.data:
            return self.__contains(current_node.left, data)
        if data > current_node.data:
            return self.__contains(current_node.rigth, data)
        
    def contains(self, data):
        self.__contains(self.root, data)


    def getHeight(self, node):
        if node is None:
            return 0
        return node.height
        

    def getBalance(self, node):
        if  node is None:
            return 0
        return self.getHeight(node.left) - self.getHeight(node.right)
        
    


    

    

    

    def rightRotate(self, node):
        newRoot = node.left
        temp = newRoot.right
        newRoot.right = node
        node.left = temp

        node.height = max(self.getHeight(node.left), self.getHeight(node.right)) + 1
        newRoot.height = max(self.getHeight(newRoot.left), self.getHeight(newRoot.right)) + 1
        return newRoot



    def leftRotate(self, node):
        newRoot = node.right
        temp = newRoot.left
        newRoot.left = node
        node.right  = temp

        node.height = max(self.getHeight(node.left), self.getHeight(node.right)) + 1
        newRoot.height = max(self.getHeight(newRoot.left), self.getHeight(newRoot.right)) + 1
        return newRoot
    

    def __insertNode(self, node, data):
        
        if node is None:
            return avl_node.TreeNode(data)
        if data > node.data:
            node.right = self.__insertNode(node.right, data)
        elif data < node.data:
            node.left = self.__insertNode(node.left, data)
        else:
            return node

        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
    
        balance = self.getBalance(node)

        if  balance > 1 and data < node.left.data:
            return self.rightRotate(node) 
        if balance < -1 and data > node.right.data:
            return self.leftRotate(node)
        if balance > 1 and data > node.left.data:
            node.left = self.leftRotate(node.left)
            return self.rightRotate(node)
        if balance < -1 and data < node.right.data:
            node.right = self.rightRotate(node.right)
            return self.leftRotate(node)
        
        # print(self.root.height)
        return node
    


    def insert(self, value):
        if self.root is None:
            self.root = avl_node.TreeNode(value)
            # print(self.root.height)
        else:
            self.root = self.__insertNode(self.root, value)

    def minimum_value(self, node):
        while node.left is not None:
            node = node.left
        return node.data
    

    def __delete_node(self, node, data):
        if  node is None:
            return None
        if data < node.data:
            node.left = self.__delete_node(node.left, data)
        elif data > node.data:
            node.right = self.__delete_node(node.right, data)
        else:
            if node.left == None and node.right == None:
                return None
            elif node.left == None:
                node = node.right
            elif node.right == None:
                node = node.left
            else:
                sub_tree_min = self.minimum_value(node.right)
                node.data = sub_tree_min
                node.right = self.__delete_node(node.right, sub_tree_min)
        
    
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        balance = self.getBalance(node)


        if balance > 1 and self.getBalance(node.left) >= 0:
            return self.rightRotate(node)
        if balance < -1 and self.getBalance(node.right) <= 0:
            return self.leftRotate(node)
        if balance > 1 and self.getBalance(node.left) < 0:
            node.left  = self.leftRotate(node.left)
            return self.rightRotate(node)
        if balance < -1 and self.getBalance(node.right) > 0:
            node.right = self.rightRotate(node.right)
            return self.leftRotate(node)
        

        return node
    


    def delete_node(self, data):
        self.__delete_node(self.root, data)




    def del_entire_tree(self):       
        self.root.data = None
        self.root.left = None
        self.root.right = None









    
    



 




my_avl = AVL()




my_avl.insert(30)
my_avl.insert(25)
my_avl.insert(35)
my_avl.insert(20)
my_avl.insert(15)
my_avl.insert(5)
my_avl.insert(10)
my_avl.insert(50)
my_avl.insert(60)
my_avl.insert(70)
my_avl.insert(65)

my_avl.delete_node(20)
# my_avl.__delete_node(my_avl.root, 25)



# my_avl.del_entire_tree()

















print(my_avl.levelOrderTraversal())

























        


