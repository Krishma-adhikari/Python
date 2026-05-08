#format-strings in python

into = "Hi my name is {}. I'm from {}"
name = "Krishma"
Country = "Nepal"
print(into.format(name,Country))

# f-strings
money = 34543.1111
txt = f"For only {money : 2f} NPR"
print(txt)
print(f"My name is {name} and I'm from {Country}")
print(f"My name is \"{{{{name}}}}\" and I live in {Country}")

num = f"{2*56}"
print(num)