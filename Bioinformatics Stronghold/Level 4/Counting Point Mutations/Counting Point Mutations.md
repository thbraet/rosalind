---
---

# Counting Point Mutations

## Read Sample Input and Output


```python
from rosalind.alignment import get_hamming_distance
from rosalind.read_files import read_text, write_text, read_fasta
```


```python
sample_input = read_text('sample_input.txt')
print("Sample Input:\n", sample_input)

sample_output = read_text('sample_output.txt')
print("\nSample Output:\n",sample_output)
```

    Sample Input:
     GAGCCTACTAACGGGAT
    CATCGTAATGACGGCCT
    
    Sample Output:
     7


## Solve Sample Problem


```python
def solve_problem(input):
    str1 = input.split('\n')[0]
    str2 = input.split('\n')[1]
    hamming_distance = get_hamming_distance(str1, str2)
    return hamming_distance

```


```python
my_sample_output = solve_problem(sample_input)
my_sample_output
```




    7




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
     7





    True



## Run Real Input


```python
real_input = read_text('rosalind_hamm.txt')

print_output(solve_problem(real_input), "my_rosalind_hamm_output.txt");
```

    Output String:
     522

