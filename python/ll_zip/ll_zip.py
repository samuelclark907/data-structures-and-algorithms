class Node:
    def __init__(self,value,next= None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, head= None):
        self.head = head


    def __str__(self):
        current = self.head
        output = ""
        while current is not None:
            output += f"{{ {current.value} }} -> "
            current = current.next
        return output + "None"


    def append(self, value):
        newnode = Node(value)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = newnode
        else:
            self.head = newnode

    @staticmethod
    def zipLists(a=object, b=object):
        cur1, cur2 = a.head, b.head
        while cur1 and cur2:
            next1,cur1.next = cur1.next, cur2
            if next1:
                next2, cur2.next = cur2.next, next1
            cur1, cur2 = next1, next2
        return a.head



if __name__ == "__main__":


    new_node = Node(1)
    ll1 = LinkedList(new_node)
    ll1.append(3)
    ll1.append(5)
    ll1.append(7)
    ll2 = LinkedList(Node(2))
    ll2.append(4)
    ll2.append(6)
    ll2.append(8)
    print(ll1)
    print(ll2)
    print(zipLists(ll1,ll2))
