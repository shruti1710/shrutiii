import math
from time import sleep

num1 = float(input("Enter first number: \n"))
operator = input("\nEnter operator \n\n + \n\n - \n\n / \n\n % \n\n log \n\n sq root \n\n x^y   : \n")


try:
    if operator == "+":
        num2 = float(input("\nEnter next number: \n"))
        print(f"\n ANS \n{num1 + num2}")

    elif operator == "*":
        num2 = float(input("\nEnter next number: \n"))
        print(f"\n ANS \n{num1 * num2}")

    elif operator == "-":
        num2 = float(input("\nEnter next number: \n"))
        print(f"\n ANS \n{num1 - num2}")

    elif operator == "/":
        num2 = float(input("\nEnter next number: \n"))
        print(f"\n ANS \n{num1 / num2}")

    elif operator == "%":
        num2 = float(input("\nEnter next number: \n"))
        print(f"\n ANS \n{num1 % num2}")

    elif operator == "log":
        print(f"\nANS \n {math.log(num1, 10)}")

    elif operator == "sq root":
        print(f"\nANS \n {num1**0.5}")

    elif operator == "x^y":
        num2 = float(input("\nEnter next number: \n"))
        print(f"\nANS \n {num1 ** num2}\n")
    else:
        print("ERROR!")
    
    

except:
    print("ERROR!")
sleep(5)











