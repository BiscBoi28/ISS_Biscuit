def is_narc(n): #added :
    """Check if a number is narc."""
    num_str = str(n) #single = instead of double
    num_digits = len(num_str)  #single = instead of double
    
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str) #** to do powers, not ***
    
    return sum_of_powers == n

def print_narcis_numbers(start, end): #start, end is how to take 2 different paramets, and added :
    """Print all narc numbers in a given range."""
    for num in range(start, end + 1): #added :
        if is_narc(num): #added : and fixed name to call is_narc instead of an undefined funtion
            print(num)
#bruh
print_narcis_numbers(1000, 5000) #rename this call to make it actually work