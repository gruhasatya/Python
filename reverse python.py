def reverse(a,start,end):
    while start < end:
        a[start],a[end] = a[end],a[start]
        start+=1
        end-=1
a = [0,1,2,3,4,5]
reverse(a,0,5)
print(a)
