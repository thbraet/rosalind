from itertools import permutations
from math import factorial
from typing import List, Tuple


def fibonacci_rabbits(n, k=1):
    """
    Calculates the number of rabbit pairs after n months,
    where each pair produces k new pairs each month.

    :param n: Number of months
    :param k: Number of new pairs each mature pair produces per month
    :return: Total number of rabbit pairs after n months
    """
    if n < 0:
        raise ValueError("Number of months (n) must be non-negative.")
    if k < 0:
        raise ValueError("Number of pairs produced (k) must be non-negative.")
    
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1

    # Initialize variables for the previous two terms
    prev2 = 1  # F(n-2)
    prev1 = 1  # F(n-1)

    # Calculate Fibonacci-like sequence iteratively
    for _ in range(3, n + 1):
        current = prev1 + k * prev2
        prev2 = prev1
        prev1 = current

    return prev1

def get_number_of_permutations(n: int) -> int:
    """
    Calculate the total number of permutations for a given integer.

    Args:
        n (int): The integer for which to calculate the number of permutations.

    Returns:
        int: The total number of permutations.

    Examples:
        >>> get_number_of_permutations(3)
        6
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    return factorial(n)


def get_all_permutations(n: int) -> List[Tuple[int, ...]]:
    """
    Generate all possible permutations for numbers from 1 to n.

    Args:
        n (int): The integer for which to generate permutations.

    Returns:
        List[Tuple[int, ...]]: A list of all possible permutations.

    Examples:
        >>> get_all_permutations(3)
        [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
    """
    if n < 1:
        raise ValueError("Input must be a positive integer.")
    return list(permutations(range(1, n + 1)))
