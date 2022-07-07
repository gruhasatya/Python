# consider an algorithm that takes input as positive integer n.
# if n is even divde it by 2.
# if n is odd multiply it by 3 and add 1.

class Weird:
    def __init__(self, n):
        self.n = n
        self.result = 0

    def weird(self):
        if n == 1:
            return 1
        if n %2 == 0:
            n /= 2
        else:
            n = n*3+1
        self.result += 1
        self.weird()

    def get_result(self):
        return self.result











def subsets(number, size):
    if size == 0:
        return [[]]
    if size == 1:
        return [[x] for x in number]
    subs = subsets(number[1:], size-1)
    return subs + [x + [number[0]] for x in subs]

# output -- [[3], [4], [3, 2], [4, 2], [3, 1], [4, 1], [3, 2, 1], [4, 2, 1]]



def subsets(number, size):
    if number == []:
        return [[]]
    x = subsets(number[1:])
    return x +[[number[0]]+ y for y in x]

def wrap(number, n):
    return [x for x in subsets(number) if len(x) == n]

if __name__ == 'main':
    number = [1,2,3,4,5]
    print(wrap(number, 3))


# output -- [[2, 3, 4], [1, 3, 4], [1, 2, 4], [1, 2, 3]]

#Easy

imoprt itertools

def subset(number, size):
    return list(itertools.combinations(number, size))

number = {1,2,3}
size = 2
print(subset(number, size))
# Python program to get all subsets of given size of a set




str  = "ABCD"
n = len(str)
arr = []

for i in range(1, n+1):
    for j in range(i,n)
        arr.append(str[i:(j+1)])

for i in arr:
    print(i)

