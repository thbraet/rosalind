---
---

# The Need for Averages
Averages arise everywhere. In sports, we want to project the average number of games that a team is expected to win; in gambling, we want to project the average losses incurred playing blackjack; in business, companies want to calculate their average expected sales for the next quarter.

Molecular biology is not immune from the need for averages. Researchers need to predict the expected number of antibiotic-resistant pathogenic bacteria in a future outbreak, estimate the predicted number of locations in the genome that will match a given motif, and study the distribution of alleles throughout an evolving population. In this problem, we will begin discussing the third issue; first, we need to have a better understanding of what it means to average a random process.

[Link to Rosalind](https://rosalind.info/problems/iev/)

# Problem
For a random variable $X$ taking integer values between 1 and $n$, the expected value of $X$ is $E(X)=\sum_{k=1}^{n}k*Pr(X=k)$. The expected value offers us a way of taking the long-term average of a random variable over a large number of trials.
As a motivating example, let $X$ be the number on a six-sided die. Over a large number of rolls, we should expect to obtain an average of 3.5 on the die (even though it's not possible to roll a 3.5). The formula for expected value confirms that $E(X)=\sum_{k=1}^{6}k*Pr(X=k)=3.5$.
More generally, a random variable for which every one of a number of equally spaced outcomes has the same probability is called a uniform random variable (in the die example, this "equal spacing" is equal to 1). We can generalize our die example to find that if $X$ is a uniform random variable with minimum possible value $a$ and maximum possible value $b$, then $E(X)=\frac{a+b}{2}$. You may also wish to verify that for the dice example, if $Y$ is the random variable associated with the outcome of a second die roll, then $E(X+Y)=7$.

<span style="color:rgba(70,165,70,255); font-weight:bold">Given</span>: Six nonnegative integers, each of which does not exceed 20,000. The integers correspond to the number of couples in a population possessing each genotype pairing for a given factor. In order, the six given integers represent the number of couples having the following genotypes:
- AA-AA
- AA-Aa
- AA-aa
- Aa-Aa
- Aa-aa
- aa-aa

<span style="color:rgba(70,165,70,255); font-weight:bold">Return</span>: The expected number of offspring displaying the dominant phenotype in the next generation, under the assumption that every couple has exactly two offspring.



# Read Example Input and Output


```python
%run ../../functions/read_files.ipynb
```


```python
input = read_text('sample_input.txt')
print(input)

output = read_text('sample_output.txt')
print(output)
```

    1 0 0 1 0 1
    3.5


# Problem solving logic


```python
def expected_dominant_offspring(input):
    couples_AA_AA = int(input.split(" ")[0])
    couples_AA_Aa = int(input.split(" ")[1])
    couples_AA_aa = int(input.split(" ")[2])
    couples_Aa_Aa = int(input.split(" ")[3])
    couples_Aa_aa = int(input.split(" ")[4])
    couples_aa_aa = int(input.split(" ")[5])
    
    prob_dom_AA_AA = 1
    prob_dom_AA_Aa = 1
    prob_dom_AA_aa = 1
    prob_dom_Aa_Aa = 0.75
    prob_dom_Aa_aa = 0.5
    prob_dom_aa_aa = 0
    
    nr_of_offspring = 2

    expected_dominant = nr_of_offspring * (couples_AA_AA * prob_dom_AA_AA + couples_AA_Aa * prob_dom_AA_Aa + couples_AA_aa * prob_dom_AA_aa + couples_Aa_Aa * prob_dom_Aa_Aa + couples_Aa_aa * prob_dom_Aa_aa + couples_aa_aa * prob_dom_aa_aa)
 
    return expected_dominant   

expected_dominant_offspring(input)
```




    3.5




```python
expected_dominant_offspring(input) == float(output)
```




    True



# Run real input


```python
with open("./rosalind_iev.txt", "r") as file:
    real_input = file.read()
    
expected_dominant_offspring(real_input)


```




    159103.0


