---
---

# Computing GC Content

## Read Sample Input and Output


```python
from rosalind.string_algorithms import get_gc_content
from rosalind.read_files import read_text, write_text, read_fasta
```


```python
sample_input = read_fasta('sample_input.txt')
print("Sample Input:\n")
display(sample_input)

sample_output = read_text('sample_output.txt')
print("\nSample Output:\n",sample_output)
```

    Sample Input:
    



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Identifier</th>
      <th>Sequence</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Rosalind_6404</td>
      <td>CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGG...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Rosalind_5959</td>
      <td>CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGC...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Rosalind_0808</td>
      <td>CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTC...</td>
    </tr>
  </tbody>
</table>
</div>


    
    Sample Output:
     Rosalind_0808
    60.919540


## Solve Sample Problem


```python
def solve_problem(input):
    max_gc_content = 0
    max_gc_content_id = None
    for id, seq in input.iterrows():
        gc_content = get_gc_content(seq.Sequence)
        if gc_content > max_gc_content:
            max_gc_content = gc_content
            max_gc_content_id = seq.Identifier
    return max_gc_content_id, max_gc_content
```


```python
my_sample_output = solve_problem(sample_input)
my_sample_output
```




    ('Rosalind_0808', 0.6091954022988506)




```python
def print_output(output, file_path = 'output.txt'):
    output_string = f"{output[0]}\n{output[1]*100:.6f}"
    
    write_text(output_string, file_path)
    
    print("Output String:\n",output_string)
        
    return output_string


```


```python
print_output(my_sample_output, "my_sample_output.txt") == sample_output
```

    Output String:
     Rosalind_0808
    60.919540





    True



## Run Real Input


```python
real_input = read_fasta('rosalind_gc.txt')

print_output(solve_problem(real_input), "my_rosalind_gc_output.txt");
```

    Output String:
     Rosalind_9404
    51.957295

