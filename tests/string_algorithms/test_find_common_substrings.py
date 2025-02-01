import pytest
from rosalind.string_algorithms import (
    find_common_substrings,
)  # Replace 'your_module' with the actual module name


@pytest.mark.parametrize(
    "s1, s2, expected_result",
    [
        (
            "hello",
            "yellow",
            ["llo", "ell", "ll", "lo", "o", "ello", "l", "el", "e"],
        ),  # Common substrings: ['e', 'ell', 'o', 'l', 'lo']
        ("abc", "def", []),  # No common substrings
        ("abc", "abc", ["abc", "a", "b", "c", "ab", "bc"]),  # Full overlap
        (
            "abcdef",
            "bcd",
            ["b", "bc", "bcd", "c", "cd", "d"],
        ),  # Partial overlap
        (
            "short",
            "shorter",
            [
                "s",
                "sh",
                "sho",
                "shor",
                "short",
                "h",
                "ho",
                "hor",
                "hort",
                "o",
                "or",
                "ort",
                "r",
                "rt",
                "t",
            ],
        ),
        ("", "nonempty", []),  # Empty first string
        ("nonempty", "", []),  # Empty second string
        ("", "", []),  # Both strings empty
    ],
)
def test_find_common_substring(s1, s2, expected_result):
    result = find_common_substrings(s1, s2)
    # Ensure both lists contain the same elements (order doesn't matter)
    assert sorted(result) == sorted(
        expected_result
    ), f"Expected {expected_result}, got {result}"
