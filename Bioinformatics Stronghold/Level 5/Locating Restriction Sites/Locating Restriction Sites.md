---
---

# Locating Restriction Sites

## Read Sample Input and Output


```python
from rosalind.string_algorithms import find_reverse_palindromes
from rosalind.read_files import read_text, write_text, read_fasta
```


```python
sample_input = read_fasta('sample_input.txt')
print("Sample Input:\n", sample_input)

sample_output = read_text('sample_output.txt')+ "\n"
print("\nSample Output:\n",sample_output)
```

    Sample Input:
         Identifier                   Sequence
    0  Rosalind_24  TCAATGCATGCGGGTCTATATGCAT
    
    Sample Output:
     4 6
    5 4
    6 6
    7 4
    17 4
    18 4
    20 6
    21 4
    


## Solve Sample Problem


```python
def solve_problem(input):
    return find_reverse_palindromes(input.iloc[0,:].Sequence, 4, 12)

```


```python
my_sample_output = solve_problem(sample_input)
my_sample_output
```




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
      <th>Position</th>
      <th>Length</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4</td>
      <td>6</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5</td>
      <td>4</td>
    </tr>
    <tr>
      <th>2</th>
      <td>6</td>
      <td>6</td>
    </tr>
    <tr>
      <th>3</th>
      <td>7</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>17</td>
      <td>4</td>
    </tr>
    <tr>
      <th>5</th>
      <td>18</td>
      <td>4</td>
    </tr>
    <tr>
      <th>6</th>
      <td>20</td>
      <td>6</td>
    </tr>
    <tr>
      <th>7</th>
      <td>21</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
def print_output(output, file_path = 'output.txt'):
    output_string = output.to_csv(sep=' ', index=False, header=False)
    
    write_text(output_string, file_path)
    
    print("Output String:\n",output_string)
        
    return output_string


```


```python
print_output(my_sample_output, "my_sample_output.txt") == sample_output
```

    Output String:
     4 6
    5 4
    6 6
    7 4
    17 4
    18 4
    20 6
    21 4
    





    True



## Run Real Input


```python
real_input = read_fasta('rosalind_revp.txt')

print_output(solve_problem(real_input), "my_rosalind_revp_output.txt");
```

    Output String:
     1 4
    54 8
    55 6
    56 4
    82 4
    93 6
    94 4
    122 4
    135 4
    138 4
    143 4
    145 4
    147 6
    148 4
    153 4
    192 4
    194 4
    223 4
    249 4
    306 6
    307 4
    359 4
    372 6
    373 4
    383 4
    437 4
    443 4
    449 4
    459 12
    460 4
    460 10
    461 8
    462 6
    463 4
    466 4
    472 4
    482 4
    523 4
    538 8
    539 6
    540 4
    559 4
    596 6
    597 4
    621 4
    625 6
    626 4
    650 10
    651 8
    652 6
    653 4
    684 4
    686 4
    690 4
    699 6
    700 4
    713 4
    725 4
    738 4
    747 4
    753 6
    754 4
    762 6
    763 4
    802 4
    814 6
    815 4
    846 4
    858 4
    866 4
    875 4
    920 4
    925 4
    

