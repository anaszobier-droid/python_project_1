import random
print("Play my number guessing game!")
numbers = list(range(1, 1001, 1))
number = int(random.choice(numbers))
numberpicked = int(input("I have chosen a number, what number will you start with: "))
while numberpicked not in numbers:
    numberpicked = int(input("pick another number that is within the specified range: "))
while numberpicked != number :
    if number > numberpicked:
        numberpicked = int(input("greater: "))
        while numberpicked not in numbers:
            numberpicked = int(input("pick another number that is within the specified range: "))
    elif number < numberpicked:
        numberpicked = int(input("less: "))
        while numberpicked not in numbers:
                    numberpicked = int(input("pick another number that is within the specified range: "))

print("You guessed the correct number!")