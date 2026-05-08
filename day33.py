#Dictionaries
dic = {'name':'Krishma','addres':'Nuwakot','Favorite singer':'Atif Aslam','Roll':8}
print(dic)

print(dic['name'])
print(dic.get('address'))
print(dic['Favorite singer'])
print(dic['Roll'])

print(dic.values())
print(dic.items())
print(dic.keys())

for i in dic.keys():
    print(f"The corresponding value of {i} is {dic[i]}.")