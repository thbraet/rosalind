---
---

# Finding a Motif in DNA

## Read Sample Input and Output


```python
from rosalind.string_algorithms import find_substring_positions
from rosalind.read_files import read_text, write_text, read_fasta
```


```python
sample_input = read_text('sample_input.txt')
print("Sample Input:\n", sample_input)

sample_output = read_text('sample_output.txt')
print("\nSample Output:\n",sample_output)
```

    Sample Input:
     GATATATGCATATACTT
    ATAT

    Sample Output:
     2 4 10


## Solve Sample Problem


```python
def solve_problem(input):
    parent_string = input.split('\n')[0]
    substring = input.split('\n')[1]
    positions = find_substring_positions(parent_string, substring)
    return positions

```


```python
my_sample_output = solve_problem(sample_input)
my_sample_output
```




    [2, 4, 10]




```python
def print_output(output, file_path = 'output.txt'):
    output_string = (" ".join(map(str, output)))

    write_text(output_string, file_path)

    print("Output String:\n",output_string)

    return output_string


```


```python
print_output(my_sample_output, "my_sample_output.txt") == sample_output
```

    Output String:
     2 4 10





    True



## Run Real Input


```python
real_input = read_text('rosalind_subs.txt')

print_output(solve_problem(real_input), "my_rosalind_subs_output.txt");
```

    Output String:
     64 82 97 140 197 222 229 236 251 258 287 294 359 423 438 455 491 671 678 919 926 971
