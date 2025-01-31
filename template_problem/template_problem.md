---
---

# Template Problem

## Read Sample Input and Output


```python
from rosalind.my_module import my_function
from rosalind.read_files import read_text, write_text
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
    return my_function(input)

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
real_input = read_text('rosalind_file.txt')

print_output(solve_problem(real_input), "my_rosalind_file_output.txt");
```

    Output String:
     522

