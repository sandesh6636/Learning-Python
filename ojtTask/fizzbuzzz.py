#Submitted by Sandesh Rai

number = int(input("Enter any number to check whether it is fizzbuzz fizz or buzz "))
if number % 3 ==0 and number % 5 ==0:
    print(number," is fizzbuzz")
elif number % 3 ==0:
    print(number, "is fizz")
elif number % 5 ==0:
    print(number, " is buzz")
else:
    print(number," is not fizzbuzz fizz buzz, try again")

