def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)
    

total = fatorial(3)

print(total)