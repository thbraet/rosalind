---
---

# Finding a Protein Motif

## Read Sample Input and Output


```python
from rosalind.string_algorithms import find_glycosylation_motifs
from rosalind.read_files import read_text, write_text
```


```python
sample_input = read_text('sample_input.txt')
print("Sample Input:\n", sample_input)

sample_output = read_text('sample_output.txt')+"\n"
print("\nSample Output:\n",sample_output)
```

    Sample Input:
     A2Z669
    B5ZC00
    P07204_TRBM_HUMAN
    P20840_SAG1_YEAST
    
    Sample Output:
     B5ZC00
    85 118 142 306 395
    P07204_TRBM_HUMAN
    47 115 116 382 409
    P20840_SAG1_YEAST
    79 109 135 248 306 348 364 402 485 501 614
    


## Solve Sample Problem


```python
def solve_problem(input):
    output_str = ""
    for i in input.split("\n"):
        motifs = find_glycosylation_motifs(i)
        if motifs:
            output_str += i + "\n" + motifs + "\n"
    return output_str

```


```python
my_sample_output = solve_problem(sample_input)
print(my_sample_output)
```

    No glycosylation motifs found for A2Z669.
    B5ZC00
    85 118 142 306 395
    P07204_TRBM_HUMAN
    47 115 116 382 409
    P20840_SAG1_YEAST
    79 109 135 248 306 348 364 402 485 501 614
    



```python
def print_output(output, file_path = 'output.txt'):
    output_string = str(output)
    
    write_text(output_string, file_path)
    
    print("Output String:\n",output_string)
        
    return output_string


```


```python
print_output(my_sample_output, "my_sample_output.txt") == sample_output
```

    Output String:
     B5ZC00
    85 118 142 306 395
    P07204_TRBM_HUMAN
    47 115 116 382 409
    P20840_SAG1_YEAST
    79 109 135 248 306 348 364 402 485 501 614
    





    True



## Run Real Input


```python
real_input = read_text('rosalind_mprt.txt')

print_output(solve_problem(real_input), "my_rosalind_mprt_output.txt");
```

    No glycosylation motifs found for Q9CE42.
    No glycosylation motifs found for Q83I57.
    No glycosylation motifs found for Q8WW18.
    No glycosylation motifs found for Q28409.
    Output String:
     P10643_CO7_HUMAN
    202 754
    Q3Z2Z2
    49
    P02725_GLP_PIG
    16 19 39
    P07359_GPBA_HUMAN
    37 175 362 398
    P07585_PGS2_HUMAN
    211 262 303
    P01880_DTC_HUMAN
    225 316 367
    P72173
    87 284 383
    Q90304_C166_CARAU
    92 171 350 441 465
    

