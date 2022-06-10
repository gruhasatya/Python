import array

arr  = array.array('i',[1,2,3])      # array(data type, value list)

for i in range(0,3):
    print(arr[i], end="")

print("\r")    # to represent or can say it will be done in a line after line

arr.append(4);

for i in range(0,4):
    print(arr[i], end="")

arr.insert(2,5)       #  inset at 2 position 5

print("\r")

for i in range(0,5):
    print(arr[i], end ="")

print("\r")

print(arr.pop(2));   # Removing an elemnt from 2 position  5 will be popped  element

print("\r")

arr.remove(1)  # removes

for i in range(0,3):                  # check the indexing it should not out of range
    print(arr[i], end=" ")

print("\r")

print(arr.index(3))                 # it prints the index value of that element 3 is at index 1 in array

arr.reverse()

for i in range(0,3):
    print(arr[i], end = " ")









c1 = 0
c2 = 0

# FIRST
for i in range(10):
    for j in range(100):
        c1 += 1
    c1 += 1

# SECOND
for i in range(100):
    for j in range(10):
        c2 += 1
    c2 += 1

print("Count in FIRST = ", c1)            # 1010
print("Count in SECOND  = ", c2)          # 1100










c1 = 1
c2 = 1
i = 0
while (i < c1 and i < 10):
    j = -1
    c1 += 1
    while (j < c1 and j < 100):
        c1 += 1
        j += 1
    i += 1

# SECOND
i = 0
while (i < c2 and i < 100):
    j = -1
    c2 += 1
    while (j < c2 and j < 10):
        c2 += 1
        j += 1
    i += 1

print(" Count fot FIRST  ", c1)              #1021
print(" Count fot SECOND  ", c2)             #1201









