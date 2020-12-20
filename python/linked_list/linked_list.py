# class LinkedList:
#     """
#     Put docstring here
#     """

#     def __init__(self):
#         # initialization here
#         pass

#     def some_method(self):
#         # method body here
#         pass

class Node:

    def __init__(self, value, next=None):       
        self.value = value
        self.next = next 

    def __str__(self):
        return f"{self.value}"

class LinkedList:
    def __init__(self,value=None):
        self.head = None
        if not value is None:
            node = Node(value)
            self.head = node


    def insert(self, value):
        node = Node(value)
        if self.head is not None:
            node.next = node.head
        node.head = node


    def includes(self, value):
        if self.head is None:
            print("No Elements")
        n = self.head
        while n is not None:
            if value == n:
                return True
            n = n.next
        return False

