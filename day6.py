#different types of data types in python
#integer
a1 = 8
print(a1)

a = 13422463627774
print(a)

krishma = 6
print(krishma)

#string
b = 'Krishma'
print(b)

b1 = "Adhikari"
print(b1)

#float
c = 9.003
print(c)

#none
d = None
print(d) 

#complex
e = complex(a,a1)
print(e)

#boolean
r = True
print(r)

#list : collection of different data items (mutable)
list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
print(list1)


# tuple : collection of different data items (immutable)
tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))
print(tuple1) 

#dictionary : collection of data containing a key value pair.
dict1 = {"name":"Krishma", "age":17, "canVote":False}
print(dict1)

#sum (we can add two values of same data type)
print(a+a1)
print(b+b1)


#We can findout the type of data type by using type() functiom
print("The type of krishma is ", type(krishma))
print("The type of b is ",type(b))
print("The type of c is ",type(c)) 
print("The type of d is ",type(d))
print("The type of e is ",type(e))
print("The type of r is ",type(r))
print("The type of list1 is ",type(list1))
print("The type of tuple1 is ",type(tuple1))
print("The type of dict1 is ",type(dict1))
