def partition(arr):
    total = 0       
    for x in arr:
        total += x
    

  #if total is odd, we cannot split
    if total % 2 != 0:
        return False
    
    
    half = total // 2
    
   
    prefix_sum = 0
    for x in arr:                #compute prefix sum and check
        prefix_sum += x
        if prefix_sum == half:
            return True

    return False      # No position where left and right sums match


arr = [1, 2, 3, 3, 2, 1]
print(partition(arr))
