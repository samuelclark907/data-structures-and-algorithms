
# Challenge Summary

- Create a brand new PseudoQueue class. Do not use an existing Queue. Instead, this PseudoQueue class will implement our standard queue interface (the two methods listed below), but will internally only utilize 2 Stack objects. Ensure that you create your class with the following methods:

enqueue(value) which inserts value into the PseudoQueue, using a first-in, first-out approach.
dequeue() which extracts a value from the PseudoQueue, using a first-in, first-out approach.
The Stack instances have only push, pop, and peek methods. You should use your own Stack implementation. Instantiate these Stack objects in your PseudoQueue constructor.


## Challenge Description
- move main stack to temporary stack. THen add value to main stack. Then put temp stack back to main stack.

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
O(n)

## Whiteboard
[Challenge 11 Whiteboard ](https://docs.google.com/spreadsheets/d/1IVJQNzRM0imzu3HtopVFi-7JZtH2KfPRQSFXCKl7A_Y/edit?usp=sharing)