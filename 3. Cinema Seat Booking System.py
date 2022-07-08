"""
Goal: Using a 2D list, create a booking system for a movie theatre
consists of 40 seats, organized in 5 rows of 8 seats. If a seat is
booked, its correspond cell in the 2D list has a value of 1. If empty,
it has a value of 0.
The system should have a menu system with the following options:

Option 1️⃣: Book a seat by row / column
Option 2️⃣: Book multiple seats in a given row
Option 3️⃣: Book seat in back row
Option 4️⃣: Exit
"""


print("* * * 🎟  Ticket Purchase Center 🎟 * * * ")


def menu():
    print("1️⃣: Book a single seat")
    print("2️⃣: Book multiple seats in a row")
    print("3️⃣: Book a backrow seat")
    print("4️⃣: Exit")


seats = [[0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]]


def single_seat(row, col):
    if seats[row][col] == 0:
        seats[row][col] = 1
        print(f"Great! We reserved seat {col} in row {row} for you ✅")
    else:
        print(f"Sorry this seat {col} in row {row} is taken ❌")


def multiple_seats(row, num_seat):
    ptr1 = 0
    ptr2 = num_seat
    while ptr2 <= len(seats[row]):
        if seats[row][ptr1:ptr2] == [0]*num_seat:
            seats[row][ptr1:ptr2] == [1]*num_seat
            print(f"Great! We reserved seats {ptr1} through {ptr2-1} in row "
                  f"{row} for you ✅")
            return
        ptr1 += 1
        ptr2 += 1
    print(f"Sorry we were unable to book {num_seat} tickets in  row {row} ❌)")


def backrow_seat():
    backrow = seats[4]
    for i in range(len(backrow)):
        if backrow[i] == 0:
            backrow[i] = 1
            print(f"Great! We reserved backrow seat {i} for you ✅")
            return
        print("Sorry the backrow is full ❌")


def selection_system():
    while True:
        menu()
        selection = int(input("Select an option (1-4): "))
        # Option 1: Book a single seat
        if selection == 1:
            row = int(input("Enter a row number (0-5): "))
            col = int(input("Enter a column number (0-7): "))
            single_seat(row, col)

        # Option 2: Book multiple seats in a row
        elif selection == 2:
            row = int(input("Enter a row number (0-5): "))
            num_seat = int(input("Enter number of seats (0-7): "))
            multiple_seats(row, num_seat)

        # Option 3: Book any backrow seat
        elif selection == 3:
            backrow_seat()

        # Option 4: Exit
        elif selection == 4:
            break
            print("Goodbye!")
        else:
            print("Please enter a valid option.")
    print("Thank you for coming! Enjoy the show. 👋")


if __name__ == "__main__":
    selection_system()










