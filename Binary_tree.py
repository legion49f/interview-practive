class Node(object):
    def __init__(self):
        self.leftside = None
        self.rightside = None
        self.data = None


class Tree(object):
    def __init__(self):
        self.root = Node()

    def insert(self, data:int):
        new_node = Node()
        new_node.data = data
        if self.root.data == None:
            self.root = new_node
            return
        placeholder = self.root
        last_node = None
        while(placeholder != None):
            last_node = placeholder
            if(data > placeholder.data):
                placeholder = placeholder.rightside
                print('go right')
            elif(data < placeholder.data):
                placeholder = placeholder.leftside
                print('go left')

        if last_node.data > new_node.data:
            last_node.leftside = new_node
        elif last_node.data < new_node.data:
            last_node.rightside = new_node 
        print('added new node')
    
    def inorder_printout(self):
        placeholder = self.root
        self.inorder_traversal_helper(placeholder)
        
    def inorder_traversal_helper(self, Node):
        if Node == None:
            return
        else:
            self.inorder_traversal_helper(Node.leftside)
            print('Data:', Node.data)
            self.inorder_traversal_helper(Node.rightside)

if __name__ == "__main__":
    tree = Tree()
    tree.insert(15)
    tree.insert(75)
    tree.insert(5)
    tree.insert(705)
    tree.insert(1)
    tree.insert(3)
    tree.insert(500)
    tree.inorder_printout()
    print('Done')