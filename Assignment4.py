#Q1

class BankAccount:
    def __init__(account, bankname, firstname, lastname, balance=0):
        account.bankname = bankname
        account.firstname = firstname
        account.lastname = lastname
        account.balance = balance

    def deposit(account, amount):
        account.balance += amount

    def withdrawal(account, amount):
        if amount > account.balance:
            print("Insufficient funds. Time to Cook")
        else:
            account.balance -= amount

    def __str__(account):
        return f"Bank Name: {account.bankname}, Account Owner: {account.firstname} {account.lastname}, Account Balance: {account.balance}"

# Test
account = BankAccount("Mesa Verde Bank and Trust", "Walter", "White", 5000)

#account.deposit(500000)

# account.withdrawal(200)

account.withdrawal(1000000)

print(account)

#Q2

class Box:
    def __init__(box, length, width):
        box.length = length
        box.width = width

    def render(box):
        for i in range(box.width):
            print('*' * box.length)

    def invert(box):
        box.length, box.width = box.width, box.length

    def get_area(box):
        return box.length * box.width

    def get_perimeter(box):
        return 2 * (box.length + box.width)

    def double(box):
        return Box(box.length * 2, box.width * 2)

    def __eq__(box, other):
        return box.length == other.length and box.width == other.width

    def print_dim(box):
        print(f"Length: {box.length}")
        print(f"Width: {box.width}")

    def get_dim(box):
        return (box.length, box.width)

    def combine(box, other):
        box.length += other.length
        box.width += other.width

    def get_hypot(box):
        return math.sqrt(box.length ** 2 + box.width ** 2)

# Instantiate 3 boxes
box1 = Box(5, 10)
box2 = Box(3, 4)
box3 = Box(5, 10)

print("Box 1 :")
box1.print_dim()

print("Box 2 :")
box2.print_dim()

print("Box 3 :")
box3.print_dim()

# Evaluation of boxes
print("box1 == box2: ", box1 == box2)
print("box1 == box3: ", box1 == box3)

# Combine box3 and box1
box1.combine(box3)

# Double box2 and Combine box2 and box1
box2_double = box2.double()
box1.combine(box2_double)

# display box1 after combination with other boxes
print(" new box1 dimensions:")
box1.print_dim()

# diagonal length of new box1
print("new box1 diagonal length:", box1.hypotenuse())

