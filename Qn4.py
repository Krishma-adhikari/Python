# Qn-4
# Count Categories (Mini AI thinking)
emails = ["spam", "not spam", "spam", "spam", "not spam"]
count = 0
i = 0
for email in emails:
  if email == "spam":
    count = count + 1
  elif email == "not spam":
    i = i + 1
  else:
   print("Invalid")
print("Number of spam emails:", count)
print("Number of not spam emails:", i)