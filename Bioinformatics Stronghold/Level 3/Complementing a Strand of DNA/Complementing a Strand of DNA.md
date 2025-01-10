---
---

# Complementing a Strand of DNA

## Read Sample Input and Output


```python
from rosalind.string_algorithms import get_complementary_dna_strand
from rosalind.read_files import read_text, write_text
```


```python
sample_input = read_text('sample_input.txt')
print("Sample Input:\n", sample_input)

sample_output = read_text('sample_output.txt')
print("\nSample Output:\n",sample_output)
```

    Sample Input:
     AAAACCCGGT
    
    Sample Output:
     ACCGGGTTTT


## Solve Sample Problem


```python
my_sample_output = get_complementary_dna_strand(sample_input)
my_sample_output
```




    'ACCGGGTTTT'




```python
def print_output(output, file_path = 'output.txt'):
    output_string = output
    
    write_text(output_string, file_path)
    
    print("Output String:\n",output_string)
        
    return output_string


```


```python
print_output(my_sample_output, "my_sample_output.txt") == sample_output
```

    Output String:
     ACCGGGTTTT





    True



## Run Real Input


```python
real_input = read_text('rosalind_revc.txt')
print_output(get_complementary_dna_strand(real_input), "my_rosalind_revc_output.txt");

```

    Output String:
     ACCATTGTTTAACGCATTGAAACTATGGTCTCTTCCCAAACGAAGTGCGGGTGGATCGCATGGGAATGAAAATAACAGGTAAAATGTCCCCGATGTATAAGATAGAGCGGACCCCCGCGGTTTCCCGTCCTCCTCTCATGACCTCTGTTTATACTTTAAAAACACACGAGAGGTTTTTAGATCAATCTGCGGTGCATCTCATAGCTGATTTCGCCAGATCCGAATTTGTAACTCAACAGATACTAGTTCATTCAGTGTAAAAACGGCTCTTACCAAAACGCATTGATACTATTTCTTGTACAAGGGCAAGTTGTGGAATATGATTTATGCTTATGCACAATATCTCTACGGTCCGTACTACCTCTTGGCTGTTTTGGGTATGTCTACATGTTGTTCGTTGTGTGCCAGGGACGATACTGATGAGAAGCGCCAAGTAAAGAAAGCAGTGAATATCTGCGAATTCCTGGTGCCGGGTCACTCGAGCGACCCGGGAGCACCCCTTCGGGCAAGAGAACTTTCGGGCTTAAGCAGAGTCTGCGTAACGGAGACCACCACCGTTAGGAGTCGTATATGGCTTCAATCCAAGTGACTGTGGTTAGATATTGTGGCAAACCGCCTGTTGCTCCAGCTCGACAGACCAAGGTTAACCAGGCTGTAAAATGTGCGTACTTATCTTCTTTTAAGAGCCAGACCCTATTGGGGGGGAGGGTTGCATCAGTAAACAGTGCTCCATCTTAACACACAATAAGAATGTCGATTCCACAATGCTGCCCAAATTGACACGTCTACGCACGGGATCAGCGGGCCTGCCCCCCGCTTCAAGTCGCGCTCCGCACGCCAGAACGGT

