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
input = read_fasta('sample_input.txt')
print(input)

output = read_text('sample_output.txt')
print(output)
```

        Identifier    Sequence
    0  Rosalind_23  AGCUAGUCAU
    12


# Solution


```python
import math

def get_perfect_matchings(input):
    rna_strand = input.Sequence[0]
    print(rna_strand)

    count_A = rna_strand.count('A')
    count_U = rna_strand.count('U')
    count_C = rna_strand.count('C')
    count_G = rna_strand.count('G')

    if count_A != count_U or count_C != count_G:
        print("Invalid String, no perfect matching possible")
        return 0

    return math.factorial(count_A) * math.factorial(count_C)


get_perfect_matchings(input)
```

    AGCUAGUCAU





    12




```python
get_perfect_matchings(input) == int(output)
```

    AGCUAGUCAU





    True



# Submit solution


```python
real_input = read_fasta('rosalind_pmch.txt')

get_perfect_matchings(real_input)
```

    GCCGCAAUGGGAACACCCGCGGGGCCGGACGUGCCCUCCUAUUCUAAUUUGCGUAGUUGACAUGCUCGAGACAUGA





    23517231061249970679935139840000000




```python

```
