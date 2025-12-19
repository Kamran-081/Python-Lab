#Second Largest Number in a List

arr = list(map(int, input().split()))

largest = second = -10**9

for x in arr:
    if x > largest:
        second = largest
        largest = x
    elif x > second and x != largest:
        second = x

print(second)
