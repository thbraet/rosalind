---
---

# Transcription May Begin Anywhere

In [Transcribing DNA into RNA](../../Level%202/Transcribing%20DNA%20into%20RNA/Transcribing%20DNA%20into%20RNA.ipynb), we discussed the transcription of DNA into RNA, and in [Translating RNA into Protein](../../Level%204/Translating%20RNA%20into%20Protein/Transalting%20RNA%20into%20Protein.ipynb), we examined the translation of RNA into a chain of amino acids for the construction of proteins. We can view these two processes as a single step in which we directly translate a DNA string into a protein string, thus calling for a DNA codon table.

However, three immediate wrinkles of complexity arise when we try to pass directly from DNA to proteins. First, not all DNA will be transcribed into RNA: so-called junk DNA appears to have no practical purpose for cellular function. Second, we can begin translation at any position along a strand of RNA, meaning that any substring of a DNA string can serve as a template for translation, as long as it begins with a start codon, ends with a stop codon, and has no other stop codons in the middle. See Figure 1. As a result, the same RNA string can actually be translated in three different ways, depending on how we group triplets of symbols into codons. For example, ...AUGCUGAC... can be translated as ...AUGCUG..., ...UGCUGA..., and ...GCUGAC..., which will typically produce wildly different protein strings.

# Problem

Either strand of a DNA double helix can serve as the coding strand for RNA transcription. Hence, a given DNA string implies six total reading frames, or ways in which the same region of DNA can be translated into amino acids: three reading frames result from reading the string itself, whereas three more result from reading its reverse complement.

An open reading frame (ORF) is one which starts from the start codon and ends by stop codon, without any other stop codons in between. Thus, a candidate protein string is derived by translating an open reading frame into amino acids until a stop codon is reached.

<span style="color:rgba(70,165,70,255); font-weight:bold">Given</span>: A DNA string $s$ of length at most 1 kbp in FASTA format.

<span style="color:rgba(70,165,70,255); font-weight:bold">Return</span>: Every distinct candidate protein string that can be translated from ORFs of $s$. Strings can be returned in any order.

# Read Example Input and Output Files


```python
%run ../../functions/read_files.ipynb
```


```python
input = read_fasta('sample_input.txt')
print(input)

output = read_text('sample_output.txt')
print(output)
```

        Identifier                                           Sequence
    0  Rosalind_99  AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTG...
    MLLGSFRLIPKETLIQVAGSSPCNLS
    M
    MGMTPRLGLESLLE
    MTPRLGLESLLE


# Problem solving logic


```python
def get_input_dna(input):
    return input.Sequence.values[0]

def get_complimentary_dna_strand(template_dna_strand):
    # Define the replacement mappings
    replacements = {'T': 'A', 'A': 'T', 'C': 'G', 'G': 'C'}
    
    # Use a list comprehension to apply replacements and then join into a new string
    return ''.join(replacements.get(base, base) for base in template_dna_strand)[::-1]
    

def transcribe_dna_to_rna(template_dna_strand):
    # Define the replacement mappings
    replacements = {'T': 'A', 'A': 'U', 'C': 'G', 'G': 'C'}
    
    # Use a list comprehension to apply replacements and then join into a new string
    return ''.join(replacements.get(base, base) for base in template_dna_strand)[::-1]

```


```python
def get_all_start_codon_indexes(rna):
    indexes = []
    start = 0
    while True:
        index = rna.find('AUG', start)
        if index == -1:
            break
        indexes.append(index)
        start = index + 1  # Move past the last found index
    return indexes

```


```python
def split_into_codons(rna):
    return [rna[i:i+3] for i in range(0, len(rna), 3)]
```


```python
def find_first_stop_codon_index(codon_list):
    # Define the stop codons
    stop_codons = ['UAA', 'UAG', 'UGA']
    
    # Loop through the list to find the first stop codon
    for index, codon in enumerate(codon_list):
        if codon in stop_codons:
            return index  # Return the index of the first stop codon
    
    # If no stop codon is found, return -1
    return -1

```


```python
def translate_rna_to_protein(codons):    
    # Translate each codon into an amino acid
    protein = ''
    for codon in codons:
        protein += codon_dict[codon]
    
    return protein
```


```python
def get_open_reading_frame(input):
    protein_list = []
    
    input_dna = get_input_dna(input)
    complimentary_dna = get_complimentary_dna_strand(input_dna)
    
    input_rna = transcribe_dna_to_rna(input_dna)
    complimentary_rna = transcribe_dna_to_rna(complimentary_dna)
    
    start_codon_indexes = get_all_start_codon_indexes(input_rna)
    complimentary_start_codon_indexes = get_all_start_codon_indexes(complimentary_rna)
    
    for i in start_codon_indexes:
        codon_list = split_into_codons(input_rna[i:])
        stop_index = find_first_stop_codon_index(codon_list)
        if stop_index != -1:
            protein_list.append(translate_rna_to_protein(codon_list[:stop_index]))
        
    for i in complimentary_start_codon_indexes:
        codon_list = split_into_codons(complimentary_rna[i:])
        stop_index = find_first_stop_codon_index(codon_list)
        if stop_index != -1:
            protein_list.append(translate_rna_to_protein(codon_list[:stop_index]))

    return set(protein_list)
    

get_open_reading_frame(input)
```




    {'M', 'MGMTPRLGLESLLE', 'MLLGSFRLIPKETLIQVAGSSPCNLS', 'MTPRLGLESLLE'}




```python
get_open_reading_frame(input) == set(output.split('\n'))
```




    True



# Run real input


```python
real_input = read_fasta('rosalind_orf.txt')
print(real_input)
```

          Identifier                                           Sequence
    0  Rosalind_3517  GTGATCGGCGGCTCAATCCATCGTACACGCGTTAACTTGGTCGACT...



```python
with open("open_reading_frames.txt", "w") as file:
    for p in get_open_reading_frame(real_input):
        file.write(p + "\n")  # Write each open reading frame on a new line

```
