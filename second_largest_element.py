# Find second largest number in a list
x = list(map(int,input("Enter elements inside list : ").split()))
n = len(x)

new = []
for item in x:
    if item not in new:
        new.append(item)
new.remove(max(new))
print(max(new))