#tuple methods
#We cannot directly make changes in tuple as tuple is an immutable data type. In order  to make changes fiurst we have convert tuple into dict.
#However we can concatenate tuples without converting it to list.
tuple_1 = ("Krishma","Kusum","Kushal","Tara","Govinda",4,3,2,2,3,2)
res = list(tuple_1)
print("The list : ",res)
tuple3 = (3,4,3,2)
print(tuple_1+tuple3)
res.append("Hi")
print(res)

print(tuple_1.count(2))
print(tuple_1.index(3,7,10))
print(len(tuple_1))
tuple_1 = tuple(res) #converting list into tuple.
print(tuple_1)