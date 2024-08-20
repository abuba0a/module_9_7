def is_prime(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        for i in range(2, res):
            if res % i == 0:
                print('Составное')
                break
        else:
            print('Простое')

        return res
    return wrapper


@is_prime
def sum_three(a, b, c):
    sum3 = a + b + c
    return sum3


result = sum_three(2, 3, 6)
print(result)
print()
result = sum_three(1, 2, 7)
print(result)
print()
result = sum_three(14, 13, 10)
print(result)

