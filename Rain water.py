# def trapped_Water(arr, n):
#     water = 0
#     left = 0
#     right = n - 1
#     while left < right:
#         if arr[left] < arr[right]:
#             left += 1
#             water += arr[left] - arr[left - 1]
#         else:
#             right -= 1
#             water += arr[right] - arr[right + 1]
#     return water
#
#     arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
#     n = len(arr)
#     print(trapped_Water(arr, n))


# sorting list by reverse once
def checkreverse(arr, n):

    temp  = [0]* n
    for i in range(n):
        temp[i] = arr[i]
    temp.sort(reverse = True)
    for i in range(n):
        if temp[i] != arr[i]:
            return False # not sorted

    for j in range(n-1,-1,-1):
        if temp[j] != arr[j]:
            return False

    if i >= j:
        return True
    while i < j:
        if arr[i] != arr[j]:
            return False
        i += 1
        j -= 1
    return True

arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
n = len(arr)
if checkreverse(arr, n) == True:
    print("Sorted")
else:
    print("Not Sorted")



class solution:
    def solve(self, n):
        arr = sorted(range(n), reverse = True)
        i,j=0,len(arr)-1
        while i<j:
            if arr[i] != arr[j]:
                return False
            i+=1
            j-=1
        return True

    while i < j: and arr[i] == arr[j]:
        i += 1
        j -= 1
    return True



















































    # output -- 6
    # Easy
    # Given an array of integers, find the number of subarrays with sum equal to 0.
    # Input: arr[] = {1, -2, 1, 0, 5}
    # Output: 2
    # Explanation: There are two subarrays with sum equal to 0.
    # [1, -2, 1, 0, 5]
    # [1, -2, 1, 0, 5]
    # Easy
    # Given an array of integers, find the number of subarrays with sum equal to 0.
    # Input: arr[] = {1, -2, 1, 0, 5}
    # Output: 2
    # Explanation: There are two subarrays with sum equal to 0.
    # [1, -2, 1, 0, 5]
    # [1, -2, 1, 0, 5]
    # Easy
    # Given an array of integers, find the number of subarrays with sum equal to 0.
    # Input: arr[] = {1, -2, 1, 0, 5}
    # Output: 2
    # Explanation: There are two subarrays with sum equal to 0.
    # [1, -2, 1, 0, 5]
    # [1, -2, 1, 0, 5]
    # Easy
    # Given an array of integers, find the number of subarrays with sum equal to 0.
    # Input: arr[] = {1, -2, 1, 0, 5}
    # Output: 2
    # Explanation: There are two subarrays with sum equal to 0.
    # [1, -2, 1, 0, 5]
    # [1, -2, 1, 0, 5]
    # Easy
    # Given an array of integers, find the number of subarrays with sum equal to 0.
    # Input: arr[] = {1, -2, 1, 0, 5}
    # Output:
