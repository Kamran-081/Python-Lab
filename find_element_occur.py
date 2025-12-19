#find all elements occuring more than n/3 times


result = []

nums = [1,1,5,5,5,4,5,2,3,1,1]
n = len(nums)
limit = n // 3

for i in range(n):
    count = 0

    for j in range(n):
        if nums[i] == nums[j]:
            count += 1

    already_added = False
    for x in result:
        if nums[i] == x:
            already_added = True
            break
        
    if count > limit and not already_added:
        result.append(nums[i])
    
    
print(result)
    