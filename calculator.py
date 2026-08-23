print("welcome to my calculator")

firstnum = float(input("What is your first number: "))
operation = input("Please select one of the four available operations: (+, -, *, /)  ")
secondnum = float(input("What is your second number: "))


if operation == "+":
     answer = (firstnum + secondnum)
     print(f"{firstnum} + {secondnum} = {answer}")
elif operation == "-":
     answer = (firstnum - secondnum)
     print(f"{firstnum} - {secondnum} = {answer}")
elif operation == "*":
     answer = (firstnum * secondnum)
     print(f"{firstnum} * {secondnum} = {answer}")
elif operation == "/":
     answer = (firstnum / secondnum)
     print(f"{firstnum} / {secondnum} = {answer}")