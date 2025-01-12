import pytest
from rosalind.combinatorics import (
    fibonacci_rabbits,
)  # Replace `your_module` with the actual module name


def test_base_case_zero_months():
    assert (
        fibonacci_rabbits(0, 3) == 0
    ), "There should be 0 rabbit pairs if no months have passed."


def test_base_case_one_month():
    assert (
        fibonacci_rabbits(1, 3) == 1
    ), "There should be 1 rabbit pair at month 1."


def test_base_case_two_months():
    assert (
        fibonacci_rabbits(2, 3) == 1
    ), "There should be 1 rabbit pair at month 2."


def test_three_months_with_k_1():
    assert (
        fibonacci_rabbits(3, 1) == 2
    ), "With k=1, there should be 2 rabbit pairs at month 3."


def test_four_months_with_k_1():
    assert (
        fibonacci_rabbits(4, 1) == 3
    ), "With k=1, there should be 3 rabbit pairs at month 4."


def test_ten_months_with_k_3():
    assert (
        fibonacci_rabbits(10, 3) == 1159
    ), "With k=3, there should be 1159 rabbit pairs at month 10."


def test_large_n_small_k():
    result = fibonacci_rabbits(20, 1)
    assert (
        result == 6765
    ), "With k=1, there should be 6765 rabbit pairs at month 20 (classic Fibonacci)."


def test_large_k():
    result = fibonacci_rabbits(5, 5)
    assert (
        result == 41
    ), "With k=5, there should be 41 rabbit pairs at month 5."


def test_invalid_n():
    with pytest.raises(ValueError):
        fibonacci_rabbits(-5, 3)


def test_invalid_k():
    with pytest.raises(ValueError):
        fibonacci_rabbits(5, -1)
