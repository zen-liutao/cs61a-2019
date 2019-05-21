"""Optional questions for Lab 1"""

# While Loops

def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 0)
    1
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    """
    result = 1
    i = 0
    while i < k:
        result = result * (n-i)
        i += 1
    return result

def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    while n:
        remainder = n % 100
        if remainder % 88 == 0:
            return True
        n = n // 10
    return False

    while n:
        last_digit = n % 10
        if last_digit == 8 and last_digit_is_eight:
            last_digit_is_eight = True
        n = n // 10
        last_but_one_digit = n % 10
        if last_but_one_digit == 8:
            return True
        else:
            last_digit = False
    return False
