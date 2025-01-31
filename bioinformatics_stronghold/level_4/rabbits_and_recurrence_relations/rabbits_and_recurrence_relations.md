---
---

# Rabbits and Recurrence Relations

## Read Sample Input and Output


```python
from rosalind.combinatorics import fibonacci_rabbits
from rosalind.read_files import read_text, write_text, read_fasta
```


```python
sample_input = read_text('sample_input.txt')
print("Sample Input:\n", sample_input)

sample_output = read_text('sample_output.txt')
print("\nSample Output:\n",sample_output)
```

    Sample Input:
     5 3
    
    Sample Output:
     19


## Solve Sample Problem


```python
def solve_problem(input):
    n = int(input.split(' ')[0])
    k = int(input.split(' ')[1])
    total_rabbits = fibonacci_rabbits(n, k)
    return total_rabbits

```


```python
my_sample_output = solve_problem(sample_input)
my_sample_output
```




    19




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
     19





    True



## Run Real Input


```python
real_input = read_text('rosalind_fib.txt')

print_output(solve_problem(real_input), "my_rosalind_fib_output.txt");
```

    Output String:
     178956971

