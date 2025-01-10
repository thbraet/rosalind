from rosalind.read_files import read_codon_dict


def get_nucleotide_counts(sequence: str) -> dict[str, int]:
    """
    Count the frequency of each nucleotide (A, C, G, T, U) in a given DNA or RNA sequence.

    Args:
        strand (str): A string representing the DNA or RNA sequence, consisting of the characters 'A', 'C', 'G', 'T' (DNA) or 'A', 'C', 'G', 'U' (RNA).

    Returns:
        dict[str, int]: A dictionary where the keys are the nucleotides ('A', 'C', 'G', 'T', 'U') and the values are their respective counts in the DNA or RNA sequence.
    
    Example:
        >>> get_nucleotide_counts("ACGTTAGC")
        {'A': 2, 'C': 2, 'G': 2, 'T': 2, 'U': 0}
        >>> get_nucleotide_counts("ACGUUAGC")
        {'A': 2, 'C': 2, 'G': 2, 'U': 2, 'T': 0}
    """
    # Include 'U' for RNA and 'T' for DNA
    freq_dict = {nucleotide: sequence.count(nucleotide) for nucleotide in "ACGTU"}
    return freq_dict



def transcribe_dna_to_rna(dna_sequence: str) -> str:
    """
    Transcribe a DNA sequence to an RNA sequence by replacing all occurrences of 'T' with 'U'.
    
    Args:
        dna_sequence (str): A string representing the DNA sequence, consisting of the characters 'A', 'C', 'G', and 'T'.

    Returns:
        str: A string representing the RNA sequence, where all occurrences of 'T' in the DNA sequence 
             are replaced with 'U'.
    
    Example:
        >>> transcribe_dna_to_rna("ACGT")
        'ACGU'
        
        >>> transcribe_dna_to_rna("ATTGCAT")
        'AUUGCAU'
    """
    return dna_sequence.replace("T", "U")

def get_complementary_dna_strand(dna_sequence: str) -> str:
    """
    Generate the complementary strand of a given DNA sequence by replacing each nucleotide 
    with its complementary base and reversing the sequence.

    The function follows these base-pairing rules:
    - A (Adenine) is complemented by T (Thymine)
    - T (Thymine) is complemented by A (Adenine)
    - C (Cytosine) is complemented by G (Guanine)
    - G (Guanine) is complemented by C (Cytosine)

    Args:
        dna_sequence (str): A string representing the DNA sequence, consisting of the characters 'A', 'T', 'C', and 'G'.

    Returns:
        str: A string representing the complementary DNA strand, where each nucleotide is replaced by its complement, 
             and the sequence is reversed.

    Example:
        >>> get_complementary_dna_strand("ATCG")
        'CGAT'
        
        >>> get_complementary_dna_strand("GATTACA")
        'TGAATCT'
    """
    # Define the translation table for nucleotide replacement
    translation_table = str.maketrans('ATCG', 'TAGC')
    # Reverse the DNA sequence and translate it using the table
    return dna_sequence[::-1].translate(translation_table)

def get_gc_content(dna_sequence: str) -> float:
    """
    Calculate the relative amount of 'C' and 'G' characters compared to the total length of the DNA sequence.

    Args:
        dna_sequence (str): A string representing the DNA sequence, consisting of the characters 'A', 'C', 'G', and 'T'.

    Returns:
        float: The relative amount of 'C' and 'G' characters in the DNA sequence, expressed as a decimal 
               between 0 and 1. A value of 0 means no 'C' or 'G', while 1 means all characters are 'C' or 'G'.
    
    Example:
        >>> get_gc_content("ACGT")
        0.5
        
        >>> get_gc_content("CGCG")
        1.0
        
        >>> get_gc_content("ATAT")
        0.0
    """
    # Count the occurrences of 'C' and 'G' in the DNA sequence
    cg_count = dna_sequence.count('C') + dna_sequence.count('G')
    
    # Calculate the relative amount (CG count divided by total length)
    return cg_count / len(dna_sequence) if dna_sequence else 0.0

def find_substring_positions(strand: str, sub_strand: str, position_type: str = "all") -> int | list[int]:
    """
    Find all the starting positions of a substring within a DNA string.

    Args:
        strand (str): The DNA sequence.
        sub_strand (str): The substring to search for within the DNA sequence.
        position_type (str, optional): A string that specifies which positions to return. Can be "first", "last", or "all". Default is "last".

    Returns:
        int or list[int]: An integer for the "first" or "last" position, or a list of integers for "all" positions.
    
    Example:
        >>> find_substring_positions("ACGTACGT", "CGT", "first")
        2
        
        >>> find_substring_positions("AAAAAA", "AA", "all")
        [1, 2, 3, 4, 5]
        
        >>> find_substring_positions("AGCTAGC", "TC", "last")
        4
    """
    if sub_strand == "":
        return -1
    
    positions = []
    for i in range(len(strand) - len(sub_strand) + 1):
        if strand[i:i+len(sub_strand)] == sub_strand:
            positions.append(i + 1)  # 1-based index

    if position_type == "first":
        # Return the first occurrence
        return positions[0] if positions else -1  # Return -1 if no match
    
    elif position_type == "last":
        # Return the last occurrence
        return positions[-1] if positions else -1  # Return -1 if no match
    
    # Default behavior: return all positions
    return positions if positions else []


def split_rna_into_codons(rna: str) -> list[str]:
    """
    Splits an RNA sequence into codons.

    A codon is a sequence of three RNA nucleotides. This function takes a string representing an RNA sequence 
    and splits it into a list of codons, where each codon is a substring of three nucleotides.

    Args:
        rna (str): The RNA sequence to split. It should consist of a valid RNA nucleotide sequence (A, U, G, C).

    Returns:
        list[str]: A list of codons, each represented as a string of three nucleotides.
    """
    return [rna[i:i + 3] for i in range(0, len(rna), 3)]


def translate_rna_to_protein(rna: str) -> str:
    """
    Translates an RNA sequence into a protein string.

    This function takes an RNA sequence, splits it into codons, and translates each codon into its corresponding
    amino acid based on a codon dictionary. Translation stops if a "Stop" codon is encountered.

    Args:
        rna (str): The RNA sequence to translate. It should consist of a valid RNA nucleotide sequence (A, U, G, C).

    Returns:
        str: The protein string resulting from translating the RNA sequence. Stop codons are not included in the output.
    """
    codon_dict = read_codon_dict()
    
    protein_string = ""
        
    codons = split_rna_into_codons(rna)
    
    for c in codons:
        if len(c) < 3:
            break
        protein = codon_dict[c]
        if protein == "Stop":
            break
        protein_string += protein
    
    return protein_string

    