---
---

# Consensus and Profile

## Read Sample Input and Output


```python
from rosalind.string_algorithms import get_consensus_string, get_profile_matrix
from rosalind.read_files import read_text, write_text, read_fasta
import pandas as pd
```


```python
sample_input = read_fasta('sample_input.txt')
print("Sample Input:\n", sample_input)

sample_output = read_text('sample_output.txt')+ "\n"
print("\nSample Output:\n",sample_output)
```

    Sample Input:
        Identifier  Sequence
    0  Rosalind_1  ATCCAGCT
    1  Rosalind_2  GGGCAACT
    2  Rosalind_3  ATGGATCT
    3  Rosalind_4  AAGCAACC
    4  Rosalind_5  TTGGAACT
    5  Rosalind_6  ATGCCATT
    6  Rosalind_7  ATGGCACT
    
    Sample Output:
     ATGCAACT
    A: 5 1 0 0 5 5 0 0
    C: 0 0 1 4 2 0 6 1
    G: 1 1 6 3 0 1 0 0
    T: 1 5 0 0 0 1 1 6
    


## Solve Sample Problem


```python
def solve_problem(input):
    dna_list = pd.DataFrame(input.Sequence.apply(list).tolist())
    consensus_string = get_consensus_string(dna_list)
    profile_matrix = get_profile_matrix(dna_list)
    
    return consensus_string, profile_matrix
        # dna_strings_to_df = pd.DataFrame(df_fasta.Sequence.apply(list).tolist())

```


```python
my_sample_output = solve_problem(sample_input)
my_sample_output
```




    ('ATGCAACT',
        0  1  2  3  4  5  6  7
     A  5  1  0  0  5  5  0  0
     C  0  0  1  4  2  0  6  1
     G  1  1  6  3  0  1  0  0
     T  1  5  0  0  0  1  1  6)




```python
def print_output(output, file_path = 'output.txt'):
    # Write to a text file
    with open(file_path, 'w') as file:
        file.write(output[0])
        file.write('\n')

        
        for nucleotide, row in output[1].iterrows():
            formatted_row = f"{nucleotide}: " + " ".join(map(str, row))
            file.write(formatted_row + '\n')
    # output_string = str(output)
    
    with open(file_path, 'r') as file:
        output_string = file.read()
    
    # write_text(output_string, file_path)
    
    print("Output String:\n",output_string)
        
    return output_string


```


```python
print_output(my_sample_output, "my_sample_output.txt") == sample_output
```

    Output String:
     ATGCAACT
    A: 5 1 0 0 5 5 0 0
    C: 0 0 1 4 2 0 6 1
    G: 1 1 6 3 0 1 0 0
    T: 1 5 0 0 0 1 1 6
    





    True



## Run Real Input


