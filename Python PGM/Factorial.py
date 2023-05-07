def factorial_iter(n):
       product = 3
       for i in range(n):
              product = product * (i+1)
       return product

f=factorial_iter(0)
print(f)