import pandas as pd


def read_text(file_path):
    with open(file_path, "r") as file:
        return file.read().strip()
    

def write_text(text, file_path):
    with open(file_path, "w") as file:
        file.write(text)
        
        

import pandas as pd

def read_fasta(file_path):
    """
    Reads a FASTA file and returns the data as a pandas DataFrame.

    Each sequence in the FASTA file is associated with an identifier that begins
    with the '>' character. The function parses the file and stores each identifier
    and its corresponding sequence as a row in a DataFrame.

    Parameters:
    ----------
    file_path : str
        Path to the FASTA file to be read.

    Returns:
    -------
    pandas.DataFrame
        A DataFrame with two columns:
        - 'Identifier': The identifier of the sequence (string, without the '>' character).
        - 'Sequence': The corresponding sequence as a string.

    Raises:
    ------
    FileNotFoundError
        If the specified FASTA file cannot be found.
    ValueError
        If the file is empty or improperly formatted.

    Example:
    -------
    >>> read_fasta("example.fasta")
         Identifier       Sequence
    0    seq1            ATGCATGC
    1    seq2            GATTACA
    """
    data = {}

    try:
        with open(file_path, 'r') as file:
            identifier = None
            for line in file:
                line = line.strip()  # Remove any trailing newline characters
                if line.startswith('>'):
                    identifier = line[1:]  # Remove '>' and store the identifier
                    if identifier in data:
                        raise ValueError(f"Duplicate identifier found: {identifier}")
                    data[identifier] = ""  # Initialize the sequence
                else:
                    if identifier is None:
                        raise ValueError("Sequence found before identifier.")
                    data[identifier] += line  # Append the sequence for the identifier

    except FileNotFoundError as e:
        raise FileNotFoundError(f"FASTA file not found: {file_path}") from e

    if not data:
        raise ValueError("The FASTA file is empty or improperly formatted.")

    return pd.DataFrame(list(data.items()), columns=['Identifier', 'Sequence'])


def read_codon_dict():
    codon_dict = {}

    # Read the text file and process each line
    with open("rosalind/files/codon.txt", 'r') as file:

    # with open("/home/thbraet/rosalind/Bioinformatics Stronghold/functions/codon.txt", 'r') as file:
    # with open("/Workspace/Users/pmm203@fluvius.be/rosalind/Bioinformatics Stronghold/functions/codon.txt", 'r') as file:
        for line in file:
            # Split the line into codons and their corresponding amino acids
            codons = line.split()
            
            # There should be four pairs (codon, amino acid) per line
            for i in range(0, len(codons), 2):
                codon = codons[i]
                amino_acid = codons[i + 1]
                
                # Add the codon and its corresponding amino acid to the dictionary
                codon_dict[codon] = amino_acid
    return codon_dict

def read_monoisotopic_mass():
    protein_mass = {}

    # Read the text file and process each line
    with open("rosalind/files/monoisotopic_mass.txt", 'r') as file:
    # with open("/Workspace/Users/pmm203@fluvius.be/rosalind/Bioinformatics Stronghold/functions/monoisotopic_mass.txt", 'r') as file:

        for line in file:
            # Split the line into amino acids and their corresponding monoisotopic masses
            amino_acid, mass = line.split()
            
            # Add the amino acid and its corresponding mass to the dictionary
            protein_mass[amino_acid] = float(mass)
    return protein_mass