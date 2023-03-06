
user_number = int(input("Enter number from 1 to 100: "))
if user_number not in range(1, 101):
    print("Error! Incorrect number.")
else:
    if user_number % 3 == 0 and user_number % 5 == 0:
        print("Fizz Buzz")
    elif user_number % 3 == 0:
        print("Fizz")
    elif user_number % 5 == 0:
        print("Buzz")
    else:
        print(user_number)
