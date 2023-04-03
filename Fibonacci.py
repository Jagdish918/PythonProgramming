def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_0 = 0
        fib_1 = 1
        
        for i in range(2, n+1):
            fib = fib_0 + fib_1
            fib_0 = fib_1
            fib_1 = fib
        return fib
s=int(input("enter the value of n :"))
for i in range(s):
    print(fibonacci(i))


