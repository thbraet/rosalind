---
---

# Finding a Shared Motif

## Read Sample Input and Output


```python
from rosalind.string_algorithms import find_lcs, find_common_substring
from rosalind.read_files import read_text, write_text, read_fasta
```


```python
sample_input = read_fasta('sample_input.txt')
print("Sample Input:\n", sample_input)

sample_output = read_text('sample_output.txt')
print("\nSample Output:\n",sample_output)
```

    Sample Input:
        Identifier Sequence
    0  Rosalind_1  GATTACA
    1  Rosalind_2  TAGACCA
    2  Rosalind_3    ATACA
    
    Sample Output:
     AC


## Solve Sample Problem


```python
def solve_problem(input):
    dna_strings = input.Sequence
    return find_lcs(dna_strings)[0]
    # return my_function(input)

```


```python
my_sample_output = solve_problem(sample_input)
my_sample_output
```




    'AC'




```python
def print_output(output, file_path = 'output.txt'):
    output_string = str(output)
    
    write_text(output_string, file_path)
    
    print("Output String:\n",output_string)
        
    return output_string


```


```python
print_output(my_sample_output, "my_sample_output.txt") == sample_output
```

    Output String:
     AC





    True



## Run Real Input


```python
real_input = read_fasta('rosalind_lcsm.txt')

print_output(solve_problem(real_input), "my_rosalind_lcsm_output.txt");
```

    Output String:
     CGGATAGATGTGGCTGAACCACGACACCGAAGTTCTCAGCGGAGGAAGATATGAAAATGCATAGAAGGCTTACAGATCGGGGGTCGACGTTCGGTACTCGACACTCATCTTTGAAGTGTGTCAGCATGCTCGATGTTCTTCAAGCTGGGGCATAGCAGGGTAGTCCCGTCACCGCATATAAGGGATGTGGTCCCGCTGCGCATCCGACATTC

