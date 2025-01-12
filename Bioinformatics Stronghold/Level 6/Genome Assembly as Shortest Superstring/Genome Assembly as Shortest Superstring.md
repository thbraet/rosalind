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

# Solution


```python
def overlap_length(suffix, prefix):
    """Calculate the length of overlap between a suffix and a prefix."""
    max_overlap = min(len(suffix), len(prefix))
    for i in range(max_overlap, 0, -1):
        if suffix[-i:] == prefix[:i]:
            return i
    return 0
```


```python
def find_and_merge_largest_overlap(strings):

    first_string = strings[0]
    best_overlap = 0
    best_matching_string = None
    best_match_index = -1

    unfinished = True

    while unfinished == True;

        for i, string1 in enumerate(strings):
            best_overlap = 0


            for j, string2 in enumerate(strings):
                if i != j:
                    overlap = overlap_length(string1, string2)
                    if overlap > best_overlap:
                        best_overlap = overlap
                        best_matching_string = string2
                        best_match_index = j
            overlap = overlap_length(first_string, string)
            if overlap > best_overlap:
                best_overlap = overlap
                best_matching_string = string
                best_match_index = i

    # Compare the first string with the rest of the strings to find the best overlap
    for i, string in enumerate(strings[1:], 1):
        overlap = overlap_length(first_string, string)
        if overlap > best_overlap:
            best_overlap = overlap
            best_matching_string = string
            best_match_index = i

    if best_matching_string:
        # Merge the two strings based on the overlap
        merged_string = first_string + best_matching_string[best_overlap:]
        # Remove the second string from the list and append the merged string to the front
        strings[0] = merged_string
        del strings[best_match_index]

    return strings
```


```python
def function(input):
    print(input)
```


```python
function(input) == output
```

    Hello World


# Submit solution


```python
real_input = read_text('real_input.txt')

function(real_input)
```
