import math

def first_task():
    approx_val1 = 0.824
    exact_val1 = 14.0 / 17.0
    error1 = abs(approx_val1 - exact_val1)

    approx_val2 = 7.28
    exact_val2 = math.sqrt(53)
    error2 = abs(approx_val2 - exact_val2)

    print(f"Error in 14/17 = 0.824 is: {error1:.4f}")
    print(f"Error in sqrt(53) = 7.28 is: {error2:.4f}")
    print("14/17 = 0.824 is more precise" if error1 < error2 else "sqrt(53) = 7.28 is more precise")

def second_task():
    original_number = 23.3748
    delta_percent = 0.27
    initial_absolute_error = original_number * delta_percent / 100

    rounded_number = round(original_number, 1)

    rounding_error = abs(rounded_number - original_number)
    total_error = initial_absolute_error + rounding_error

    print(f"Original number: {original_number}")
    print(f"Initial absolute error: {initial_absolute_error:.4f}")
    print(f"Rounded number: {rounded_number}")
    print(f"Rounding error: {rounding_error:.4f}")
    print(f"Total absolute error after rounding: {total_error:.4f}")

def third_task():
    approx_number = 0.645
    min_change = 0.001
    absolute_error = min_change
    relative_error = absolute_error / approx_number

    print(f"Absolute Error: {absolute_error}")
    print(f"Relative Error: {relative_error * 100:.2f}%")

first_task()
print()
second_task()
print()
third_task()
