from heapq import headpush, heappop, heapify

class minheap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i-1)/2

    def insertkey(self, k):
        headpush(self.heap, k)

    def decreasekey(self, i , new_value):
        self.heap[i] = new_value
        while(i != 0 and self.heap[self.parent(i)]>self.heap[i]):
            