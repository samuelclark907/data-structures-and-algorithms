class InvalidOperationError(BaseException):
    pass


class Node():
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Stack():
    def __init__(self, node=None):
        self.top = node


    def __len__(self):
        count = 0
        curr = self.top
        while curr:
            count += 1
            curr = curr.next
        return count


    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node


    def pop(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        else:
            node = self.top.value
            self.top = self.top.next
            # node.next = None
            return node

    
    def peek(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        return self.top.value

    
    def is_empty(self):
        return self.top is None


class Queue():
    def __init__(self):
        self.front = None
        self.rear = None


    def enqueue(self, value):
        node = Node(value)
        if not self.front:
            self.front, self.rear = node, node
        else:
            self.rear.next = node
            self.rear = node


    def dequeue(self):
        # if self.is_empty():
            # raise InvalidOperationError("Method not allowed on empty collection")
        
        node = self.front.value
        self.front = self.front.next
        return node


    def peek(self):
        # if self.is_empty():
        #     raise InvalidOperationError("Method not allowed on empty collection")
        return self.front.value


    def is_empty():
        if not self.front:
            return True
