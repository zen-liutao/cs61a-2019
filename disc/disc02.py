# def curry2(h):
#     return lambda x: lambda y: h(x,y)

# curry3 = lambda h : lambda x: lambda y: h(x,y)

def keep_ints(cond, n):
    """
    >>> def is_even(x):
    ...     return x % 2 == 0
    ...     
    >>> keep_ints(is_even, 5)
    2
    4
    """
    i = 1
    while i <= n:
        if cond(i):
            print(i)
        i += 1


def make_keeper(n):
    """Returns a function which takes one parameter cond and prints out
    all integers 1..i..n where calling cond(i) returns True.
    >>> def is_even(x):
    ...     # Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> make_keeper(5)(is_even)
    2
    4
    """
    def cond_print(cond):
        i = 1
        while i <= n:
            if cond(i):
                print(i)
            i += 1

    return cond_print


def and_add(f, n):
    """Return a new function. This new function takes an
    argument x and returns f(x) + n.
    >>> def square(x):
    ...     return x * x
    >>> new_square = and_add(square, 3)
    >>> new_square(4) # 4 * 4 + 3
    19
    """
    return lambda x : f(x) + n