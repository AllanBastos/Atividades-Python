def fib(n):
    if n == 2:
        return 1
    elif n == 3:
        return 1
    return fib(n-1) + fib(n-2)

termo = int(input())
print(fib(termo))