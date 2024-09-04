def apply_decorator(func):
    def wrapper():
        print("Decorator Applied")  # Print a message indicating the decorator has been applied
        return func  # Return the original function without calling it
    return wrapper  

def decorator_func():
    # Placeholder function
    pass


#Example
def function():
    print("Original function called")

decorated_function = apply_decorator(function)
decorated_function()