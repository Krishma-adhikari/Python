#number guessing game.
n = int(input("Enter range upto which we can guess the target ."))
target = 40
i = 1
while(i <= n):
 guess = int(input("Enter your guess : "))

 if guess == target:
    print("Target found. Stop.")
    break
 elif guess < target:
    print("Enter Higher number.")
    i = i+1
 elif guess > target :
       print("Enter Lower number.")
       i = i+1
else:
   print("Enter upto which we can guess the target.")

print("Total guesses :",i)