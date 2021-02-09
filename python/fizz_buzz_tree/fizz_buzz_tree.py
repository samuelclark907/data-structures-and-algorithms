from stacks_and_queues import Queue

def fizz_buzz(value):
    if value % 15 == 0:
        # print("FizzBuzz")
        return "FizzBuzz"
    elif value % 5 == 0:
        # print("Fizz")
        return "Fizz"
    elif value % 3 == 0:
        # print("Buzz")
        return "Buzz"
    else:
        # print(value)
        return str(value)



class K_node: 
    def __init__(self, value): 
        self.value= value 
        self.child = [] 
        # <--- List of children that the nodes has.

class Tree:
    def __init__(self):
        self.root = None


def fizz_buzz_tree(tree):
    output = Tree()
    if tree.root:
        que = Queue()
        que.enqueue(tree.root)
        output.root = K_node(fizz_buzz(tree.root.value))
    while not que.is_empty():
        deq = que.dequeue()
        # print(deq.child)
        for child in deq.child:
            output.root.child.append(K_node(fizz_buzz(child.value)))
            if child.child:
                que.enqueue(child)
    print(output.root.value)
    print(output.root.child[0].value)
    print(output.root.child[0].child)
    
        



if __name__ == "__main__":
    # node = K_node(20)
    tree = Tree()
    # tree.root = node
    tree.root = K_node(1)
    tree.root.child.append(K_node(2))
    tree.root.child.append(K_node(3))
    tree.root.child.append(K_node(4))
    tree.root.child[0].child.append(K_node(5)) 
    tree.root.child[0].child[0].child.append(K_node(10)) 
    tree.root.child[0].child.append(K_node(6)) 
    tree.root.child[0].child[1].child.append(K_node(11))
    tree.root.child[0].child[1].child.append(K_node(12))
    tree.root.child[0].child[1].child.append(K_node(15)) 
    tree.root.child[2].child.append(K_node(7))
    tree.root.child[2].child.append(K_node(8))
    tree.root.child[2].child.append(K_node(9))

    fizz_buzz_tree(tree)
    