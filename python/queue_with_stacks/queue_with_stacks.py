from stacks_and_queues.stacks_and_queues import Stack

class PseudoQueue():
    def __init__(self):
        self.main = Stack()
        self.temp = Stack()


    def __len__(self):
        return len(self.main) + len(self.temp)


    def enqueue(self, value):
        while not self.main.is_empty():
            self.temp.push(self.main.pop())
        self.main.push(value)
        while not self.temp.is_empty():
            self.main.push(self.temp.pop())

            
        return self.main.top.value
        

    def dequeue(self):
        # self.main.pop()
        return self.main.pop()
        # while not self.main.is_empty():
        #     self.main.pop()
        # return self.main.pop()

            



            






