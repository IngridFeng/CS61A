""" Optional problems for Lab 3 """

# Q4
def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    k = 2
    def has_remainder(k):
        if n == k:
            return True
        else:
            if n % k != 0:
                return has_remainder(k + 1)
            return False
    return has_remainder(k)



# Q5
def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    "*** YOUR CODE HERE ***"
    if a < b:
        larger, smaller = b, a
    else:
        larger, smaller = a, b

    if larger % smaller == 0:
        return smaller
    else:
        return gcd(smaller, larger % smaller)

# Q6
def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    "*** YOUR CODE HERE ***"
    def app(n, k): #number of appearance
        if n == 0:
            if k == 0:
                return 1
            return 0
        else:
            if n % 10 == k:
                return app(n // 10, k) + 1
            else:
                return app(n // 10, k)
    return int(app(n,1)*app(n,9)+app(n,2)*app(n,8)+app(n,3)*app(n,7)+app(n,4)*app(n,6)+app(n,5)*(app(n,5)-1)/2)

# Q7
def factors_list(n):
    """Return a list containing all the numbers that divide `n` evenly, except
    for the number itself. Make sure the list is in ascending order.

    >>> factors_list(6)
    [1, 2, 3]
    >>> factors_list(8)
    [1, 2, 4]
    >>> factors_list(28)
    [1, 2, 4, 7, 14]
    """
    all_factors = []
    "*** YOUR CODE HERE ***"

    return [i for i in range(1, n) if n % i == 0]
