initial_asset = 0
interest_rate = 0
num_years = 0
while True:
    initial_asset = float(input("Enter the initial asset (greater or equal to 0): "))
    if initial_asset < 0:
        print("Invalid input. Please enter a number greater than 0.")
        initial_asset = float(input("Enter the initial asset (greater or equal to 0): "))
    else:
        break
while True:
    interest_rate = float(input("Enter the interest rate (greater than 0): "))
    if interest_rate < 0:
        print("Invalid input. Please enter a number greater than 0.")
        interest_rate = float(input("Enter the interest rate (greater than 0): "))
    else:
        break
while True:
    num_years = int(input("Enter the number of years (greater or equal to 0): "))
    if num_years < 0:
        print("Invalid input. Please enter a number greater or equal to 0.")
        num_years = int(input("Enter the number of years (greater or equal to 0): "))
    else:
        break
final_asset = initial_asset * pow((1 + interest_rate / 100), num_years)
print(f"The final asset after {num_years} years is: {final_asset:.2f}")

