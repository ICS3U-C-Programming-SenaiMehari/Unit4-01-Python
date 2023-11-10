#This program uses a while loop to repeatedly prompt the user for input until a valid positive number is entered. It then calculates the sum of all whole numbers from 0 to the entered number using another while loop and displays the result. The try and except blocks are used to catch and handle any invalid entries (e.g., non-integer input or negative numbers).


def sum_of_numbers():
    # Get a positive number from the user
    while True:
        try:
            number = int(input("Enter a positive number: "))
            if number < 0:
                raise ValueError("Please enter a positive number.")
            break
        except ValueError as e:
            print(f"Invalid input. {e}")

    # Calculate the sum using a while loop
    total = 0
    current_number = 0
    while current_number <= number:
        total += current_number
        current_number += 1

    # Display the sum to the user
    print(f"The sum of whole numbers from 0 to {number} is: {total}")


# Call the function to run the program
sum_of_numbers()
