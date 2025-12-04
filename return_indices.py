#program to return indices of two numbers that add up to a targetr sum


def two_sum(arr, target):
    n = len(arr)
    
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                return [i, j]
    
    return None


arr = [2, 7, 11, 15]
target = 9
print(two_sum(arr, target))  # [0, 1]
