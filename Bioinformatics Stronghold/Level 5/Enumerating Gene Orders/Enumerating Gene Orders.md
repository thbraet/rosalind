---
---

# INSERT TITEL

# Problem

Lorem Ipsum

<span style="color:rgba(70,165,70,255); font-weight:bold">Given</span>: ...

<span style="color:rgba(70,165,70,255); font-weight:bold">Return</span>: ...



# Read Files


```python
%run ../../functions/read_files
```


```python
input = read_text('/Workspace/Users/pmm203@fluvius.be/rosalind/Bioinformatics Stronghold/Level 5/Enumerating Gene Orders/sample_input.txt')
# input = read_text('sample_input.txt')
print(input)

output = read_text('/Workspace/Users/pmm203@fluvius.be/rosalind/Bioinformatics Stronghold/Level 5/Enumerating Gene Orders/sample_output.txt')
# output = read_text('sample_output.txt')
print(output)
```

# Solution


```python
from itertools import permutations
from math import factorial

def generate_permutations_and_count(n):
    numbers = list(range(1, n + 1))
    all_permutations = list(permutations(numbers))
    total_permutations = factorial(n)
    
    return all_permutations, total_permutations

sample_permutations, sample_count = generate_permutations_and_count(int(input))

print(sample_count)
for perm in sample_permutations:
    print(" ".join(map(str, perm)))

```


```python
generate_permutations_and_count(int(input)) == output
```

# Submit solution


```python
real_input = read_text('/Workspace/Users/pmm203@fluvius.be/rosalind/Bioinformatics Stronghold/Level 5/Enumerating Gene Orders/rosalind_perm.txt')
real_input
# function(real_input)
```


```python
real_permutations, real_count = generate_permutations_and_count(int(real_input))

print(f"Total permutations: {real_count}")
print("All permutations:")
for perm in real_permutations:
    print(" ".join(map(str, perm)))
```
