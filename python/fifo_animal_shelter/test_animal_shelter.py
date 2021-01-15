import pytest
from fifo_animal_shelter.fifo_animal_shelter import AnimalShelter, Cat, Dog, Node

def test_enqueu():
    shelter = AnimalShelter()
    shelter.enqueue("cat")
    shelter.enqueue("dog")
    shelter.enqueue("bird")
    assert shelter.front.value == "cat"
    assert shelter.front.next.value == "dog"
    assert shelter.front.next.next.value == "bird"

def test_dequeue():
    shelter = AnimalShelter()
    shelter.enqueue("cat")
    shelter.enqueue("dog")
    shelter.enqueue("bird")
    assert shelter.dequeue() == "cat"
    assert shelter.dequeue() == "dog"
    assert shelter.dequeue() == "bird"