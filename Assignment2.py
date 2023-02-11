# Q1. What will the following code display?
numbers = [1, 2, 3, 4, 5]
print(numbers[1:-5])
# the current code displays an empty set

#Can you debug and fix the output? The code should return the entire list
numbers1 = [1, 2, 3, 4, 5]

print(numbers1[:])

#Q2. Design a program that asks the user to enter a store’s sales for each day of the
# week. The amounts should be stored in a list. Use a loop to calculate the total sales for
# the week and display the result.

total_sales = 0
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

for i in range(len(days)):
    daily_sales = float(input("Enter this store's sales for {}: ".format(days[i])))
    total_sales += daily_sales

print("This week's sales are ${:.2f}".format(total_sales))

#Q3. Create a list with at least 5 places you’d like to travel to. Make sure the list isn’t in
#alphabetical order
#● Print your list in its original order.
#● Use the sort() function to arrange your list in order and reprint your list.
#● Use the sort(reverse=True) and reprint your list.

trips = ["Montreal", "Tokyo", "Melbourne", "Copenhagen", "Jakarta", "Rio de Janeiro"]

#1

print(trips)

# 2

trips.sort()
print(trips)

#3

trips.sort(reverse=True)
print(trips)

#Q4. Write a program that creates a dictionary containing course numbers and the room
#numbers of the rooms where the courses meet. The program should also create a
#dictionary containing course numbers and the names of the instructors that teach each
#course. After that, the program should let the user enter a course number, then it should
#display the course’s room number, instructor, and meeting time.
courses = {
    "DATA101": {"room": "100", "instructor": "Johnny Cash", "time": "8:00am"},
    "DATA102": {"room": "200", "instructor": "Willie Nelson", "time": "9:00am"},
    "DATA103": {"room": "300", "instructor": "Kris Kristofferson", "time": "10:00am"},
    "DATA104": {"room": "400", "instructor": "Waylon Jennings", "time": "11:00am"},
}

course_numbers = input("Enter a course number from DATA101, DATA102, DATA103, DATA104: ")

if course_numbers in courses:
    course = courses[course_numbers]
    room = course["room"]
    instructor = course["instructor"]
    time = course["time"]
    print("Room:", room)
    print("Instructor:", instructor)
    print("Time:", time)
else:
    print("Course Not Listed")

#Q5. Write a program that keeps names and email addresses in a dictionary as
#key-value pairs. The program should then demonstrate the four options:
#● look up a person’s email address,
#● add a new name and email address,
#● change an existing email address, and
#● delete an existing name and email address.

pairs = {
    "Johnny Cash": "maninblack@gmail.com",
    "Willie Nelson": "ontheroadagain@gmail.com",
    "Kris Kristofferson": "highwayman420@gmail.com",
    "Waylon Jennings": "hazzardduke@gmail.com"
}

def look_up(name):
    if name in pairs:
        print(name + "email address: " + pairs[name])
    else:
        print("Not found.")

# add a name and email address
def add_name(name, email):
    if name in pairs:
        print("Existing name.")
    else:
        pairs[name] = email
        print("Name added.")

# change email address
def change_email(name, email):
    if name in pairs:
        pairs[name] = email
        print("Email changed")
    else:
        print("Not found.")

# Function to delete an existing name and email address
def delete_name(name):
    if name in pairs:
        del pairs[name]
        print("NAme deleted.")
    else:
        print("Not found.")

#1
look_up("Johnny Cash")

#2
add_name("Janis Joplin", "bobbysgirl@gmail.com")
print(pairs)
#3
change_email("Willie Nelson", "blueeyescryin@gmail.com")

#4
delete_name("Waylon Jennings")

