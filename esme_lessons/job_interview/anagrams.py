"""
Exercise 1: ANAGRAMS - Level Easy

Your goal is to write a function and it's unit test.
This function should do the following task:

Given a positive number n from 0 to an infinite value, the function should return a number
that is the highest anagram of n.

Examples:
    n = 68169
    anagram(n)
    -> 98661

    n = 1993
    anagram(n)
    -> 9931

    n = 631
    anagram(n)
    -> 631

    n = 2
    anagram(n)
    -> 2
Try to find an optimal way of doing it if possible ;)
"""


def anagram(number):
    """
    Given a positive number the function returns a number that is the highest anagram.
    :param String n: A positive number
    :return: The biggest anagram of n.

    :rtype: int
    """
    tri = []
    number = str(number)
    for letter in number:
        tri.append(lettre)

    tri = sorted(tri, reverse=True)
    number = "".join(tri)
    number = int(number)
    return number
pass

