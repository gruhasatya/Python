# two stacks with costly enqueue
# enQueue(q, x):
#
# While stack1 is not empty, push everything from stack1 to stack2.
# Push x to stack1 (assuming size of stacks is unlimited).
# Push everything back to stack1.
# Here time complexity will be O(n)
#
# deQueue(q):
#
# If stack1 is empty then error
# Pop an item from stack1 and return it
# Here time complexity will be O(1)

class queue:
    def __init__(self):
        self.s1=[]
        self.s2=[]
    def enqueue(self,x ):
        while len(self.s1)!=0:
            self.s2.append(self.s1[-1])
            self.s1.pop()

        self.s1.append(x)

        while len(self.s2)!=0:
            self.s1.append(self.s2[-1])
            self.s2.pop()
  # Dequeue an item from the queue
    def dequeue(self):
        if len(stack.s1)==0:
            x = self.s1[-1]
            self.s1.pop()
            return x

#
# Method 2 (By making deQueue operation costly)
# enQueue(q,  x)
#   1) Push x to stack1 (assuming size of stacks is unlimited).
# Here time complexity will be O(1)
#
# deQueue(q)
#   1) If both stacks are empty then error.
#   2) If stack2 is empty
#        While stack1 is not empty, push everything from stack1 to stack2.
#   3) Pop the element from stack2 and return it.
# Here time complexity will be O(n)


class queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, x):
        self.s1.append(x)

    def dequeue(self):
        if len(self.s1)== 0 and len(self.s2) == 0:
            return
        elif len(self.s1)>0 and len(self.s2)==0:
            while len(self.s1):
                temp = self.s1.pop()
                self.s2.append(temp)
                return self.s2.pop()
        else:
            retur self.s2.pop()




