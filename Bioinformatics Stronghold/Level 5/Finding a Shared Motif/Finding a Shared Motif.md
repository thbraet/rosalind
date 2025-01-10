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
input = read_fasta('/Workspace/Users/pmm203@fluvius.be/rosalind/Bioinformatics Stronghold/Level 5/Finding a Shared Motif/sample_input.txt')
# input = read_fasta('sample_input.txt')
print(input)

output = read_text('/Workspace/Users/pmm203@fluvius.be/rosalind/Bioinformatics Stronghold/Level 5/Finding a Shared Motif/sample_output.txt')
# output = read_text('sample_output.txt')
print(output)
```

# Solution


```python
def find_common_substring(s1, s2):
    common_substrings = []

    for i in range(len(s1)):
        for j in range(i, len(s1)):
            # print(s1[i:j+1])
            if s1[i:j+1] in s2:
                # print(s1[i:j+1],"Yeey")
                common_substrings.append(s1[i:j+1])

    return list(set(common_substrings))

def find_lcs(input):
    input['length'] = input['Sequence'].str.len()
    input = input.sort_values(by='length', ascending=True).drop(columns=['length'])  # Sort and drop the helper column

    substring_list = find_common_substring(input.iloc[0,:]['Sequence'], input.iloc[1,:]['Sequence'])

    for dna_strand in input['Sequence']:

        substring_list = [x for x in substring_list if x in dna_strand]

    return sorted(substring_list, key=len, reverse=True)[0]


find_lcs(input)
```


```python
find_lcs(input) == output
```

# Submit solution


```python
real_input = read_fasta('/Workspace/Users/pmm203@fluvius.be/rosalind/Bioinformatics Stronghold/Level 5/Finding a Shared Motif/rosalind_lcsm.txt')

find_lcs(real_input)
```
