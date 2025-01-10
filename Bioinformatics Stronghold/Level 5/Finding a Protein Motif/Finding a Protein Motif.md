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

    A2Z669
    B5ZC00
    P07204_TRBM_HUMAN
    P20840_SAG1_YEAST
    B5ZC00
    85 118 142 306 395
    P07204_TRBM_HUMAN
    47 115 116 382 409
    P20840_SAG1_YEAST
    79 109 135 248 306 348 364 402 485 501 614


# Solution


```python
import re
import requests

def get_result(function_input):
    
    def find_glycosylation_motifs(uniprot_id):
        
        id = uniprot_id.split('_')[0]
        # id = uniprot_id
        
        # Fetch the FASTA data from UniProt REST API
        url = f"https://rest.uniprot.org/uniprotkb/{id}.fasta"
        response = requests.get(url)
        
        if response.status_code != 200:
            # print(f"Failed to fetch data for {uniprot_id}. HTTP status code: {response.status_code}")
            return
        
        # Parse the FASTA response
        fasta_data = response.text
        lines = fasta_data.splitlines()
        sequence = "".join(line.strip() for line in lines if not line.startswith(">") and line.isalpha())
        
        # Regular expression for the N-glycosylation motif
        pattern = r"N(?=[^P][ST][^P])"  # Lookahead to allow overlapping matches
        
        # Find all overlapping matches and their start indices
        start_positions = []
        for match in re.finditer(pattern, sequence):
            start_positions.append(match.start() + 1)  # Convert to 1-based indexing
        
        # Format the output
        if start_positions:
            print(f"{uniprot_id}\n{' '.join(map(str, start_positions))}")
            return f"{uniprot_id}\n{' '.join(map(str, start_positions))}"
        else:
            return f"{uniprot_id}\nNo motifs found"

    result = []
    for i in function_input.split('\n'):
        # print(i)
        result.append(find_glycosylation_motifs(i))
    # return result


# Example usage
get_result(input)

```

    B5ZC00
    85 118 142 306 395
    P07204_TRBM_HUMAN
    47 115 116 382 409
    P20840_SAG1_YEAST
    79 109 135 248 306 348 364 402 485 501 614



```python
print(output)
```

    B5ZC00
    85 118 142 306 395
    P07204_TRBM_HUMAN
    47 115 116 382 409
    P20840_SAG1_YEAST
    79 109 135 248 306 348 364 402 485 501 614


# Submit solution


```python
real_input = read_text('rosalind_mprt.txt')

get_result(real_input)
```

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

