                                                                # stack using array
# import maxsize from sys module
# Used to return -infinite when stack is empty


from sys import maxsize


# Function to create a stack. It initializes size of stack as 0
def Stack():
    stack = []
    return stack

# Stack is empty when stack size is 0
def empty(stack):
    return len(stack) == 0


# Function to add an item to stack. It increases size by 1
def push(stack, item):
    stack.append(item)
    print(item + " pushed to stack ")


# Function to remove an item from stack. It decreases size by 1
def pop(stack):
    if (empty(stack)):
        return str(-maxsize - 1)  # return minus infinite
    return stack.pop()

# Function to return the top from stack without removing it
def peek(stack):
    if (empty(stack)):
        return str(-maxsize - 1)  # return minus infinite
    return stack[len(stack) - 1]


# Driver program to test above functions
stack = Stack()
push(stack, str(10))
push(stack, str(20))
push(stack, str(30))
print(pop(stack) + " popped from stack")



                                                                      # stack using linked list

class stackNode:
    def__inti__(self, data):
    self.data = data
    data.next = None

class stack:
    def__inIt__(Self):
    self.head = None

def empty(self):
    return True if self.head is None else False

def push(self, new_data):
    new_node = stackNode(new_data)
    new_node.next = self.head
    self.head = new_node
    print("%d pushed to stack"%(new_data))

def pop(self):
    if(self.empty()):
        return float("-inf")
    temp = self.head
    self.head = self.head.next
    popped = temp.new_data
    return popped

def peek(self):
    if self.empty():
        return float("-inf")
    return self,head.new_data










# push

# begin
#  if stack is full
#     return
#  endif
# else
#  increment top
#  stack[top] assign value
# end else
# end procedur

# pop
# begin
#  if stack is empty
#     return
#  endif
# else
#  store value of stack[top]
#  decrement top
#  return value
# end else
# end procedure



from sys import maxsize
def createstack():
    stack = []
    return stack
# stack is empty when stack is zero
def Empty(stack):
    return len(stack) == 0

def push(stack, item):
    stack.append(item)
    print(item)
def pop(stack):
    if (empty(stack)):
        return str(maxsize -1)
    return stack.pop() #  decrement top
def peek(stack):
    if(empty(stack)):
        return str(maxsize -1)
    return stack[len(stack)-1]






class stacknode:
    def __init__(self, data):
        self.data = data
        self.next = None

class stack:
    def __init__(self):
        self.head = None
    def empty(self):
        return True if self.head is None else False
    def push(self, new_data):
        new_node = stacknode(new_data)
        new_node.next = self.head
        self.head = new_node
    def pop(self):
        if self.empty():
            return float("- inf")
        return self.head.data













        # Python program to
        # demonstrate stack implementation
        # using collections.deque

        from collections import deque

        stack = deque()

        # append() function to push
        # element in the stack
        stack.append('a')
        stack.append('b')
        stack.append('c')

        print('Initial stack:')
        print(stack)

        # pop() function to pop
        # element from stack in
        # LIFO order
        print('\nElements popped from stack:')
        print(stack.pop())
        print(stack.pop())
        print(stack.pop())

        print('\nStack after elements are popped:')
        print(stack)

        # uncommenting print(stack.pop())
        # will cause an IndexError
        # as the stack is now empty













        # Python program to
        # demonstrate stack implementation
        # using queue module

        from queue import LifoQueue

        # Initializing a stack
        stack = LifoQueue(maxsize=3)

        # qsize() show the number of elements
        # in the stack
        print(stack.qsize())

        # put() function to push
        # element in the stack
        stack.put('a')
        stack.put('b')
        stack.put('c')

        print("Full: ", stack.full())
        print("Size: ", stack.qsize())

        # get() function to pop
        # element from stack in
        # LIFO order
        print('\nElements popped from the stack')
        print(stack.get())
        print(stack.get())
        print(stack.get())

        print("\nEmpty: ", stack.empty())








