def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
    
T = int(input())

for _ in range(T):
    case = int(input())

    a = case // 2
    b = case // 2

    while True:
        if is_prime(a) and is_prime(b):
            print(a, b)
            break
        a -= 1
        b += 1