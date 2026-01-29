# for loops
a = "Krishma"
for i in a :
    print(i,end=",")


#printing the odd and even number seperately from 1 upto 10.
print("Even numbers : ") 
for i in range(1,11):
    if i % 2 == 0 :
      print(i)

print("Odd Numbers")
for i in range(1,11):
   if i % 2 != 0 :
      print(i)
listt = ['Apple','Ball','Cat','Dog']
for fruit in listt:
    print(fruit)
    for i in fruit:
        print(i)

for i in range(20001):
   print(i)
for i in range(1,10,2):
   print(i)