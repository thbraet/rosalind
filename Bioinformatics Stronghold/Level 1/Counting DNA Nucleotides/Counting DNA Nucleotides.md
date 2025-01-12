---
---

# Counting DNA Nucleotides

## Read Sample Input and Output


```python
from rosalind.string_algorithms import get_nucleotide_counts
from rosalind.read_files import read_text, write_text
```


```python
sample_input = read_text('sample_input.txt')
print("Sample Input:\n", sample_input)

sample_output = read_text('sample_output.txt')
print("\nSample Output:\n",sample_output)
```

    Sample Input:
     AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC

    Sample Output:
     20 12 17 21


## Solve Sample Problem


```python
my_sample_output = get_nucleotide_counts(sample_input)
my_sample_output
```




    {'A': 20, 'C': 12, 'G': 17, 'T': 21, 'U': 0}




```python
def print_output(output, file_path = 'output.txt'):
    output_string = f"{output["A"]} {output["C"]} {output["G"]} {output["T"]}"

    write_text(output_string, file_path)

    print("Output String:\n",output_string)

    return output_string


```


```python
print_output(my_sample_output, "my_sample_output.txt") == sample_output
```

    Output String:
     20 12 17 21





    True



# Run Real Input


```python
real_input = read_text('rosalind_dna.txt')
print_output(get_nucleotide_counts(real_input), "my_rosalind_dna_output.txt");
```

    Output String:
     211 209 237 221



```python

```
