---
---

# Mendels First Law

## Read Sample Input and Output


```python
from rosalind.probability import probability_dominant_offspring
from rosalind.read_files import read_text, write_text
```


```python
sample_input = read_text('sample_input.txt')
print("Sample Input:\n", sample_input)

sample_output = read_text('sample_output.txt')
print("\nSample Output:\n",sample_output)
```

    Sample Input:
     2 2 2
    
    Sample Output:
     0.78333


## Solve Sample Problem


```python
def solve_problem(input):
    k = int(input.split(' ')[0])
    m = int(input.split(' ')[1])
    n = int(input.split(' ')[2])
    prob = probability_dominant_offspring(k, m, n)
    return round(prob,5)

```


```python
my_sample_output = solve_problem(sample_input)
my_sample_output
```




    0.78333




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
     0.78333





    True



## Run Real Input


```python
real_input = read_text('rosalind_iprb.txt')

print_output(solve_problem(real_input), "my_rosalind_iprb_output.txt");
```

    Output String:
     0.72064

