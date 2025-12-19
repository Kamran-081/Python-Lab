#Python Inbuilt List Functions
list = [3, 1, 4, 2]
list.append(5)
list.extend([6, 7])
list.insert(2, 10)
list.remove(1)
list.pop()
print(list.index(4))
print(list.count(3))

list.sort()
list.reverse()

new_lst = list.copy()
print(len(list))
print(min(list))
print(max(list))
print(sum(list))

del list[0]
print(list)