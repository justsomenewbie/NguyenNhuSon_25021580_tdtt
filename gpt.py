def get_float(prompt, min_value=0, allow_zero=True):
    while True:
        try:
            value = float(input(prompt))
            if (allow_zero and value >= min_value) or (not allow_zero and value > min_value):
                return value
            else:
                print(f"Invalid input. Please enter a number {'greater than' if not allow_zero else 'greater or equal to'} {min_value}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_int(prompt, min_value=0):
    while True:
        try:
            value = int(input(prompt))
            if value >= min_value:
                return value
            else:
                print(f"Invalid input. Please enter a number greater or equal to {min_value}.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

initial_asset = get_float("Enter the initial asset (greater or equal to 0): ", min_value=0)
interest_rate = get_float("Enter the interest rate (greater than 0): ", min_value=0, allow_zero=False)
num_years = get_int("Enter the number of years (greater or equal to 0): ", min_value=0)

final_asset = initial_asset * pow((1 + interest_rate / 100), num_years)
print(f"The final asset after {num_years} years is: {final_asset:.2f}")
