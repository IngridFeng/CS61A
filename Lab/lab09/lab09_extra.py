# Extra Questions
from lab09 import *

# Q5
def same_shape(t1, t2):
    """Returns whether two Trees t1, t2 have the same shape. Two trees have the
    same shape iff they have the same number of branches and each pair
    of corresponding branches have the same shape.

    >>> t, s = Tree(1), Tree(3)
    >>> same_shape(t, t)
    True
    >>> same_shape(t, s)
    True
    >>> t = Tree(1, [Tree(2), Tree(3)])
    >>> same_shape(t, s)
    False
    >>> s = Tree(4, [Tree(3, [Tree(2, [Tree(1)])])])
    >>> same_shape(t, s)
    False
    """
    "*** YOUR CODE HERE ***"
    if t1.is_leaf() and t2.is_leaf():
        return True
    if len(t1.branches) == len(t2.branches):
        for i in len(t1.branches):
            same_shape(t1.branches[i], t2.branches[i])
    return False


# Q6
def reverse_other(t):
    """Mutates the tree such that nodes on every other (odd-depth) level
    have the labels of their branches all reversed.

    >>> t = Tree(1, [Tree(2), Tree(3), Tree(4)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(4), Tree(3), Tree(2)])
    >>> t = Tree(1, [Tree(2, [Tree(3, [Tree(4), Tree(5)]), Tree(6, [Tree(7)])]), Tree(8)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(8, [Tree(3, [Tree(5), Tree(4)]), Tree(6, [Tree(7)])]), Tree(2)])
    """
    "*** YOUR CODE HERE ***"
    def helper(t, count = True):
        if t.is_leaf():
            pass
        else:
            labels = [b.label for b in t.branches]
            for b in t.branches:
                if count:
                    b.label = labels.pop()
                helper(b, not count)
    helper(t, True)

# Q7
def next_element(bst, n):
    """
	This function takes in a BST and a number N and it returns the smallest
	element that is greater than N, or None if it has no such element.

    >>> t = BST(8, BST(3, BST(1), BST(6, BST(4), BST(7))), BST(10, BST.empty, BST(14, BST(13))))
    >>> next_element(t, 1)
    3
    >>> next_element(t, 3)
    4
    >>> next_element(t, 5)
    6
    >>> next_element(t, 7)
    8
    >>> next_element(t, 10)
    13
    >>> next_element(t, 14)
    >>> result = [1]
    >>> a = next_element(t, 1)
    >>> while a:
    ...   result += [a]
    ...   a = next_element(t, a)
    >>> result
    [1, 3, 4, 6, 7, 8, 10, 13, 14]
    """
    "*** YOUR CODE HERE ***"
    def helper(bst):
        if bst.is_leaf():
            return [bst.label]
        all = [bst.label]
        if bst.left is not BST.empty:
            all.extend(helper(bst.left))
        if bst.right is not BST.empty:
            all.extend(helper(bst.right))
        return all
    lst = [i for i in helper(bst) if i > n]
    if lst:
        return min(lst)
    return None
