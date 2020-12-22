
class Node:
    def __init__(self,value,next= None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, head= None):
        self.head = head
       
        


    def insert(self, value):
        node = Node(value)
        if self.head is not None:
            self.next = self.head
        self.head = node


    def includes(self, value):
        if self.head is None:
            print("No Elements")
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False


    def __str__(self):
        current = self.head
        output = ""
        while current is not None:
            output += f"{{ {current.value} }} -> "
            current = current.next
        return output + "None"





if __name__ == "__main__":
    new_node = Node(1)
    new_linked = LinkedList()
    print(new_linked)

    newone_linked = LinkedList(new_node)
    newone_linked.insert(2)
    print(newone_linked.includes(2))
    print(newone_linked.includes(4))
    print(newone_linked.head.value)


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

# class Node:

#     def __init__(self, value, next=None):       
#         self.value = value
#         self.next = next 

#     def __str__(self):
#         return f"{self.value}"

# class LinkedList:
#     def __init__(self,value=None):
#         self.head = None
#         if not value is None:
#             node = Node(value)
#             self.head = node


#     def insert(self, value):
#         node = Node(value)
#         if self.head is not None:
#             node.next = node.head
#         node.head = node


#     def includes(self, value):
#         if self.head is None:
#             print("No Elements")
#         n = self.head
#         while n is not None:
#             if value == n:
#                 return True
#             n = n.next
#         return False

