vechiles = 200
wheels = 540
if (wheels&1)==1 or wheels<1 or wheels<=vechiles:
    print("Invalid")
else:
    x = ((4*vechiles) - wheels)//2  # 130
    print("two whelleres = {0} four wheeler = {1}".format(x,vechiles-x))# two whelleres = 130 four wheeler = 170








# another statment

# From the input above
# Product of the digits 5,2,4,4
# 5*2*4*4= 160
# Hence, output is 160.

n = int(input())
p = 1
for i in n:
    p* = n
print(p)





# House Robber
def maxi(arr,n):
    include = 0
    exclude = 0
    for i in arr:
        mx = max(include, exclude)
        include = exclude + i
        exclude = mx
    return max(include,exclude)






# codu and sum Love

# Given N number of x’s, perform logic equivalent of the above Java code and print the output
#
# Input
#
# First line contains an integer N
# Second line will contain N numbers delimited by space
# Output
#
# Number that is the output of the given code by taking inputs as specified above


n = int(input())
arr = list(map(int, input().split()))
ans = 0
for i in arr:
    x = 2**i
    if x>99:
        ans += x%100
    else:
        ans += x
print(ans%100)







