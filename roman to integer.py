# roman values increases from left to right
# so we will come from right to left
# take example CIV = 104
# last to first v=5 I=1 less then 5 so subtract that from result
# now 4 is result and check for C=100 greater then rsult add to result
# result =5-1 = 4+100=104

def romanToInt(s: str) -> int:
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    n = len(s)
    result = roman[s[n-1]]
    for i in range(n-2,-1,-1):  # last second element subtraction goes on left to right
         if roman[s[i]] < roman[s[i+1]]:
             result-= roman[s[i]]
         else:
             result+=roman[s[i]]
    return result

# given the driver code as input