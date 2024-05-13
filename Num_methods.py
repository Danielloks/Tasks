import math

def first_task():
    approx_val1 = 0.871
    exact_val1 = 27.0 / 31.0
    error1 = abs(approx_val1 - exact_val1)

    approx_val2 = 6.48
    exact_val2 = math.sqrt(42)
    error2 = abs(approx_val2 - exact_val2)

    print(f"Error in {approx_val1} is: {error1:.6f}")
    print(f"Error in {approx_val2} is: {error2:.6f}")
    print(f"Error in {approx_val1} is more precise" if error1 < error2 else f"Error in {approx_val2} is more precise")

def second_task():
    original_number = 0.088748
    delta_percent = 0.56
    initial_absolute_error = original_number * delta_percent / 100

    rounded_number = round(original_number, 1)

    rounding_error = abs(rounded_number - original_number)
    total_error = initial_absolute_error + rounding_error

    print(f"Original number: {original_number:.6f}")
    print(f"Initial absolute error: {initial_absolute_error:.6f}")
    print(f"Rounded number: {rounded_number:.1f}")
    print(f"Rounding error: {rounding_error:.6f}")
    print(f"Total absolute error after rounding: {total_error:.6f}")

def third_task():
    approx_number = 71.385
    min_change = 0.001
    absolute_error = min_change
    relative_error = absolute_error / approx_number

    print(f"Absolute Error: {absolute_error:.6f}")
    print(f"Relative Error: {relative_error * 100:.6f}%")

first_task()
second_task()
third_task()