```python
real_input = read_fasta('rosalind_cons (1).txt')

print_output(solve_problem(real_input), "my_rosalind_cons_output.txt");
```

    Output String:
     GTAAACCTAGCAGATGGGTCGCGGCGGTCCTGGAGGACCCTTAACCCCGAGGGTAATAGCAGCAGACAATCCAAAGGCACGCAGTTAAAGAGATCTGAGACCATACCTCGAGGGATGACGCAGTCAATACCCTATCCCCCTGGCCGCCTATACTGCGGCAGTTTGGCGTAAATACTGACAAATGTTCAACCTTAAAACGGCTAACAAGACAAATGCTATCATACACGACAAAAGCAGAACATACCCACCCAAAAAAAGAGCGTGCCATATGCTATCGCTCTGCCATCCCCCCAATCCAGCACGCATTATCTGTTCTGGGTTAATACGACCCACGGAGTAAACAACGAGTTTGGCTTGCGAAGAGACGCTTGGTACCTTAATTATGACCCCAAAGGGCGCGAGGAGAAGCGAAATTACACACAGACACCAGAAAGGTATACGTAGAAACGCCGAAGAAAGAACATAATAACTCCCATCCAGCATGACAAAATCTCGTAAAAACGATGGAATCCGTAATCGAGACAGGTACGAGCTTAGTTTGCACGTCATGTGGACGACTGGGTCATGACCTACCTAACATGGGATGCGCAGAACATCGAGTGCTAAGGCGATCCACGACGGTAAAAGACGATAGCAAAGAACGCTTAGTTCGGCGCCCTGTGACGAGCCATCGAGCGTCTCGTGAAAACTAGAGGGCGGGAGAGTTCCAAAGAGACAATAGAGGGCACTATCCCCGAAAACGGGCTCGAGTGAAACGTCAGTCGTGCTCTCTCGTCCGCTCAGCTCAATGCTGACGCACAGAATATACAACGAGCGCGTCATTGGATCAGACGGAGCTCCATCCCAACAGTATAACCAGACGACGGCGCCGGTACAAAAATTTAATTCACCCTACCTACGCAATATTTATAGCCCCGCGGCCCGAAATCACCAAATAGAACAGAATCGTGAGGAACGACCAAATGCCTACACCGTAACTTA
    A: 1 1 5 3 3 2 2 3 3 0 2 4 2 3 2 0 3 3 2 2 3 2 2 2 1 3 2 1 2 2 1 1 1 4 3 1 5 2 1 3 3 2 6 3 1 1 2 2 0 3 2 1 3 1 3 3 2 5 2 1 3 0 2 4 3 4 3 5 3 3 2 2 4 3 6 3 3 1 5 1 2 2 5 2 3 2 5 4 3 2 3 2 3 3 2 0 2 4 1 3 2 0 4 2 3 1 2 3 2 1 4 0 1 1 3 2 4 4 2 1 2 3 1 2 3 3 3 1 3 2 2 2 3 3 3 1 2 1 2 2 4 2 1 2 3 1 1 1 3 5 1 4 1 1 3 1 2 3 2 4 1 3 1 2 0 3 0 2 2 5 3 3 3 3 1 2 3 3 2 4 4 4 0 2 2 0 2 4 4 2 2 2 2 3 5 3 4 2 2 1 1 1 4 4 2 3 6 1 3 1 4 4 3 1 3 3 2 5 2 2 3 0 6 1 5 2 0 3 3 3 3 3 4 3 1 5 1 5 3 0 3 2 3 1 3 1 4 2 2 1 5 3 4 3 3 3 5 3 3 2 2 2 2 3 1 3 4 2 4 2 0 2 2 5 3 2 0 2 0 1 2 2 2 1 4 1 2 3 2 3 1 1 4 5 2 3 4 4 1 2 3 2 2 2 3 3 1 3 2 3 2 1 3 2 0 3 1 1 2 1 2 3 4 4 3 2 1 5 2 0 2 4 0 2 3 3 1 1 4 4 5 1 3 4 0 1 3 2 1 1 1 1 3 2 1 2 2 2 3 4 3 1 4 2 3 1 1 2 1 3 2 2 3 4 2 4 1 2 5 4 2 2 4 0 2 4 2 1 1 2 5 3 4 2 2 1 3 3 2 3 4 3 2 3 2 5 3 2 3 1 4 3 3 1 3 4 2 3 2 3 2 4 2 6 3 3 1 2 4 2 4 5 3 1 1 3 6 1 3 3 1 1 4 1 3 3 4 2 1 2 1 2 4 5 2 4 3 4 2 4 4 2 4 2 3 3 2 7 4 4 3 1 2 4 3 3 3 2 4 2 2 4 3 3 3 2 5 5 3 3 2 1 1 1 3 3 5 3 4 4 5 2 2 3 2 1 0 5 4 3 2 1 2 2 4 3 2 2 3 4 2 3 1 4 0 2 1 5 1 3 3 3 2 2 3 4 2 3 1 1 1 0 3 0 2 1 2 4 3 2 3 2 2 5 3 2 3 1 2 3 2 2 2 1 4 0 2 4 1 2 3 4 2 0 0 3 4 2 4 0 2 0 3 4 2 2 0 1 2 3 1 3 3 2 7 0 3 2 5 2 1 3 2 3 4 3 2 1 1 3 4 2 1 2 5 1 0 3 2 2 1 3 3 6 5 3 0 4 2 0 4 3 4 3 0 4 4 4 3 4 3 2 3 2 0 3 3 3 3 2 3 2 0 2 2 3 2 2 2 2 2 4 6 1 2 5 3 1 1 3 3 1 2 3 3 2 2 2 1 0 2 2 3 3 3 5 4 5 2 3 3 2 5 0 3 1 3 2 2 3 3 2 3 2 2 2 2 0 5 4 3 2 4 2 4 2 5 3 2 5 1 4 3 1 3 2 3 3 3 5 3 2 2 2 2 1 3 4 4 3 2 0 2 1 2 3 2 3 5 1 1 2 4 3 4 0 2 1 2 4 3 2 2 2 1 0 2 1 2 1 2 1 2 2 3 2 2 2 2 0 2 5 3 1 1 3 4 4 2 1 2 1 1 3 2 2 2 4 1 4 2 5 3 2 4 2 3 2 3 4 2 1 4 2 2 3 1 2 1 1 3 2 2 2 1 3 3 3 3 1 4 2 2 1 4 2 1 2 3 1 3 3 1 2 2 3 3 2 3 3 1 3 1 4 4 2 1 3 2 4 1 2 4 3 2 2 3 3 1 2 2 2 1 3 3 3 4 5 5 4 2 0 1 3 3 2 0 1 4 1 1 3 2 5 2 2 1 5 1 2 0 3 3 2 5 1 1 2 4 2 4 2 1 3 2 2 0 3 0 1 2 1 2 2 5 4 4 3 1 4 1 3 3 4 4 3 3 3 4 3 0 5 2 6 5 2 2 2 3 3 6 3 1 4 5 1 2 4 1 2 5 4 3 2 1 1 1 2 3 1 3 2 2 1 1 3 5 2 1 1 3
    C: 2 1 2 2 2 5 3 2 3 3 3 2 2 3 2 3 2 1 2 4 0 5 2 3 5 1 2 3 4 3 3 2 2 2 3 1 1 4 4 4 2 2 0 3 4 4 3 5 1 2 3 0 3 3 3 2 3 0 1 4 2 2 3 2 1 1 4 1 3 2 3 4 3 3 2 1 0 4 0 3 2 3 2 3 1 1 1 2 3 2 1 0 3 1 4 2 1 2 2 2 3 4 2 2 3 3 6 2 3 0 2 2 2 3 2 2 0 1 4 1 4 3 2 2 4 2 1 1 1 4 3 5 2 3 2 3 3 4 6 3 1 3 2 4 4 1 6 5 1 0 3 0 4 2 1 4 3 2 5 1 0 3 3 2 2 1 4 3 1 1 2 2 2 2 4 1 1 2 3 2 2 0 3 2 1 1 5 3 0 4 4 2 2 3 2 2 2 4 1 1 6 2 3 3 3 2 2 2 2 5 0 3 2 2 2 4 2 1 3 4 1 1 2 3 3 4 3 3 4 3 2 2 3 1 4 1 2 2 3 6 3 1 3 6 6 4 2 3 3 5 2 3 2 3 3 2 3 1 2 2 4 3 1 0 3 4 2 1 4 3 3 3 1 3 1 5 3 6 2 5 3 1 4 4 1 3 4 4 5 4 5 5 2 3 3 5 5 1 0 5 2 4 3 3 3 0 2 3 2 5 3 0 3 2 4 1 3 1 1 2 3 2 3 1 3 5 3 1 5 5 5 4 5 1 1 2 2 3 0 3 1 4 2 3 4 3 1 2 2 2 3 2 3 5 3 3 3 3 2 1 2 1 2 1 2 3 3 4 1 2 2 2 2 1 5 5 2 1 2 0 3 2 2 3 1 3 3 4 5 3 1 3 1 2 2 2 4 1 3 2 1 3 2 3 2 4 3 2 4 2 2 2 3 3 2 3 4 3 4 2 4 4 0 2 4 3 6 4 0 2 1 0 3 2 2 1 0 2 3 5 2 2 2 2 1 1 3 4 3 5 4 1 1 1 1 1 3 3 2 2 1 4 1 1 3 2 3 0 0 5 0 3 6 5 1 3 5 4 1 1 5 3 3 2 2 4 4 2 2 1 3 4 2 3 2 1 1 3 2 2 1 4 1 2 2 1 2 1 2 1 3 5 1 0 1 3 1 3 0 3 2 1 5 1 3 2 3 1 4 0 2 2 4 1 1 3 2 0 3 3 3 5 3 5 2 3 7 3 0 0 2 2 1 4 5 3 3 6 3 1 1 2 2 4 1 1 2 3 3 3 1 3 3 4 3 3 2 3 1 1 2 0 0 3 2 2 4 2 4 1 1 3 3 4 1 3 4 1 2 2 2 2 3 2 3 1 2 2 4 1 2 2 4 3 3 5 3 2 3 0 3 1 3 2 2 2 3 1 4 3 3 3 1 1 5 1 1 2 2 1 1 4 2 5 0 2 2 3 1 1 5 2 4 4 2 4 4 6 3 1 3 0 0 5 3 1 1 4 4 2 1 6 2 2 0 4 2 3 4 3 5 0 1 3 2 1 1 2 5 2 3 1 1 2 0 3 4 2 0 1 1 2 3 2 1 2 3 5 2 2 2 3 0 0 2 4 1 3 2 1 2 4 1 1 0 7 2 4 1 1 1 3 5 6 4 1 2 3 0 3 3 4 2 1 5 0 3 1 3 3 2 2 2 2 2 5 2 2 3 2 3 1 4 2 2 3 3 3 3 3 3 2 4 1 3 4 4 1 4 3 3 2 1 7 2 5 4 2 3 1 4 3 2 3 4 2 3 2 3 2 2 2 3 1 0 2 1 3 3 2 6 2 3 2 3 3 4 2 3 4 2 2 1 3 3 2 1 5 3 1 1 4 3 1 0 0 4 3 4 3 2 1 4 3 4 1 3 3 3 1 1 3 2 3 3 4 6 1 2 2 6 0 0 4 2 2 4 2 4 3 2 2 3 3 5 2 2 0 0 3 2 1 2 2 2 3 3 4 4 4 4 5 2 3 6 3 1 2 4 1 7 3 1 1 2 2 2 3 0 3 3 2 3 4 6 6 2 4 2 3 5 4 3 0 1 2 2 1 3 4 5 5 1 1 2 3 3 1 3 3 4 4 3 4 0 1 4 1 2 1 1 3 1 3 2 4 1 2 3 4 0 1 3 3 3 4 6 0 2 5 3 6 4 1 2 3 3 3 2 3 3
    G: 5 3 2 3 2 1 3 1 1 4 2 4 3 1 2 5 4 4 2 1 4 1 3 4 2 4 5 1 2 2 2 4 4 1 4 5 1 3 1 2 0 2 1 2 4 4 3 0 6 3 4 5 4 2 1 3 0 3 4 3 2 4 3 3 4 4 3 3 2 1 3 1 2 2 0 5 4 1 4 3 4 2 2 4 2 3 2 1 1 3 3 5 3 2 2 3 5 2 5 2 2 4 3 2 1 3 2 0 2 5 3 4 4 4 2 1 5 1 2 5 2 1 5 2 2 3 3 2 3 2 2 0 0 3 1 3 3 2 0 3 0 4 5 1 1 5 2 3 2 3 1 4 2 2 4 4 4 5 3 4 5 0 2 1 4 4 4 5 2 2 3 3 0 2 2 3 6 2 2 2 0 4 3 4 3 2 2 1 4 3 1 1 2 3 0 2 2 1 4 4 0 2 3 0 2 3 1 5 2 1 3 2 3 3 4 1 2 0 1 1 3 2 0 3 2 1 5 2 1 2 2 2 2 5 2 3 4 1 1 2 3 3 2 2 1 2 2 3 3 3 2 1 1 2 2 3 1 4 2 3 2 4 3 5 3 1 1 3 1 1 5 3 3 0 2 2 4 1 3 2 0 6 0 3 1 1 0 0 1 2 1 1 1 0 0 2 0 3 5 2 3 2 4 3 2 3 3 2 2 2 1 5 0 2 3 2 4 4 4 1 1 2 1 0 3 1 5 4 2 4 0 1 2 6 4 3 5 2 3 2 3 4 2 1 4 4 3 5 2 2 2 4 4 3 2 1 4 2 5 1 3 4 1 4 2 3 4 0 3 1 4 5 1 2 3 0 3 3 2 3 1 1 0 3 4 2 3 4 1 3 4 2 3 4 3 4 2 4 2 4 4 4 4 2 4 0 2 5 2 5 3 3 2 2 1 2 1 2 1 3 3 2 5 2 2 2 3 2 3 3 4 2 1 4 5 1 1 1 3 1 5 3 3 4 3 3 1 3 4 2 2 5 2 2 4 2 2 3 3 1 4 2 1 3 3 3 0 1 2 0 1 3 1 0 3 0 1 1 2 4 1 1 0 4 3 1 1 3 2 3 1 4 3 3 4 2 3 1 2 1 2 3 6 3 1 6 6 3 3 2 2 2 4 3 4 2 3 2 4 2 4 3 2 3 4 3 2 1 3 4 3 4 0 1 2 1 3 3 1 2 4 2 3 3 3 2 0 2 2 4 0 3 5 0 1 4 3 0 1 5 4 4 1 2 3 2 4 1 3 2 2 1 3 3 2 2 2 2 1 4 3 7 4 1 1 4 2 4 1 3 4 3 2 2 1 1 2 4 0 5 3 4 3 1 1 3 4 4 2 4 3 1 4 2 2 3 4 2 2 4 4 2 2 1 2 2 4 3 3 4 3 0 2 4 3 3 4 0 4 4 3 2 5 2 4 1 2 4 0 3 1 5 5 3 4 1 1 0 1 4 1 5 2 2 4 2 6 3 1 3 2 1 3 3 5 0 4 1 2 3 3 5 2 4 3 3 3 1 2 1 2 5 1 6 5 4 0 3 4 5 3 4 1 3 3 1 3 2 1 4 3 4 4 5 3 2 3 3 1 3 5 1 4 4 4 1 2 2 1 1 1 2 2 1 3 6 2 3 3 2 2 6 4 4 2 3 2 4 2 5 2 4 2 2 2 4 4 3 3 2 4 3 2 4 3 5 3 2 2 1 3 3 2 4 0 1 1 5 2 3 3 0 4 1 2 1 0 1 1 5 3 2 4 2 2 5 2 1 3 1 5 1 2 3 2 2 3 2 2 4 1 4 1 4 2 4 4 6 2 2 3 1 3 4 4 2 2 1 2 4 2 2 4 4 4 5 3 1 1 3 2 2 2 2 1 3 1 2 2 4 2 2 3 1 3 1 2 3 3 3 2 4 3 3 4 5 1 4 2 3 5 4 1 2 1 3 1 2 2 3 2 3 1 2 3 0 0 2 0 4 2 1 1 1 0 3 0 1 2 6 0 3 3 3 0 1 2 1 4 0 1 3 3 1 0 1 6 2 6 6 2 3 2 6 3 3 2 2 3 1 0 1 3 1 4 0 2 5 2 2 4 0 4 0 3 3 1 4 1 6 1 4 5 3 1 4 5 1 3 1 2 1 3 1 4 4 1 2 3 1 2 0 0 4 2 1 0 3 2 1 1
    T: 2 5 1 2 3 2 2 4 3 3 3 0 3 3 4 2 1 2 4 3 3 2 3 1 2 2 1 5 2 3 4 3 3 3 0 3 3 1 4 1 5 4 3 2 1 1 2 3 3 2 1 4 0 4 3 2 5 2 3 2 3 4 2 1 2 1 0 1 2 4 2 3 1 2 2 1 3 4 1 3 2 3 1 1 4 4 2 3 3 3 3 3 1 4 2 5 2 2 2 3 3 2 1 4 3 3 0 5 3 4 1 4 3 2 3 5 1 4 2 3 2 3 2 4 1 2 3 6 3 2 3 3 5 1 4 3 2 3 2 2 5 1 2 3 2 3 1 1 4 2 5 2 3 5 2 1 1 0 0 1 4 4 4 5 4 2 2 0 5 2 2 2 5 3 3 4 0 3 3 2 4 2 4 2 4 7 1 2 2 1 3 5 4 1 3 3 2 3 3 4 3 5 0 3 3 2 1 2 3 3 3 1 2 4 1 2 4 4 4 3 3 7 2 3 0 3 2 2 2 2 3 3 1 1 3 1 3 2 3 2 1 4 2 1 0 3 2 2 2 1 1 3 3 2 2 2 1 2 3 3 2 1 4 2 3 2 3 4 1 4 2 2 4 2 4 1 3 1 5 2 5 1 4 2 4 5 4 3 2 1 3 3 3 2 5 0 1 2 4 1 2 2 1 2 2 4 4 2 4 0 4 4 4 4 3 4 2 4 3 6 4 3 2 5 1 2 1 0 1 1 3 1 3 1 2 2 2 4 3 1 1 1 3 2 2 2 3 1 5 5 4 3 0 0 4 4 1 3 0 4 2 4 3 3 3 3 2 4 5 4 2 1 4 3 0 1 4 4 1 3 4 5 4 4 3 1 2 1 3 2 0 2 2 2 3 3 1 2 3 1 1 0 2 2 2 1 2 1 1 2 1 2 2 4 4 1 3 2 3 2 1 0 3 0 1 2 0 2 3 3 1 3 3 3 2 5 3 6 1 1 2 4 1 3 3 3 2 1 2 1 3 2 3 2 3 3 2 0 3 3 1 2 4 4 1 2 5 2 4 1 6 3 1 1 3 4 1 3 3 3 2 2 4 1 2 3 0 0 3 3 4 1 4 3 1 4 1 3 2 3 2 1 1 2 5 2 2 1 1 4 3 2 3 5 1 2 4 3 3 1 2 3 2 2 3 3 4 3 2 3 2 1 4 6 4 2 3 4 5 4 2 3 1 2 3 4 1 1 5 4 5 3 2 1 1 1 1 3 4 1 3 2 5 3 2 7 2 2 3 3 4 2 2 3 5 2 2 3 4 5 3 3 3 2 5 2 4 3 3 3 4 1 2 2 1 6 1 3 3 1 4 1 2 4 2 3 2 3 3 2 1 5 1 3 0 1 3 3 3 4 2 4 2 1 1 3 3 2 1 3 0 4 3 2 2 2 1 4 1 1 3 2 0 1 6 4 3 0 6 4 1 1 1 1 2 2 3 2 4 3 4 1 2 2 1 2 0 2 4 2 4 2 3 2 2 4 2 4 3 4 0 3 4 0 2 1 2 2 1 4 2 2 3 2 2 2 3 3 4 1 3 2 3 3 4 5 2 3 2 0 2 1 2 3 1 2 1 1 5 1 2 1 2 4 3 0 3 1 5 3 5 3 1 1 1 2 3 0 3 2 3 0 2 4 1 4 3 2 0 1 5 2 2 3 2 1 2 4 2 2 0 4 2 2 4 2 2 4 3 5 2 4 2 3 4 3 3 2 2 4 2 3 2 1 5 1 2 3 4 3 1 4 3 2 2 1 3 3 3 3 1 2 2 4 4 4 3 3 2 0 1 3 2 2 3 0 1 0 4 3 2 5 4 1 2 3 4 1 2 4 3 2 1 4 2 3 2 4 2 3 3 4 3 3 3 3 3 3 2 2 6 2 4 2 0 3 1 3 3 1 1 4 3 0 2 1 2 1 3 2 1 2 5 2 1 2 3 3 3 0 4 6 6 3 2 5 7 3 2 1 3 1 5 1 2 2 8 2 3 1 3 1 3 4 3 6 5 4 2 5 2 3 3 2 2 1 2 1 2 0 1 2 3 2 1 1 2 4 3 1 4 1 3 4 0 4 2 1 1 2 2 1 1 0 2 4 3 3 4 0 2 0 3 0 2 1 2 3 3 3 3 4 1 4 2 1 2 6 2 3 2 2 4 4 5 3 2 2 5 5 3
    


