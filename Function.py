def add_numbers(num1, num2):
    # Adds the two numbers and returns the result
    result = num1 + num2
    return result


def is_even(number):
    # Check if a number is even using remainder operator
    if number % 2 == 0:
        return True
    else:
        return False
    

def reverse_string(text):
    # Return the reversed version of a string using slice method
    return text[::-1]

def count_vowels(text):
    # Count and return the number of vowels in a string
    vowels = "aeiou"
    return len([letter for letter in text if letter in vowels])
    
def calculate_factorial(n):
    # Calculate and return the factorial of a number
    total = 1
    for multiplier in range(1, n + 1):
       total *= multiplier  # Multiply the current total by the number
    return total  # Return the final factorial value

        
