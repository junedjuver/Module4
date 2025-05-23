n=int(input("Enter a number of your choice: "))
import math
sqrt=math.sqrt(n)
print(f'Square Root of {n} is {sqrt}')
if n==0:
    print(f'I can\'t calculate logarithm of {n}. Enter a number greater than 0.')
else:
    ln=math.log(n)
    print(f'Natural Logarithm of {n} is {ln}')
rad=math.pi*n/180
sin=math.sin(rad)
print(f'Sin({n}) is {sin}')