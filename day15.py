# Create a python program capable of greeting you with Good Morning, Good Afternoon and Good Evening.
#  Your program should use time module to get the current hour. 
# Here is a sample program and documentation link for you:

import time
h = time.strftime("%H:%M:%S")
print(h)
h = int(time.strftime("%H"))

if(4<=h<12):
    print("Good Morning Krishma",". The time is",h)

elif(12<h>=17):
    print("Good Afternoon Krishma",".The time is",h)
elif(17<h>=20):
    print("Good Evening Krishma",".The time is",h)
else:
    print("Good Night Krishma",". The time is",h)

 
