# pass or fail

test = int(input())
for i in range(test):
    n, tot, p = map(int, input().split())
    j = tot - n
    k = 3 * tot
    l = k + j
    if l >= p:
        print('pass')
    else:
        print('fail')
# The “TypeError: 'str' object cannot be interpreted as an integer”error is raised
# when you pass a string as an argument into a range() statement. To fix this error,
# make sure all the values you use in a range() statement are integers