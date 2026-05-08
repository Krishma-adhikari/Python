# list operations
list = [5,1,2,6,7,3,2]
list.append(4)
print(list)

list.sort()
print(list)

list.sort(reverse=True)
print(list)

list.reverse()
print(list)
print(list.index(5))
print(list.count(2))
m = list.copy()
print(m)
m = [3,4,5,1,2]
list.insert(3,5677)
print(list)
list.extend(m)
print(list)
k = list+m
print(k)