print("welcome to my calculator")

firstnum = float(input("What is your first number: "))
secondnum = float(input("What is your second number: "))
operation = input("Please select one of the four available operations: (+, -, *, /)  ")

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