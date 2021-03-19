from tree import BinaryTree, Node

def tree_intersection(tree1,tree2):
    intersection = []
    treelist1 = []
    treelist2 = []
    def traverse(root):
        if not root:
            return "Tree Empty"
        elif tree1.root:    
            treelist1.append(root.value)
            traverse(root.left)
            traverse(root.right)
        elif not tree1.root:
            treelist2.append(root.value)
            traverse(root.left)
            traverse(root.right)            

    traverse(tree1.root)
    traverse(tree2.root)
    print(treelist1)
    print(treelist2)

if __name__ == '__main__':
    a = Node("1")
    b = Node("2")
    c = Node("3")
    d = Node("4")
    e = Node("5")
    f = Node("6")

    g = Node("7")
    h = Node("8")
    i = Node("9")
    j = Node("10")
    k = Node("11")
    l = Node("12")

    tree1 = BinaryTree()
    a.left = b 
    a.right = c
    tree1.root = a 
    b.left = d
    b.right = e 
    c.left = f

    tree2 = BinaryTree()
    g.left = h 
    g.right = i
    tree2.root = g 
    h.left = j
    h.right = k 
    i.left = l

    tree_intersection(tree1, tree2)