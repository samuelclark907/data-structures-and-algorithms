# class Node:
#     def __init__(self,value,next= None):
#         self.value = value
#         self.next = next


# class LinkedList:
#     def __init__(self, head= None):
#         self.head = head


#     def __str__(self):
#         current = self.head
#         output = ""
#         while current is not None:
#             output += f"{{ {current.value} }} -> "
#             current = current.next
#         return output + "None"


#     def append(self, value):
#         newnode = Node(value)
#         if self.head:
#             current = self.head
#             while current.next:
#                 current = current.next
#             current.next = newnode
#         else:
#             self.head = newnode

#     @staticmethod
def zipLists(a=object, b=object):
    cur1, cur2 = a.head, b.head
    while cur1 and cur2:
        save1 = cur1.next
        save2 = cur2.next

        cur1.next = cur2
        cur2.next = save1

        cur1 = save1
        cur2 = save2

    return a

    #     next1,cur1.next = cur1.next, cur2
    #     if next1:
    #         next2, cur2.next = cur2.next, next1
    #     cur1, cur2 = next1, next2
    # return a

