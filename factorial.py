def factorial(n):
    """Calculate factorial of a number recursively."""
    if n == 0:
        return 1 
    return n * factorial(n - 1)

# Example usage
num = 10
print(f"Factorial of {num} is {factorial(num)}")
