---
---

# INSERT TITEL

# Problem

Lorem Ipsum

<span style="color:rgba(70,165,70,255); font-weight:bold">Given</span>: ...

<span style="color:rgba(70,165,70,255); font-weight:bold">Return</span>: ...



# Read Files


```python
%run ../../functions/read_files.ipynb
```


```python
input = read_text('sample_input.txt')
print(input)

output = read_text('sample_output.txt')
print(output)
```

    21 7
    51200


# Solution


```python
import math

def get_partial_permutations(input):
    result = 1
    n = int(input.split()[0])
    k = int(input.split()[1])
    
    for i in range(n-k+1,n+1):
        result *= i
    
    return result % 1000000    
    
    # This doesn't work for large numbers    
    return int(math.factorial(n)/math.factorial(n-k)) % 1000000
    
get_partial_permutations(input)
```




    51200




```python
get_partial_permutations(input) == int(output)
```




    True



# Submit solution


```python
real_input = read_text('rosalind_pper.txt')

get_partial_permutations(real_input)
```




    596800




```python

```
