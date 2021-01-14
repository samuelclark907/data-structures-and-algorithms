from stacks_and_queues.stacks_and_queues import Queue

class AnimalShelter():
    def __init__(self):
        self.order = Queue()
        # self.dog = Queue()
        # self.cat = Queue()


    def enqueue(self, animal):
        input = animal.lower()
        if input == "dog":
            self.order.enqueue("dog")
        elif input == "cat":
            self.order.enqueue("cat")


if __name__ == "__main__":
    enqueue(cat)
    print(Queue)
