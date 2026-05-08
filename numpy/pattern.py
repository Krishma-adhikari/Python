# Given vectors:

# x = [1, 2, 3]  
# w = [4, 5, 6]

# Find dot product (used in predictions)
def product(a,b):
  return a*b

x = list(map(int,input("Enter the values of x : ").split()))
y = list(map(int,input("Enter the values of w : ").split()))
sum = 0
for i in range(len(x)):
  for j in range(len(y)):
    sum = sum + product(x[i],y[j])
print(sum)