---
---

# Wabbit Season

In “Rabbits and Recurrence Relations”, we mentioned the disaster caused by introducing European rabbits into Australia. By the turn of the 20th Century, the situation was so out of control that the creatures could not be killed fast enough to slow their spread (see Figure 1).

The conclusion? Build a fence! The fence, intended to preserve the sanctity of Western Australia, was completed in 1907 after undergoing revisions to push it back as the bunnies pushed their frontier ever westward (see Figure 2). If it sounds like a crazy plan, the Australians at the time seem to have concurred, as shown by the cartoon in Figure 3.

By 1950, Australian rabbits numbered 600 million, causing the government to decide to release a virus (called myxoma) into the wild, which cut down the rabbits until they acquired resistance. In a final Hollywood twist, another experimental rabbit virus escaped in 1991, and some resistance has already been observed.

The bunnies will not be stopped, but they don't live forever, and so in this problem, our aim is to expand Fibonacci's rabbit population model to allow for mortal rabbits.

[Link to Rosalind](https://rosalind.info/problems/fibd/)

# Problem

Recall the definition of the Fibonacci numbers from “Rabbits and Recurrence Relations”, which followed the recurrence relation $F_{n}=F_{n−1}+F_{n−2} and assumed that each pair of rabbits reaches maturity in one month and produces a single pair of offspring (one male, one female) each subsequent month.

Our aim is to somehow modify this recurrence relation to achieve a dynamic programming solution in the case that all rabbits die out after a fixed number of months. See Figure 4 for a depiction of a rabbit tree in which rabbits live for three months (meaning that they reproduce only twice before dying).

<span style="color:rgba(70,165,70,255); font-weight:bold">Given</span>: Positive integers $n≤100$ and $m≤20$.

<span style="color:rgba(70,165,70,255); font-weight:bold">Return</span>: The total number of pairs of rabbits that will remain after the $n$-th month if all rabbits live for $m$ months.

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

    6 3
    4


# Problem solving logic


```python
def get_mortal_fibonacci_rabbits(input):
    month = int(input.split(" ")[0])
    lifespan = int(input.split(" ")[1])
    
    rabbits_m = []
    m1 = [1] + [0] * (lifespan - 1)
    rabbits_m = [m1]
    for m in range(1, month):
        new_rabbits = sum(rabbits_m[m-1]) - rabbits_m[m-1][0]
        rabbits_i = [new_rabbits] + rabbits_m[m-1][:-1]
        rabbits_m.append(rabbits_i)
    return sum(rabbits_m[-1])

get_mortal_fibonacci_rabbits(input)
```




    4




```python
get_mortal_fibonacci_rabbits(input) == int(output)  
```




    True




```python
# Recursive solution but takes too long to execute

def get_newborns(t, L):
    if t <= 0:
        return 0
    if t == 1:
        return 1
    else:
        total = 0
        for i in range(2, L+1):
            total += get_newborns(t-i, L)
        return total            

def get_mortal_fibonacci_rabbits_recursive(t, L):
    total = 0
    for i in range(1, L+1):
        total += get_newborns(t-i+1, L)
    return total

print(get_mortal_fibonacci_rabbits_recursive(6, 3))
```

    4


# Run real input


```python
real_input = read_text('rosalind_fibd.txt')

get_mortal_fibonacci_rabbits(real_input)
```




    159659704963213182


