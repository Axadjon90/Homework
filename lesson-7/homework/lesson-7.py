1)def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
print(is_prime(4))
print(is_prime(7)) 
print(is_prime(1)) 
print(is_prime(2))
print(is_prime(9))
False
True
False
True
False

2)def digit_sum(k):
    return sum(int(raqam) for raqam in str(abs(k)))
print(digit_sum(24)) 
print(digit_sum(502)) 
print(digit_sum(-123))
6
7
6
3)def print_powers_of_two(N):
    k = 1
    while 2 ** k <= N:
        print(2 ** k, end=" ")
        k += 1
print_powers_of_two(10)
2 4 8
