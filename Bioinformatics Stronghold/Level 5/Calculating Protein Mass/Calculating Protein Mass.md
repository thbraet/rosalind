---
---

# Template Problem

## Read Sample Input and Output


```python
from rosalind.computational_mass_spectometry import protein_mass
from rosalind.read_files import read_text, write_text
```


```python
sample_input = read_text('sample_input.txt')
print("Sample Input:\n", sample_input)

sample_output = read_text('sample_output.txt')
print("\nSample Output:\n",sample_output)
```

    Sample Input:
     SKADYEK

    Sample Output:
     821.392


## Solve Sample Problem


```python
def solve_problem(input):
    return protein_mass(input, 3)

```


```python
my_sample_output = solve_problem(sample_input)
my_sample_output
```




    821.392




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
     821.392





    True



## Run Real Input


```python
real_input = read_text('rosalind_prtm.txt')



print_output(solve_problem(real_input), "my_rosalind_prtm_output.txt");
```

    Output String:
     103372.12



```python
%run ../../functions/read_files.ipynb
```


```python
input = read_text('sample_input.txt')
print(input)

output = read_text('sample_output.txt')
print(output)
```

    SKADYEK
    821.392


# Problem solving logic


```python
def calculate_weight(input):
    weight = 0
    for c in input:
        weight += monoisotopic_mass_dict[c]

    return weight

calculate_weight(input)
```




    821.3919199999999



# Run real input


```python
real_input = read_text('rosalind_prtm.txt')
calculate_weight(real_input)
```




    103372.12024000057
