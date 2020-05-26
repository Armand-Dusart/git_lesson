"""
Exercise 2: PARENTHESIS - Level Medium

Your goal is to write a function and it's unit test (and docstrings).
This function should do the following task:

Given a String s containing parenthesis, the function should return True if it respects the parenthesis rule
False if it's not.

Examples
    s = '(()'
    parenthesis(s)
    -> False

    s = '()(()())'
    parenthesis(s)
    -> True

    s = '())())(())'
    parenthesis(s)
    -> False

    s = '(((())()))'
    parenthesis(s)
    -> True
Try to find an optimal way of doing it if possible ;)

BONUS: SQUARE BRAQUETS: Change your function so that it handles in an efficient way both square braquets []
and parenthesis rules. (add some cases in unit testing)
"""


def parenthesis(s):
    count1=0
    for letter in s:
        if letter == "(":
            count1 += 1
        else:
            count1 = count1 - 1
        if count1 == -1:
            return False
    if count1 != 0:
        return False
    else:
        return True
    pass


def brackets(s):
    count1 = 0
    count2 = 0
    for letter in s:
        if letter == "(":
            count1 += 1
        elif letter == ")":
            count1 = count1 - 1
        elif letter == "[":
            count2 += 1
        elif letter == "]":
            count1 = count1 - 1
        if count1 == -1:
            return False
    if count1 != 0 or count2 !=0:
        return False
    else:
        return True
    pass
