def fibonacci(n):
    if n == 0:
        return 0
    
    if n == 1:
        return 1
    
    return fibonacci(n-1) + fibonacci(n-2)

def product(a, b):
    if b == 1:
        return a
    else:
        return a + product(a, b-1)
    
def sum(a, b):
    if b == 0:
        return a
    return sum(a, b-1) + 1

print(fibonacci(3))
print(sum(5,3))
