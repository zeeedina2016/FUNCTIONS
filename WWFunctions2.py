#function to get fibonacci number
def fib(n):

     # if n is less that or equal to 0, return -1
     if n <= 0:
          return -1
     #if n is equal to 1 position 1, return 0
     elif n == 1:
          return 0
     # if n is equal to position 2, return 1
     elif n == 2:
          return 1
     #use fibonnaci to figure out the rest
     else:
          return fib(n-1) + fib(n-2)

# print sequence for nth number
def main():
     print("The fourth Fibonacci number is", fib(4))
     print("The tenth Fibonacci number is", fib(10))
     print("fib(-4) =", fib(-4))
