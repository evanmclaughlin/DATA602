#Q1
meal = input("What meal are you in the mood for (breakfast, lunch, or dinner)? ")

if meal == "breakfast":
    print("How about some bacon and eggs?")
elif meal == "lunch":
    print("You could try a salad. New year, new you.")
elif meal == "dinner":
    print("How about housing Dylan's burger down at Graham's Loralei Lounge?")
else:
    print("That's not a meal, dummy.")

#Q2
hours = float(input("Enter hours worked: "))
rate = float(input("Enter rate per hour: "))

if hours > 20:
    hours_norm = 20
    overtime = hours - 20
    total = (hours_norm * rate) + (overtime * (rate * 1.5))
else:
    total = hours * rate

print("Total = $", total)

#Q3

def times_ten(number):
    product = number * 10
    print(product)

print(times_ten(6))

#Q4
def main():
    calories1 = float(input("How many calories are in the first food?"))
    calories2 = float(input("How many calories are in the second food?"))
    show_calories(calories1, calories2)

def show_calories(calories1, calories2):
    total_calories = calories1 + calories2
    print("Total calories:", total_calories)

main()

#Q5
loop_sum = 0

for i in range(1, 31):
    loop_sum += i / (31 - i)

print("loop_sum total: ", loop_sum)

#Q6
def tri_area(base, height):
    area = 0.5 * base * height
    return area
print(tri_area(5,4))