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

        Identifier                   Sequence
    0  Rosalind_24  TCAATGCATGCGGGTCTATATGCAT
    4 6
    5 4
    6 6
    7 4
    17 4
    18 4
    20 6
    21 4


# Solution


```python
def get_reverse_compliment(s):
    reverse = s[::-1]
    reverse_compliment = ''
    for i in reverse:
        if i == 'A':
            reverse_compliment += 'T'
        elif i == 'T':
            reverse_compliment += 'A'
        elif i == 'C':
            reverse_compliment += 'G'
        elif i == 'G':
            reverse_compliment += 'C'
    return reverse_compliment
```


```python
def locate_restriction_site(input):
    dna_strand = input['Sequence'].iloc[0]
    for i in range(len(dna_strand)):
        for j in range(i+4, min(i+13, len(dna_strand)+1)):
            if dna_strand[i:j] == get_reverse_compliment(dna_strand[i:j]):
                print(f"{i+1}\t{len(dna_strand[i:j])}")

locate_restriction_site(input)
```

    4	6
    5	4
    6	6
    7	4
    17	4
    18	4
    20	6
    21	4



```python
locate_restriction_site(input) == output
```

    4	6
    5	4
    6	6
    7	4
    17	4
    18	4
    20	6
    21	4





    False



# Submit solution


```python
real_input = read_fasta('rosalind_revp.txt')

locate_restriction_site(real_input)
```

    1	4
    54	8
    55	6
    56	4
    82	4
    93	6
    94	4
    122	4
    135	4
    138	4
    143	4
    145	4
    147	6
    148	4
    153	4
    192	4
    194	4
    223	4
    249	4
    306	6
    307	4
    359	4
    372	6
    373	4
    383	4
    437	4
    443	4
    449	4
    459	12
    460	4
    460	10
    461	8
    462	6
    463	4
    466	4
    472	4
    482	4
    523	4
    538	8
    539	6
    540	4
    559	4
    596	6
    597	4
    621	4
    625	6
    626	4
    650	10
    651	8
    652	6
    653	4
    684	4
    686	4
    690	4
    699	6
    700	4
    713	4
    725	4
    738	4
    747	4
    753	6
    754	4
    762	6
    763	4
    802	4
    814	6
    815	4
    846	4
    858	4
    866	4
    875	4
    920	4
    925	4



```python

```
