class InvalidOperationError(BaseException):
    pass

class Node():
    def __init__(self,value, next = None):
        self.value = value
        self.next = next

class Cat():
    def __init__(self, type= "cat"):
        self.type = type
        type = "cat"

class Dog():
    def __init__(self, type= "dog"):
        self.type = type
        type ="dog"

class AnimalShelter():
    def __init__(self):
        self.front = None
        self.rear = None 


    def enqueue(self, animal):
        # for ani in [Cat,Dog]:
        #     if ani.type == "dog" or ani.type == "cat":
        node = Node(animal)
        if not self.front:
            self.front, self.rear = node, node
        else:
            self.rear.next = node 
            self.rear = node
                # else:
                #     raise InvalidOperationError("Please choose a cat or a dog")


    def dequeue(self):
        if self.front:
            tmp = self.front
            self.front = self.front.next
            tmp.next = None
            return tmp.value
        else:
            raise InvalidOperationError("Method not allowed on empty collection")




    def is_empty(self):
        if self.front is None:
            return True
        else:
            return False



if __name__ == "__main__":
    shelter = AnimalShelter()
    shelter.enqueue("cat")
    shelter.enqueue("dog")
    # shelter.enqueue("bird")
    print(shelter.front.value)
    print(shelter.front.next.value)
    print(shelter.front.next.next.value)
    print(shelter.dequeue())
    print(shelter.dequeue())
    print(shelter.dequeue())

