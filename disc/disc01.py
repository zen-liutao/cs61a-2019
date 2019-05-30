def wears_jacket_with_if(temp, raining):
    """
    >>> wears_jacket_with_if(90, False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(100, True)
    True
    """
    if temp < 60 or raining:
        return True
    return False

def wears_jacket(temp, raining):
    """
    >>> wears_jacket(90, False)
    False
    >>> wears_jacket(40, False)
    True
    >>> wears_jacket(100, True)
    True
    """
    return temp < 60 or raining



def square(x):
    print("here!")
    return x * x


def so_slow(num):
    x = num
    while x > 0:
        x = x + 1
    return x / 0

# print(square(so_slow(5)))

def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    >>> is_prime(2)
    True
    """
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True
