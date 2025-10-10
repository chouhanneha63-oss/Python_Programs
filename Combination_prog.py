import math

n = int(input("Enter number of trials:"))
r = int(input("Enter number of combination/successes:"))
p = float(input("Enter probability of success:"))

nCr = math.factorial(n)//((math.factorial(r))*(math.factorial(n-r)))   
print(f"{n}C{r}:{nCr}")

BD = nCr*(p**r)*((1-p)**(n-r))

print(f"Binomial Distribution:{BD}")
