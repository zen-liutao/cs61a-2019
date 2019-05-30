def count_digits(n):
    '''
    >>> count_digits(4)
    1
    >>> count_digits(12345678)
    8
    >>> count_digits(0)
    0
    '''
    number_digits = 0
    while n:
        n = n // 10
        number_digits += 1
    return number_digits


def count_matches(n, m):
    '''
    >>> count_matches(10, 30)
    1
    >>> count_matches(12345, 23456)
    0
    >>> count_matches(121212, 123123)
    2
    >>> count_matches(111, 11) # only one's place matches
    2
    >>> count_matches(101, 10) # no place matches
    0
    '''
    number_digit_matches = 0
    while n and m:
        digit1, digit2 = n % 10, m % 10
        if digit1 == digit2:
            number_digit_matches += 1
        n = n // 10
        m = m // 10
    return number_digit_matches
