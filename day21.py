#defualt arguement
def sum(a = 2, b = 5):
    print("The sum is",a+b)
sum()


#keyword argument
def sum(a,b):
    return a+b
s = sum(b=5,a=4)
print("The sum is",s)

#required arguement
def sum(a,b):
    print("The sum is",a+b)
sum(5,6)

#Variable length arguement
#arbitary (class type tuple)
def sum(*num):
    jum = 0
    for i in num :
        jum = jum + i
        print("The sum is ",jum)
sum(4,7,6,5)

#keyword-arbitary(class type dict)
def name(**name):
    print("Hello",name["a"],name["b"])
name(a = "Krishma", b = "Adhikari")

