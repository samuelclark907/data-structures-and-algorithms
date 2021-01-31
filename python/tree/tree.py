print('Hello World')

class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, root = None):
        self.root = root

    def pre_order(self):
        def traverse(root):
            if not root:
                return "Tree Empty"
            print(root.value)
            traverse(root.left)
            traverse(root.right)
        traverse(self.root)

    def in_order(self):
        def traverse(root):
            if not root:
                return "Tree Empty"
            
            traverse(root.left)
            print(root.value)
            traverse(root.right)
        traverse(self.root)

    def post_order(self):
        def traverse(root):
            if not root:
                return "Tree Empty"
            traverse(root.left)
            traverse(root.right)
            print(root.value)
        traverse(self.root)


class BinarySearchTree(BinaryTree):
    def contains(self, value):
        def traverse(node):
            while node:
                if node.value == value:
                    print("true")
                    return True
                if value < node.value:
                    traverse(node.left)
                else:
                    traverse(node.right)
                print("false")
                return False
        return traverse(self.root)


    def add(self, value):
        nn = Node(value)
        def traverse(node):
            if nn.value < node.value:
                if node.left:
                    traverse(node.left)
                else:
                    node.left = nn
            else:
                if node.right:
                    traverse(node.right)
                else:
                    node.right = nn
        if self.root:
            traverse(self.root)
        else:
            self.root = nn
        # print("Hello Add")
        # root = self.root
        # def traverse(root, value):
        #     if not root:
        #         print("not self")
        #         root = value
                # print(self.root.value)
            # if value.value < self.root.value:
            #     if not self.root.left:
            #         self.root.left = value 
            #     else:
            #         traverse(self.root.left, value)
            #         value = self.root
        #     if value.value > root.value:
        #         print(root.right)
        #         if not root.right:
        #             root.right = value
        #     else:
        #         traverse(root.right, value)

        # traverse(root, value)

if __name__ == "__main__":
    # a = Node("A")
    # b = Node("B")
    # c = Node("C")
    # d = Node("D")
    # e = Node("E")
    # f = Node("F")

    # tree = BinaryTree()
    # a.left = b 
    # a.right = c
    # tree.root = a 
    # b.left = d
    # b.right = e 
    # c.left = f 
    # tree.pre_order()
    # tree.in_order()
    # tree.post_order()

    g = Node(2)
    h = Node(4)
    i = Node(1)
    j = Node(20)
    k = Node(10)
    l = Node(15)

    bitree = BinarySearchTree()
    # print(bitree.root.value)
    # bitree.add(g)
    # bitree.add(h)
    
    bitree.add(10)
    bitree.add(20)
    bitree.add(30)
    bitree.add(9)
    bitree.add(7)
    bitree.contains(9)
    # print(bitree.root)
    # print(bitree.root.value)
    # print(bitree.root.left.value)
    # print(bitree.root.right.value)
    # print(bitree.root.right.right.value)
    # print(bitree.root.left.value)
    # print(bitree.root.left.left.value)
   
   