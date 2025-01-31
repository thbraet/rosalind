---
---

# Pitfalls of reversing translation

When researchers discover a new protein, they would like to infer the strand of mRNA from which this protein could have been translated, thus allowing them to locate genes associated with this protein on the genome.

Unfortunately, although any RNA string can be translated into a unique protein string, reversing the process yields a huge number of possible RNA strings from a single protein string because most amino acids correspond to multiple RNA codons (see the RNA Codon Table).

Because of memory considerations, most data formats that are built into languages have upper bounds on how large an integer can be: in some versions of Python, an "int" variable may be required to be no larger than $2^{31}−1$, or 2,147,483,647. As a result, to deal with very large numbers in Rosalind, we need to devise a system that allows us to manipulate large numbers without actually having to store large numbers.

[Link to Rosalind](https://rosalind.info/problems/mrna/)

# Problem

For positive integers $a$ and $n$, $a$ modulo $n$ (written $a\ mod\ n$ in shorthand) is the remainder when $a$ is divided by $n$. For example, $29\ mod\ 11 = 7$ because $29 = 11 * 2 + 7$.

Modular arithmetic is the study of addition, subtraction, multiplication, and division with respect to the modulo operation. We say that $a$ and $b$  are congruent modulo $n$ if $a\ mod\ n = b\ mod\ n$; in this case, we use the notation $a≡b\ mod\ n$.

Two useful facts in modular arithmetic are that if $a ≡ b\ mod\ n$ and $c\ ≡\ d\ mod\ n$, then $a+c≡b+d\ mod\ n$ and $a*c≡b*d\ mod\ n$. To check your understanding of these rules, you may wish to verify these relationships for $a=29$, $b=73$, $c=10$, $d=32$, and $n=11$.

As you will see in this exercise, some Rosalind problems will ask for a (very large) integer solution modulo a smaller number to avoid the computational pitfalls that arise with storing such large numbers.

<span style="color:rgba(70,165,70,255); font-weight:bold">Given</span>: A protein string of length at most 1000 aa.

<span style="color:rgba(70,165,70,255); font-weight:bold">Return</span>: The total number of different RNA strings from which the protein could have been translated, modulo 1,000,000. (Don't neglect the importance of the stop codon in protein translation.)

# Read Example Input and Output Files


```python
%run ../../functions/read_files.ipynb
```


```python
input = read_text('sample_input.txt')
print(input)

output = read_text('sample_output.txt')
print(output)
```

    MA
    12


# Problem solving logic


```python

def get_possible_rna_sequences(input):
    protein_codon_freq = pd.DataFrame(codon_dict.items(), columns=['Codon', 'Amino Acid']).groupby('Amino Acid').count().to_dict().get('Codon')
    
    possible_sequences = 1
    for aa in input:
        possible_sequences *= protein_codon_freq.get(aa)
    possible_sequences *= 3 # 3 stop codons
    
    return possible_sequences % 1000000

get_possible_rna_sequences(input)
```




    12




```python
get_possible_rna_sequences(input) == int(output)
```




    True



# Run real input


```python
real_input = read_text('rosalind_mrna.txt')

get_possible_rna_sequences(real_input)
```




    956992