## Solution


```python
def get_consensus_and_profile_matrix(input_path = './sample_input.txt', output_path = 'nucleotide_frequencies.txt' ):
    
    dna_strings = read_fasta(input_path)
        
    dna_strings_to_df = pd.DataFrame(dna_strings.Sequence.apply(list).tolist())

    freq_df = pd.DataFrame(
            ((dna_strings_to_df == 'A').sum().values,
            (dna_strings_to_df == 'C').sum().values,
            (dna_strings_to_df == 'G').sum().values,
            (dna_strings_to_df == 'T').sum().values), index=['A', 'C', 'G', 'T'])




    # Write to a text file
    with open(output_path, 'w') as file:
        file.write(''.join(freq_df.idxmax().values) + '\n')

        
        for nucleotide, row in freq_df.iterrows():
            formatted_row = f"{nucleotide}: " + " ".join(map(str, row))
            file.write(formatted_row + '\n')

    print("Output written to nucleotide_frequencies.txt")
```


```python
get_consensus_and_profile_matrix()
```

    Output written to nucleotide_frequencies.txt


## Submit problem


```python
get_consensus_and_profile_matrix(input_path = './rosalind_cons.txt', output_path = 'nucleotide_frequencies_submission.txt')
```

    Output written to nucleotide_frequencies.txt

