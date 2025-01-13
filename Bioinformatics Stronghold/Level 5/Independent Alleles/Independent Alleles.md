---
---

# Template Problem

## Read Sample Input and Output


```python
from rosalind.probability import phenotype_probability
from rosalind.read_files import read_text, write_text
from scipy.stats import binom
```


```python
sample_input = read_text('sample_input.txt')
print("Sample Input:\n", sample_input)

sample_output = read_text('sample_output.txt')
print("\nSample Output:\n",sample_output)
```

    Sample Input:
     2 1
    
    Sample Output:
     0.684


## Solve Sample Problem


```python
def solve_problem(input):
    k = int(input.split(' ')[0])
    N = int(input.split(' ')[1])

    total_offspring  = 2**k	
        
    p_AaBb = 1 / 4
    
    # Compute P(X >= N) as 1 - P(X < N)
    # P(X >= N) = 1 - binom.cdf(N-1, total_offspring, p_AaBb)
    probability = 1 - binom.cdf(N - 1, total_offspring, p_AaBb)
    
    return round(probability, 3)

```


```python
my_sample_output = solve_problem(sample_input)
my_sample_output
```




    np.float64(0.684)




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
     0.684





    True



## Run Real Input


```python
real_input = read_text('rosalind_lia.txt')

print_output(solve_problem(real_input), "my_rosalind_lia_output.txt");
```

    Output String:
     0.66

