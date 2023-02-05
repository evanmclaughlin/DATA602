# Q1 Fix all the syntax and logical errors in the given source code
# add comments to explain your reasoning

# This program gets three test scores and displays their average.  It congratulates the user if the
# average is a high score. The high score variable holds the value that is considered a high score.

high_score = 95

# Get the test scores.
test1 = float(input('Enter the score for test 1: '))
test2 = float(input('Enter the score for test 2: '))
test3 = float(input('Enter the score for test 3: '))

# Calculate the average test score.
# this calculation needed to be moved up before print command
average = (test1 + test2 + test3) / 3
#print average score
print('The average score is', average)


# Print the average.

# If the average is a high score,
# congratulate the user.
# corrected this to combine the messages so "that is a great average" wasn't included for bad averages
# variable reference needs to be same case as first variable reference
if average >= high_score:
    print('Congratulations! That is a great average!')

# Q2
# The area of a rectangle is the rectangle’s length times its width. Write a program that asks for the length and width of two rectangles and prints to the user the area of both rectangles.

def rectangle_area(length, width):
    return length * width

rect1_length = float(input("Enter the length of rectangle 1: "))
rect1_width = float(input("Enter the width of rectangle 1: "))

rect2_length = float(input("Enter the length of rectangle 2: "))
rect2_width = float(input("Enter the width of rectangle 2: "))

rect1_area = rectangle_area(rect1_length, rect1_width)
rect2_area = rectangle_area(rect2_length, rect2_width)

print("The area of rectangle 1 is", rect1_area)
print("The area of rectangle 2 is", rect2_area)

# Q3
# Ask a user to enter their first name and their age and assign it to the variables name and age.
# The variable name should be a string and the variable age should be an int.

# Using the variables name and age, print a message to the user stating something along the lines of:
# "Happy birthday, name!  You are age years old today!"

name = input("Enter your first name: ")
age = int(input("Enter your age: "))

message = f"Happy birthday, {name}! You are {age} years old today!"
print(message)


