"""Lab 1: Expressions and Control Structures"""

# Q3
def sum_digits(n):
    """Sum all the digits of n.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    """
    "*** YOUR CODE HERE ***"
    sum, this_digit = 0, 0
    while n != 0:
        this_digit = n % 10
        sum += this_digit
        n = n // 10
    return sum
