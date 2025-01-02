def get_hamming_distance(str1, str2):
    """
    Calculate the Hamming distance between two strings.

    The Hamming distance is defined as the number of differing characters 
    at the same positions in two strings of equal length.

    Parameters:
    str1 (str): The first input string.
    str2 (str): The second input string.

    Returns:
    int: The Hamming distance between the two strings.

    Raises:
    ValueError: If the input strings are not of equal length.
    """
    if len(str1) != len(str2):
        raise ValueError("Strings must be of equal length.")
    
    return sum(char1 != char2 for char1, char2 in zip(str1, str2))
