#  Write a program to:

# Find relation between x and y
# Predict value when x = 5
# This is the idea behind Linear Regression
sx = 0
sxy = 0
sy = 0
sx2 = 0
x = [1, 2, 3, 4]
y = [2, 4, 6, 8]
n = len(x)
for i in range(n):
    sx += x[i]
    sy += y[i]
    sxy += x[i] * y[i]
    sx2 += x[i] * x[i]
b = (n * sxy - sx * sy) / (n * sx2 - sx * sx)
a = (sy - b * sx) / n
print("The straight line equation is y = ", b, "x + ", a)

x_new = 5
y = b * x_new + a
print("The predicted value is", y)
