class queue:

    # basic implementation of queue with all the auxiallary operation on queue
    def __init__(self, capacity):
        self.front = self.size = 0
        self.rear = capacity -1
        self.Q = [none]*capacity
        self.capacity = capacity


    def full(self):
        return self.size = self.capacity

    def empty(self):
        return self.size == 0

    def enque(self, new_data):
        if self.full():
            return

        self.rear = (self.rear + 1)%(Self.capacity)# it increments from last
        self.Q[self.rear] = item    # adding at last
        self.size = self.size+1     # incremnt the size


    def dequeue(self):
        if self.empty():
            return

        self.front = (self.front + 1)%(self.capacity) # this is called removing from first in queue
        self.size = self.size -1 # decresing the size

    # function to get front of Queue

    def que_front(self):
        if self.empty():
            return
         print(self.Q[self.front])

    def que_rear(self):
        if self.empty():
            return
        print(self.Q[self.rear])
