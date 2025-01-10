---
---

# Calculating Expected Offspring

## Read Sample Input and Output


```python
from rosalind.probability import expected_dominant_offspring
from rosalind.read_files import read_text, write_text
```


```python
sample_input = read_text('sample_input.txt')
print("Sample Input:\n", sample_input)

sample_output = read_text('sample_output.txt')
print("\nSample Output:\n",sample_output)
```

    Sample Input:
     1 0 0 1 0 1
    
    Sample Output:
     3.5


## Solve Sample Problem


```python
def solve_problem(input):
    couples_AA_AA = int(input.split(" ")[0])
    couples_AA_Aa = int(input.split(" ")[1])
    couples_AA_aa = int(input.split(" ")[2])
    couples_Aa_Aa = int(input.split(" ")[3])
    couples_Aa_aa = int(input.split(" ")[4])
    couples_aa_aa = int(input.split(" ")[5])
    
    return expected_dominant_offspring(couples_AA_AA, couples_AA_Aa, couples_AA_aa, couples_Aa_Aa, couples_Aa_aa, couples_aa_aa, 2)

```


```python
my_sample_output = solve_problem(sample_input)
my_sample_output
```




    3.5




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
     3.5





    True



## Run Real Input


```python
real_input = read_text('rosalind_iev.txt')

print_output(solve_problem(real_input), "my_rosalind_iev_output.txt");
```

    Output String:
     159103.0



```python

```
