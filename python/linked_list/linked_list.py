
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
            output += f"{{{current.value}}}->"
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


    def insertBefore(self, value, newVal):
        current = self.head
        if current is None:
            return 
        newnode = Node(newVal)
        if current.value == value:
            newnode.next = current
            self.head = newnode
        while current.next:
            if current.next.value == value:
                newnode.next = current.next
                current.next = newnode
                break
            current = current.next


    def insertAfter(self, value, newVal):
        current = self.head
        newnode = Node(newVal)
        if current.value == value:
            current.next = newnode
            current = newnode
        while current.next:
            if current.value == value:
                newnode.next = current.next
                current.next = newnode
                break
            current = current.next


    def llkth(self,k):
        current = self.head
        counter = 0
        while current:
            current = current.next
            counter += 1
        if k > counter:
            return "That value is too big"
        for i in range(0,counter - k):
            current = current.next
        return current.value












if __name__ == "__main__":
    # new_node = Node(1)
    # new_linked = LinkedList()
    # print(new_linked)

    # newone_linked = LinkedList(new_node)
    # newone_linked.insert(2)
    # newone_linked.insert(4)
    # print(newone_linked.includes(2))
    # print(newone_linked.includes(4))
    # print(newone_linked.head.value)
    # newone_linked.append(5)
    # newone_linked.append(8)
    # newone_linked.append(7)
    # newone_linked.insertBefore(1,6)
    # newone_linked.insertAfter(1,3)
    # print(newone_linked)
    # newone_linked.insertAfter(6,7)
    # print(newone_linked)
    
    
    # print(newone_linked)
    # val = newone_linked.llkth(2)
    # print(val)


    newone_linked = LinkedList(Node(1))
    newone_linked.insertAfter(1,3)
    newone_linked.append(7)
    print(newone_linked)
    print(newone_linked.llkth(0) == True)

   