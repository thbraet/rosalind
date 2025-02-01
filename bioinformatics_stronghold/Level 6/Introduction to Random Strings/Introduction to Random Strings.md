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

    ACGATACAA
    0.129 0.287 0.423 0.476 0.641 0.742 0.783
    -5.737 -5.217 -5.263 -5.360 -5.958 -6.628 -7.009


# Solution


```python
def get_log_probability(gc_content, dna):
    prob_log = 0
    frequency_map = {
        'A': (1-gc_content)/2,
        'C': gc_content/2,
        'T': (1-gc_content)/2,
        'G': gc_content/2
        }

    for char in dna:
        prob_log += np.log10(frequency_map[char])

    return prob_log

# input_dna = input.split('\n')[0]
# gc_content = float(input.split('\n')[1].split(' ')[0])

def get_all_log_probability(input):
    input_dna = input.split('\n')[0]
    gc_contents = [float(num) for num in input.split('\n')[1].split()]

    output_string = ''

    for gc_content in gc_contents:
        prob = get_log_probability(gc_content, input_dna)
        output_string += f"{prob:.3f}" + ' '

    return output_string.rstrip()


print(get_all_log_probability(input))
```

    -5.737 -5.217 -5.263 -5.360 -5.958 -6.628 -7.009



```python
get_all_log_probability(input) == output
```




    True



# Submit solution


```python
real_input = read_text('rosalind_prob.txt')

get_all_log_probability(real_input)
```




    '-72.067 -64.517 -56.167 -53.731 -51.787 -49.664 -49.081 -48.546 -48.178 -48.339 -48.619 -49.428 -50.411 -51.888 -56.452 -59.667 -66.093 -75.507'




```python

```
