# STACK - Abstract Data Structure - implementation using basic python + OOP

'''
1. The name stack data structure resembles a pile of objects, stack of papers, or a tower of blocks, where
    adding and removing of items occur only at the top of the pile.
2. A stack an abstract linear data type. collection of objects that supports fast last=in, first-out (LIFO)
    semantics for inserts and deletes
3. Unlike lists or arrays, stacks typically dont allow for random access to the objects they contain.
4. The insert and delete operations are also often called push and pop operations
5. Stacks and Queues are both linear collections of items.
    a. However, in a queue the least recently added item is removed first, following the First in First Out or FIFO
    b. On the other hand in a stack the most recently added item is removed in the begining following, following the LIFO


A real-life example of a stack is a pile of heavy and precious plates, all kept on top of the other. If you wish to add a plate or 
remove one , you can do that only from the top. However, if you wish to remove a lower plate from the stack, you have to remove the topmost plates one by one, in order to 
1. A useful real-world analogy for a stack data structure is a stack of plates:
    A. New plates are added to the top of the stack. And because the plates are precious and heavy, only the topmost plate can be removes (last-in, first-out). To reach the plates lower down in the stack the topmost plates must be removed one by one.

The basic operations which are performed in the stack are mentioned below:
    1. Push: Adds an item in the stack. Once the stack is full, it is said to be in an Overflow condition.
    2. Pop: Removes an item from the stack. It follows a reversed order to pop items similar to the way when items are pushed. It is said to be an Underflow condition.
    3. Peek or Top: Returns Top element of stack
    4. isEmpty: Returns true if stack is empty, else false

Applications of Stacks:
    1. They are used to reverse a string. Each of the characters are pushed in and then popped off, which results in a reversed string.
    2. It is used in Expression Evaluation and Expression Conversion (infix to postfix, infix to prefix, postfix to infix and prefix to infix)
    3. It is used for forward and backward features in web browsers.
    4. It is used for recursive parsing in Natural Language Processing.
    5. It is used in syntax parsing and parenthesis checking
    6. It is used for Backtracking like finding paths to a maze or exhaustive searching
    7. It is used in algorithms like tower of hanoi, trree traversals, histogram problem and also in graph algorithms like Topological sorting

Understanding Stack Operations:
    There are mainly two types of primitive stack operations:
    1. Push: It is performed to insert and store and element in the stack. However, when you try to insert an element in a stack which is fulll, the Overflow condition occurs.
    2. Pop: It is used to remove an element from the stack. However, when the stack is empty, the Underflow condition occurs.
Push:- Lets consider editing a python fiile using the undo feature in your editor so you can have a clear understanding of the stackk operations. At first, a new function called Insert is added. The push operation adds the Insert function into the stack.
Pop:- Now to perform the pop operations, let us make use of the undo feature. when we first hit the undo, it removes the top-most elemtn fo the stack.









# IMPLEMENTING STACK IN PYTHON
1. Python gives you a lot of options for implementing a Python stack. However, there are some basic implementations of Python stack that will fulfil most of your needs.
   Some of those implementations are as follows.
    a. using list
    b. using collections.deque
    c. using custom method
    d. numerous 3rd party packages

A. The list Build-in
        Pythons build-in list type makes a decent stack data structure as it supports push and pop operations in amortized O(1) time

'''

# define the stack
s = []

# add some items to it
s.append('eat')
s.append('sleep')
s.append('code')

# print
print(s)

# pop
print(s.pop())


'''
B. The list Build-in
    1. Using collections deque
    2. Python contains a module names collections. This comprises of deque class which is a double-ended Queues
        that supports inserting and removing elements from either ends.
    3. Because deques support adding and removing elements from either end equally well, they can serve both as queues
    and stacks.
'''

from collections import deque
q = deque()

q.append('eat')
q.append('sleep')
q.append('code')

print(q)
print(q[0])

print(q.pop())


'''
c. Custom method using classes/objects
1. The following stack implementation assumes that the end of the list will hold the top element of the stack.
2. As the stack grows (as push operations occur), new items will be added on the end of the list
3. pop operations will manipulate that same end.

'''

# define stack class
class StackTOPn():
    def __init__(self):
        self.items = []

    # for printing the stack elemnts
    def __str__(self):
        return ' '.join([str(i) for i in self.items])
    
    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items) - 1]
    
    def size(self):
        return len(self.items)
    
    def display_all_items(self):
        return (self.items)
        
# Initialize the stack
s = StackTOPn()
print(s)

# Check list is empty
print(s.isEmpty())

# all elements
s.push('First')
s.push('second')
s.push('third')
print(s)

# displaying all items
for item in s.display_all_items():
    print(item)

print(s.display_all_items())

# Print the recent item inserted
print(s.peek())

# Add a boolean
s.push(True)

# size of the stack
print(s.size())

s.pop()

print(s.display_all_items())


## EXERCISE
# use Stack to reverse the character in string

class stack_reverse():
    def __init__(self):
        self.string=[]
        self.reverse=[]

    def add_string(self, word):
        return self.string.append(word)
    
    def reverser(self):
        for i in range(len(self.string)):
            self.reverse.append(self.string.pop())
        return ' '.join(self.reverse)

    

stack_string_reverse = stack_reverse()

## adding string
lamda_append=(lambda s: stack_string_reverse.add_string(s))
words = 'hello'
for char in words:
    lamda_append(char)
print(stack_string_reverse.string)
print(stack_string_reverse.reverser())


