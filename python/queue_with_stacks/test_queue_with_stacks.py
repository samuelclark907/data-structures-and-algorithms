# import pytest
# from queue_with_stacks import PseudoQueue


# queue = PseudoQueue()
# queue1 = PseudoQueue()
# queue2 = PseudoQueue()

# def test_enqueue():
#     assert queue.enqueue(1) == 1
#     assert len(queue) == 1
#     assert queue.enqueue(2) == 1
#     assert len(queue) == 2
#     assert queue.enqueue(3) == 1
#     assert len(queue) == 3

# def test_enqueue_rear():
#     queue2.enqueue(1)
#     queue2.enqueue(2)
#     assert queue2.enqueue(3) == 1
#     assert len(queue2)== 3
#     assert queue2.main.pop() == 1
#     assert queue2.main.pop() == 2
#     assert queue2.main.pop() == 3
    


# def test_dequeue():
#     queue1.enqueue(1)
#     queue1.enqueue(2)
#     assert len(queue1) == 2
#     assert queue1.dequeue() == 1
#     assert queue1.dequeue() == 2
#     assert len(queue1) == 0


#     assert queue1.dequeue() == 1
#     assert len(queue1) == 1

    # queue1.enqueue(3)
    # queue1.enqueue(4)
    # assert len(queue1) == 3
