import pandas as pd


def read_text(file_path):
    with open(file_path, "r") as file:
        return file.read().strip()
    

def write_text(file_path, text):
    with open(file_path, "w") as file:
        file.write(text)
        
        

def read_fasta(file_path):
    data = {}

    with open(file_path, 'r') as file:
        identifier = None
        for line in file:
            line = line.strip()  # Remove any trailing newline characters
            if line.startswith('>'):
                identifier = line[1:]  # Remove '>' and store the identifier
                data[identifier] = ""  # Initialize the sequence
            else:
                data[identifier] += line  # Append the sequence for the identifier

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