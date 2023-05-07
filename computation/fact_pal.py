#!/usr/bin/python3
def largest_palindrome_product():
    """
    This function finds the largest palindrome made from the product of two 3-digit numbers.
    """
    largest_palindrome = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            product = i * j
            if str(product) == str(product)[::-1] and product > largest_palindrome:
                largest_palindrome = product
    return largest_palindrome

print(largest_palindrome_product())
