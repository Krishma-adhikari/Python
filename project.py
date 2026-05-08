#my second project using python
records = []
while(True):
 print("Study Tracker")
 print("1. Add Study Record.")
 print("2. View Study Record.")
 print("3. Exit.")

 choice = input("Enter Your Choice: ")

 match choice:
  case "1":
   date = input("Enter date : ")
   hour = input("Enter studied time : ")
   subject = input("Enter Subect : ")
   record = {'Date':date,'Time':hour,'Subject':subject}
   records.append(record)
   print("Record Added Successfully.")

  case "2":
   if len(records)==0:
    print("No records found.")
   else : 
    print("\nYour Records : ")
    for r in records:
     print(f"Date: {r['Date']}",f"Time: {r['Time']}",f"Subject: {r['Subject']}")

  case "3": 
   print("Bye Keep Studying.")
   break
  case _:
   print("Invalid Choice. Try Again.")
