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
