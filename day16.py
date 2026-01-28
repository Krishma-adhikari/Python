x = int(input("Enter a number : "))

match x :
    case 0 :
        print("x is zero.")
    case 1 :
        print("x is one.")
    case 4 :
        print("x is four.")
    case _ if x>10 :
       print("x is greater than 10.")
    case _ if x<10 :
        print("x is less than 10.")
    case _ :
        print("x")