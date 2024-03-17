#sum 2 binary numbers

def add_trailing_zero(n, l):
    if len(n) >= l:
        return n
    else:
        return (l-len(n)) * "0" + n 

def digit_sum(d1, d2):
    #return digit and carry
    if d1 == "0" and d2 == "0":
        return "0", "0"
    elif d1 == "0" and d2 == "1":
        return "1" , "0"
    elif d1 == "1" and d2 == "0":
        return "1", "0"
    elif d1 == "1" and d2 == "1":
        # 1+1 = 2 >> "10" as binary string
        return "0", "1"


def binary_sum_carry(d1, d2, carry):
    d_sum, d_carry = digit_sum(d1, d2)
    

def binary_sum(n1: str, n2: str):
    max_len = max(len(n1), len(n2))
    n1 = add_trailing_zero(n1, max_len)
    n2 = add_trailing_zero(n2, max_len)
    
    

print(binary_sum("101", "11"))