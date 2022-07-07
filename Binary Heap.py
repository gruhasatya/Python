from heapq import heappush, heappop, heapify

class heap:
    def __init__(self):
        self.heap = []
        self.size = 0

    def insert(self, data):
        heappush(self.heap, data)
        self.size += 1

    def parent(selfself,i):
        return (i-1)/2

    def decrease_key(self,i , new_value):
        self.heap[i] = new_value
        # its assumed new value is smaller than heap[i]
        while(i != 0 and self.heap[self.parent(i)]> self.heap[i]):

            # swapping function
            self.heap[i], self.heap[(self.parent(i))] = (self.heap[self.parent(i)], self.heap[i])


# removes the minimum element from the heap
    def extract(self):
        return heapop(self.heap)

    def delete(self,i):
        self.heap[i] = float('-inf')
        self.decrease_key(i, self.heap[i])
        self.extract()


    def getmin(self):
        return self.heap[0]

    def printheap(self):
        print(self.heap)

