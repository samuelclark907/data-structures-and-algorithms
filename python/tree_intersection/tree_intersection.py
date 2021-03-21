from tree import BinaryTree, Node

def tree_intersection(tree1,tree2):
    intersection = []
    treelist1 = []
    treelist2 = []
    def traverse(root):
        if not root:
            return "Tree Empty"
        if tree1:    
            treelist1.append(root.value)
            traverse(root.left)
            traverse(root.right)
    def traverse1(root):
        if not root:
            return "Tree Empty"
        if tree1:    
            treelist2.append(root.value)
            traverse1(root.left)
            traverse1(root.right)         
    traverse1(tree2.root)
    traverse(tree1.root)

    for item in treelist1:
        if item in treelist2:
            intersection.append(item)
            treelist1.remove(item)

    return intersection
    

if __name__ == '__main__':
    a = Node("1")
    b = Node("2")
    c = Node("3")
    d = Node("4")
    e = Node("5")
    f = Node("6")

    g = Node("1")
    h = Node("6")
    i = Node("1")
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