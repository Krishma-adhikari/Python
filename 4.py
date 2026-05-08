# Print all elements of a list using a loop.
l = [8,4,5,3,20,56,34]
# for i in range(len(l)):
#     print(l[i], end=" ")

# Find the sum of all elements in a list.
# sum = 0
# for i in range(len(l)):
#     sum = sum+l[i]

# print(sum)

# count = 0
# for i in range(len(l)):
#     if l[i] > 10:
#         count = count + 1

# print(count)
# Find the maximum number in a list (without using max()).
l.sort()
print(l[len(l)-1])