# def kthSmallest(arr, n, k):
#     arr.sort()
#     return arr[k - 1]
# if __name__ == '__main__':
#     arr = [12, 3, 5, 7, 19]
#     n = len(arr)
#     k = 2
#     print("K'th smallest element is",
#           kthSmallest(arr, n, k))




import heapq
from heapq import heappop

def find(input, k):

    if not input or len(input) < k:
        exit(-1)

    #transform the input to heap
    heapq.heapify(input)

    #pop k-1 element
    while k > 1:
        heappop(input)
        k = k-1

    #return the root of min heap
    return input[0]

### driver code
if __name__ ='__main__':

    input =[7, 4, 6, 3, 9, 1]
    k = 3
    print(find(input, k))




























# Python3 program to find k'th smallest element
# using min heap

# Class for Min Heap
class MinHeap:

    # Constructor
    def __init__(self, a, size):

        # list of elements in the heap
        self.harr = a

        # maximum possible size of min heap
        self.capacity = None

        # current number of elements in min heap
        self.heap_size = size

        i = int((self.heap_size - 1) / 2)
        while i >= 0:
            self.minHeapify(i)
            i -= 1

        def minHeapify(self, i):
            l = self.left(i)
            r = self.right(i)
            smallest = i
            if ((l < self.heap_size) and                          # if left is less then heap size and elements in the heap[left] < elements in the heap[i]
                    (self.harr[l] < self.harr[i])):
                smallest = l
            if ((r < self.heap_size) and
                    (self.harr[r] < self.harr[smallest])):
                smallest = r
            if smallest != i:
                self.harr[i], self.harr[smallest] = (
                    self.harr[smallest], self.harr[i])
                self.minHeapify(smallest)

    def parent(self, i):
        return (i - 1) / 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    # Returns minimum
    def getMin(self):
        return self.harr[0]

    # Method to remove minimum element (or root)
    # from min heap
    def extractMin(self):
        if self.heap_size == 0:
            return float("inf")

        # Store the minimum value
        root = self.harr[0]

        # If there are more than 1 items, move the last item
        # to root and call heapify
        if self.heap_size > 1:
            self.harr[0] = self.harr[self.heap_size - 1]
            self.minHeapify(0)
        self.heap_size -= 1
        return root

# Function to return k'th smallest element in a given array
def kthSmallest(arr, n, k):
    # Build a heap of n elements in O(n) time
    mh = MinHeap(arr, n)

    # Do extract min (k-1) times
    for i in range(k - 1):
        mh.extractMin()

    # Return root
    return mh.getMin()

# Driver code
arr = [12, 3, 5, 7, 19]
n = len(arr)
k = 2
print("K'th smallest element is", kthSmallest(arr, n, k))

# This Code is contributed by Kevin Joshi



######################################Java#############################################


# package
# heap;
#
# import java.util.Collections;
# import java.util.PriorityQueue;
#
# public
#
#
# class HeapApp {
#
# public static int kthSmallestElementInGivenArrayMaxHeap(int[] arr, int k) {
# if (arr.length < k) {
# System.out.println("Invalid Case");
#
#
# return -1;
# }
#
# PriorityQueue < Integer > maxHeap = new
# PriorityQueue <> (Collections.reverseOrder());
#
# for (int i = 0; i < k; i++)
# {
# maxHeap.add(arr[i]);
# }
#
# for (int i = k; i < arr.length; i++) {
#     if (arr[i] < maxHeap.peek()) {
#     maxHeap.poll();
#     maxHeap.add(arr[i]);
#     }
# }
#
# return maxHeap.peek();
# }
#
# public
# static
# int
# kthSmallestElementInGivenArrayMinHeap(int[]
# arr, int
# k) {
# if (arr.length < k) {
# System.out.println("Invalid Case");
# return -1;
# }
#
# PriorityQueue < Integer > minHeap = new
# PriorityQueue <> ();
#
# for (int i = 0; i < arr.length; i++)
# {
# minHeap.add(arr[i]);
# }
#
# for (int i = 0; i < k - 1; i++) {
#     minHeap.poll();
# }
#
# return minHeap.peek();
# }
#
# public
# static
# void
# main(String[]
# args) {
#
# int[]
# arr = {10, 7, 11, 30, 20, 38, 2, 45};
# int
# k = 3;
#
# System.out.println(HeapApp.kthSmallestElementInGivenArrayMaxHeap(arr, k));
# System.out.println(HeapApp.kthSmallestElementInGivenArrayMinHeap(arr, k));
#
# }
#
}