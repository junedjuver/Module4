n = int(input ("Enter number you want to find factorial of: "))
def factorial(n):
    if n<2:
        return 1
    else:
        return n * factorial(n-1)
Result = factorial(n)
print(f'Factorial of {n} is {Result}.')
