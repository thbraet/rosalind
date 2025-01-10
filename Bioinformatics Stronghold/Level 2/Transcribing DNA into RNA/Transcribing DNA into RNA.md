---
---

# Transcribing DNA into RNA


## Read Sample Input and Output


```python
from rosalind.read_files import read_text, write_text
from rosalind.string_algorithms import transcribe_dna_to_rna
```


```python
sample_input = read_text('sample_input.txt')
print("Sample Input:\n", sample_input)

sample_output = read_text('sample_output.txt')
print("\nSample Output:\n",sample_output)
```

    Sample Input:
     GATGGAACTTGACTACGTAAATT
    
    Sample Output:
     GAUGGAACUUGACUACGUAAAUU


## Solve Sample Problem


```python
my_sample_output = transcribe_dna_to_rna(sample_input)
my_sample_output
```




    'GAUGGAACUUGACUACGUAAAUU'




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
     GAUGGAACUUGACUACGUAAAUU





    True



# Run real input


```python
real_input = read_text('rosalind_rna.txt')
    
print_output(transcribe_dna_to_rna(real_input), "my_rosalind_rna_output.txt");


```

    Output String:
     UAAGUUUGUGGCGAUAAUGUGGCAGAUAUAACCGUGGCUACGAUUGGUAGCUCAGUGAAUUCGUCACUAUCCAUAAUACCCAAAGGUUCUUAUGAGAUACAUAAGUGCCAAUCCUCCAGAAUCAACUUACAUUUUGGAUGUUUAGAACUUACGCAGCGAGGGUGUCUCCACCGCCGCGAAGAACACGUGAUUCCGUGCCCCUUCGCGAAACGCCCAAGCUGCAGCUGGACCCGAAGCCCGCAAGGUCUAUGAAAACAGCAACCUUUUCCUGUCGGAUAUGCAUAGUCGGGACCAAGCGCUUAUGGGAGGGCGAACAUCACCGGGUCUCGUUCUAACGAGAGUCCGCGAGCGCUCGCUGAUAUCUACAUCACUUCUAAUCAGUAGGCCAAUAAGCGGGGAAGAGAUGUCAUCCAUCCUGUCCCUAGACCGCGUGCAGUCGCUGCUGUAGAGUAGUCGCCGUGCGAUUUGAAAGCAGCGCACUGAACGUUAUAUGGGCCUCUCAACGGAGGCAACUGGAGUUGGCUCCAAUGCGGUUCUCGAGCGCCUCUAGGUUUCUCAGAUCCAAAGCGUAGGUAUUCUGAGAUCCUUGUCAUCAUUGUGCGACCGUCAGUAGACAUUUCGUCUGCAACAGUGGAGACCGAACUAUCAGUGUGCAGGGGACGUUACACAGCUGGCUGUGCUAGUUCUUCCCUAAAGACACUUGCUCAGCGCCCACGACGCCGUGCGAGCGUGUAACAUACGAUGAAUCAUCCGUUGUCAUCGCGCUAACACUGCCAGGGUCCGAGAGGGCCGACGUCGUAAUAAUGUAGCUAUACGGUCUAAAUGGUCAUGGUUCACGAAUAGAAAGAGUGUCUGGUGUACUUGAUCACGCUCGCUAAAAAACACUACGAGUGAAAGUCGGCAUGAAGUCAUGGUCCAUAACUGUGGUUCCAAAAAUCCGCCCCUGUACACACAUAUCUGGAGGGGUUGUG



```python

```
