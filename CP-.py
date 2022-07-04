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

