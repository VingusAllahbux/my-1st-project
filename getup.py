
User_input = int(input("Enter a number:"))
sum_of_number ==0
corepunter=1
while counter <= user_input:
    sum_of_numbers += counter + 1
    print(f"The sum of natural numbers up to {user_input} is: {sum_of_numbers}")





Names = ["Vingus"", "Maria", "Fatima," "Rabia."]
For name in names:
print(name)







user_input = int(input("Enter a number:"))
 Factorial = 1
 Factorial = 1
while count <= user_input:
    factorial *= counter
    counter += 1
    print(f" The factorial of {user_input} is: {factorial}")




    num_terms = in(input("Enter the number of Fibonacci terms:"))
    a, b = 0,1
    print("fibonacci series:")
    for_in range(num_terms):
    print(a, end="")
    a,  b =b, a +b



    user_input = int(input("Enter a number:"))
    reversed_number = 0
while user_input > 0:
    digit = user_input % 10
    reversed_number = reversed_number * 10 + digit user_input // = 10

print(f" The reversed number is: {reversed_number}"))




user_input = input("Enter a string:")
vowel_count = 0
for char in user_input:
    if char.lower() in vowel_count + = "1:"

    print(f"The number of vowels in the stringbis: {vowel_count}")








    user_input = int(input("Enter a number:"))
    original_number  =user_input
    reversed_number = 0
    while user_input >  0:
        digit = user_input % 10
        reversed_number = reversed_number * 10 + digit
        user_input //=10

        if original_number == reversed_number:
            print(f"{orginal_number} is a palindrom.")
    else:
     print(f"{orginal_number} is not a palindrom.")




Sum_of_sequares = 0
 for i in range(1,9):
            sum_of_sequres += i ** 2
            print(f" The sum of the sequares of numbes from to 1 to 8 is: { sum_of_sequares}")


num = int(input("Enter a number:"))

if num% 2 == 0:
    print("Even")
else:
    print("Odd")





user_input = int(input("Enter a yerar:"))
if (user_input % 4 == 0 and user_input % 100 ! = 0) or ( user_input % 400 == o):
    print(f"{user_input} is a leap year.")
else:
    print(f"{user_input} is not a leap year.")


user_age = int(input("Enter your age:"))
if user_age >= 20:
    print("You are an adult.")
else:
    print("You are a minor.")
               




user_number = float("Enter a number:"))
if user_number > 0:
    print("The number is positive.")    
elif user_number  < 0:
        print("The number is negstive.")
else:
        print("The number is zero.")





num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
num3 = float(input("Enter the third number:"))
maxium_number = max(num1, num2, num3)
print(f" The maxium of the three numbes is: {maxium_number}")








numeric_score = float(input("Enter your numeric score:"))
if 90 <= numeric_score <= 100:
    grade = "A"
numeric_score = float(input("Enter your numeric score:"))
if 80 <= numeric_score < 90:
    grade = "B"
  elif: 80 <= numeric_score < 90
    grade = "B"
  elif: 70 <= numeric_score < 80:
    grade = "C"
      elif: 60 <= numeric_score < 70:
        grade = "D"
        elif:
            grade = "F"
            print(f" Your grade is: {grade}")






user_number = int(input("Enter a number:"))
is_prime = true
if user_number <= 1:
    is_prime = false
else:
    for i in range(2, int(user_number**0.5) + 1):
        if user_number % 1 ==0:
            is _prime = false
            break
if is_prime:
    print(f"{user_number} is a prime number.")
else:
    print(f"{user_number} is not a prime number.")








user_year = int(input("Enter a year:"))
if (user_year % 4 == 0 and user_year % 100 != 0) or (user_year % 400 == 0):
    print(f"{user_year} is a leap year.")
else:
    print(f"{user_year} is not a leap year.")









num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
if num1 < num2:
    print(f"The larger number is: {num1}")
elif num1 > num2:
        print(f"The larger number is: {num2}")
else:
        print("The two numbers are equal.")



signup_username=0
signup_password=0
yes="y"
while yes== "y":
    print("1. sign up")
    print("2. sign in")
    user_input=int(input("select option:"))
    if user_input==1:
        print("sign up")
        signup_username=input("Enter user name:")
        signup_password=input("Enter password:")
        print("your account has been created")
        elif user_input==2:
            print("sign in")
            login_username=input("Enter user name:")
            login_password=input("Enter password:")
            if signup_username==login_username and signup_password==login_password:
                print("successful login")
                else:
                    print("invalid user name and password")
                   else:
                    print("invalid command") 
                    yes=input("Do you want to continue y/n:")
                    
print("Thank you")


