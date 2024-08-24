def is_armstrong_number(number: int) -> bool:
    length = len(str(number))
    num_sum = sum(int(i) ** length for i in str(number))
    return num_sum == number
    

def find_armstrong_numbers(limit):
    numbers = []
    for number in range(1, limit):
        if is_armstrong_number(number):
            numbers.append(number)
    if len(numbers) == 0:
        print(f"There are no Armstrong numbers up to {limit}.")
    else:
        print(numbers)
    
def main():
    while True:
        print("\n--- Armstrong Number Checker ---")
        print("1 - Find Armstrong numbers up to a limit")
        print("2 - Check if a specific number is an Armstrong number")
        print("3 - Exit")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                limit = int(input("Enter the limit: "))
                find_armstrong_numbers(limit)
            elif choice == 2:
                number = int(input("Enter the number: "))
                if is_armstrong_number(number):
                    print(f"{number} It's an Armstrong number")
                else:
                    print(f"{number} It's not an Armstrong number")
            elif choice == 3:
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please select 1, 2, or 3.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
