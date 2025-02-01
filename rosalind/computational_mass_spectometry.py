from rosalind.read_files import read_monoisotopic_mass


def get_protein_mass(amino_acid_chain, rounding=None):
    """
    Calculate the mass of a protein based on its amino acid chain.

    This function calculates the total mass of a protein using monoisotopic masses of amino acids.
    Optionally, the result can be rounded to a specified number of decimal places.

    Parameters:
        amino_acid_chain (str): A string representing the amino acid sequence.
        rounding (int, optional): Number of decimal places to round the result to. Default is None (no rounding).

    Returns:
        float: The total mass of the protein. Rounded to the specified number of decimal places if rounding is provided.
    """
    aa_masses = read_monoisotopic_mass()

    weight = 0
    for c in amino_acid_chain:
        weight += aa_masses[c]

    if rounding is not None:
        return round(weight, rounding)
    return weight
