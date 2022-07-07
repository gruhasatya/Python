stack = []
stack.append('a')
stack.append('b')
stack.append('c')
print(stack)
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack)










from collections import deque

stack = deque()

stack.append('a')
stack.append('b')
stack.append('c')

print(stack)
print(stack.pop())
print(stack.pop())
stack.pop()  # just removes dont print

print(stack)











from queue import lifoQueue

stack = lifoQueue(maxsize = 3)

print(stack.qsize())

stack.put('a')
stack.put('b')

print(stack.qsize())

print(stack.get())
print(stack.get())




















class Node:
    def __init__(self, data):
        self.data = data
        self.next = value

class stack:
    def __init__(self):
        self.head = Node("head")
        self.size = 0

    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.value)+"->"  # printing like this
            cur = cur.next              # increment
        return out[:-3]

    def size(self):
        return self.size

    def empty(self):
        return self.size == 0

    def peek(self):
        if self.empty
            raise Exception("peeking from empty value")
        return self.head.next.value

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head.next
        self.head.next = new_node
        self.size += 1

    def pop(self):
        if self.empty():
            raise Exception("nothing to remove")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.new_data







































class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class stack:
    def __init__(self):
        self.head = Node("head")
        self.size = 0

    def __str__(self):
        cur = self.head.next
        output = ""
        while cur:
            out += str(cur.data) + "->"
            cur  = cur.next
        return out[:-3]

    def Size(self):
        return self.size
    def Empty(self):
        return self.size == 0
    def peek(self):
        if self.Empty()
            return self.head.next.data
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head.next
        self.head.next = new_node
        self.size += 1

    def pop(self):
        if self.Empty():
            remove = self.head.next
            self.head.next = self.head.next.next
            self.size -=1
            return remove.value



