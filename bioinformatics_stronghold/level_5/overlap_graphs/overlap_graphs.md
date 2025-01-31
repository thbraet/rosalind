---
---

# A Brief Introduction to Graph Theory

Networks arise everywhere in the practical world, especially in biology. Networks are prevalent in popular applications such as modeling the spread of disease, but the extent of network applications spreads far beyond popular science. Our first question asks how to computationally model a network without actually needing to render a picture of the network.

First, some terminology: graph is the technical term for a network; a graph is made up of hubs called nodes (or vertices), pairs of which are connected via segments/curves called edges. If an edge connects nodes $v$ and $w$, then it is denoted by $v$, $w$ (or equivalently $w$, $v$).

- an edge $v$, $w$ is incident to nodes $v$ and $w$; we say that $v$ and $w$ are adjacent to each other;
- the degree of $v$ is the number of edges incident to it;
- a walk is an ordered collection of edges for which the ending node of one edge is the starting node of the next (e.g., $\{v_{1},v_{2}\}$,$\{v_{2},v_{3}\}$, $\{v_{3},v_{4}\}$, etc.);
- a path is a walk in which every node appears in at most two edges;
- path length is the number of edges in the path;
- a cycle is a path whose final node is equal to its first node (so that every node is incident to exactly two edges in the cycle); and
- the distance between two vertices is the length of the shortest path connecting them.

Graph theory is the abstract mathematical study of graphs and their properties.

[Link to Rosalind](https://rosalind.info/problems/grph/)

# Problem

A graph whose nodes have all been labeled can be represented by an adjacency list, in which each row of the list contains the two node labels corresponding to a unique edge.

A directed graph (or digraph) is a graph containing directed edges, each of which has an orientation. That is, a directed edge is represented by an arrow instead of a line segment; the starting and ending nodes of an edge form its tail and head, respectively. The directed edge with tail $v$ and head $w$ is represented by $(v, w)$ (but not by $(w,v)$). A directed loop is a directed edge of the form $(v,v)$.

For a collection of strings and a positive integer $k$, the overlap graph for the strings is a directed graph $O_{k}$ in which each string is represented by a node, and string $s$ is connected to string $t$ with a directed edge when there is a length $k$ suffix of $s$ that matches a length $k$ prefix of $t$, as long as $s≠t$; we demand $s≠t$ to prevent directed loops in the overlap graph (although directed cycles may be present).

<span style="color:rgba(70,165,70,255); font-weight:bold">Given</span>: A collection of DNA strings in FASTA format having total length at most 10 kbp.

<span style="color:rgba(70,165,70,255); font-weight:bold">Return</span>: The adjacency list corresponding to $O_{3}$



# Read Files


```python
%run ../../functions/read_files.ipynb
```


```python
input = read_fasta('sample_input.txt')
print(input)

output = read_text('sample_output.txt')
print(output)
```

          Identifier Sequence
    0  Rosalind_0498  AAATAAA
    1  Rosalind_2391  AAATTTT
    2  Rosalind_2323  TTTTCCC
    3  Rosalind_0442  AAATCCC
    4  Rosalind_5013  GGGTGGG
    Rosalind_0498 Rosalind_2391
    Rosalind_0498 Rosalind_0442
    Rosalind_2391 Rosalind_2323


# Solution


```python
def get_overlap_graph(input, k=3):
    result = ""
    for i,row_suffix in input.iterrows():
        for j, row_prefix in input.iterrows():
            if i!=j:
                if row_suffix.Sequence[-k:] == row_prefix.Sequence[:k]:
                    result += row_suffix.Identifier + " " + row_prefix.Identifier + "\n"

    return result

get_overlap_graph(input)

```




    'Rosalind_0498 Rosalind_2391\nRosalind_0498 Rosalind_0442\nRosalind_2391 Rosalind_2323\n'




```python
print(get_overlap_graph(input))
print("\nOUTPUT:")
print(output)
```

    Rosalind_0498 Rosalind_2391
    Rosalind_0498 Rosalind_0442
    Rosalind_2391 Rosalind_2323
    
    
    OUTPUT:
    Rosalind_0498 Rosalind_2391
    Rosalind_0498 Rosalind_0442
    Rosalind_2391 Rosalind_2323


# Submit solution


```python
real_input = read_fasta('rosalind_grph.txt')

print(get_overlap_graph(real_input))
```

    Rosalind_7803 Rosalind_4226
    Rosalind_0184 Rosalind_1277
    Rosalind_0184 Rosalind_8036
    Rosalind_7259 Rosalind_7594
    Rosalind_7259 Rosalind_0069
    Rosalind_8388 Rosalind_1644
    Rosalind_8388 Rosalind_4183
    Rosalind_8388 Rosalind_3451
    Rosalind_8388 Rosalind_5132
    Rosalind_8388 Rosalind_5894
    Rosalind_8388 Rosalind_1896
    Rosalind_9478 Rosalind_8334
    Rosalind_9478 Rosalind_2015
    Rosalind_9478 Rosalind_3322
    Rosalind_7594 Rosalind_4888
    Rosalind_7594 Rosalind_4267
    Rosalind_8864 Rosalind_2541
    Rosalind_8864 Rosalind_3778
    Rosalind_7914 Rosalind_7803
    Rosalind_7914 Rosalind_3273
    Rosalind_7894 Rosalind_7803
    Rosalind_7894 Rosalind_3273
    Rosalind_1233 Rosalind_0184
    Rosalind_1233 Rosalind_5989
    Rosalind_4930 Rosalind_2541
    Rosalind_4930 Rosalind_3778
    Rosalind_0427 Rosalind_5141
    Rosalind_9175 Rosalind_9927
    Rosalind_9175 Rosalind_5227
    Rosalind_8334 Rosalind_2180
    Rosalind_6689 Rosalind_4648
    Rosalind_6689 Rosalind_2940
    Rosalind_1277 Rosalind_1233
    Rosalind_1277 Rosalind_6689
    Rosalind_1277 Rosalind_4583
    Rosalind_1277 Rosalind_8945
    Rosalind_1277 Rosalind_8207
    Rosalind_8036 Rosalind_1574
    Rosalind_4493 Rosalind_1233
    Rosalind_4493 Rosalind_6689
    Rosalind_4493 Rosalind_4583
    Rosalind_4493 Rosalind_8945
    Rosalind_4493 Rosalind_8207
    Rosalind_3749 Rosalind_7259
    Rosalind_3749 Rosalind_0017
    Rosalind_3749 Rosalind_7776
    Rosalind_3749 Rosalind_0284
    Rosalind_3749 Rosalind_0313
    Rosalind_4331 Rosalind_7369
    Rosalind_1574 Rosalind_6406
    Rosalind_1574 Rosalind_3197
    Rosalind_1574 Rosalind_1406
    Rosalind_3455 Rosalind_5520
    Rosalind_3455 Rosalind_0286
    Rosalind_7460 Rosalind_1920
    Rosalind_7460 Rosalind_7610
    Rosalind_7765 Rosalind_4500
    Rosalind_5989 Rosalind_5141
    Rosalind_2415 Rosalind_7076
    Rosalind_6447 Rosalind_7803
    Rosalind_6447 Rosalind_3273
    Rosalind_2015 Rosalind_2180
    Rosalind_7369 Rosalind_0245
    Rosalind_7369 Rosalind_8753
    Rosalind_4583 Rosalind_5141
    Rosalind_6200 Rosalind_5141
    Rosalind_9927 Rosalind_8741
    Rosalind_9927 Rosalind_8974
    Rosalind_1644 Rosalind_4226
    Rosalind_7778 Rosalind_1920
    Rosalind_7778 Rosalind_7610
    Rosalind_4888 Rosalind_7259
    Rosalind_4888 Rosalind_0017
    Rosalind_4888 Rosalind_7776
    Rosalind_4888 Rosalind_0284
    Rosalind_4888 Rosalind_0313
    Rosalind_0069 Rosalind_0245
    Rosalind_0069 Rosalind_8753
    Rosalind_5520 Rosalind_7914
    Rosalind_5520 Rosalind_6243
    Rosalind_7076 Rosalind_7765
    Rosalind_6694 Rosalind_4912
    Rosalind_4267 Rosalind_5465
    Rosalind_6406 Rosalind_0184
    Rosalind_6406 Rosalind_5989
    Rosalind_3778 Rosalind_2180
    Rosalind_4500 Rosalind_2659
    Rosalind_3322 Rosalind_1574
    Rosalind_5465 Rosalind_4226
    Rosalind_2940 Rosalind_0703
    Rosalind_2940 Rosalind_0809
    Rosalind_8108 Rosalind_6406
    Rosalind_8108 Rosalind_3197
    Rosalind_8108 Rosalind_1406
    Rosalind_6556 Rosalind_5134
    Rosalind_5134 Rosalind_4226
    Rosalind_7776 Rosalind_6406
    Rosalind_7776 Rosalind_3197
    Rosalind_7776 Rosalind_1406
    Rosalind_8066 Rosalind_8741
    Rosalind_8066 Rosalind_8974
    Rosalind_4912 Rosalind_8741
    Rosalind_4912 Rosalind_8974
    Rosalind_0809 Rosalind_7076
    Rosalind_3071 Rosalind_9478
    Rosalind_3071 Rosalind_4930
    Rosalind_3628 Rosalind_7076
    Rosalind_2180 Rosalind_5134
    Rosalind_0284 Rosalind_2541
    Rosalind_0284 Rosalind_3778
    Rosalind_2659 Rosalind_6556
    Rosalind_9362 Rosalind_5465
    Rosalind_4183 Rosalind_7803
    Rosalind_4183 Rosalind_3273
    Rosalind_7482 Rosalind_4226
    Rosalind_5141 Rosalind_9280
    Rosalind_5141 Rosalind_9362
    Rosalind_3197 Rosalind_1277
    Rosalind_3197 Rosalind_8036
    Rosalind_8945 Rosalind_2203
    Rosalind_8945 Rosalind_4725
    Rosalind_5227 Rosalind_2180
    Rosalind_9126 Rosalind_3455
    Rosalind_9126 Rosalind_6354
    Rosalind_5894 Rosalind_1644
    Rosalind_5894 Rosalind_4183
    Rosalind_5894 Rosalind_3451
    Rosalind_5894 Rosalind_5132
    Rosalind_5894 Rosalind_1896
    Rosalind_1896 Rosalind_2415
    Rosalind_6243 Rosalind_3455
    Rosalind_6243 Rosalind_6354
    Rosalind_3273 Rosalind_4648
    Rosalind_3273 Rosalind_2940
    Rosalind_8207 Rosalind_3749
    Rosalind_8207 Rosalind_4331
    Rosalind_8207 Rosalind_6447
    Rosalind_8207 Rosalind_0070
    Rosalind_6354 Rosalind_7765
    Rosalind_4725 Rosalind_0245
    Rosalind_4725 Rosalind_8753
    Rosalind_4232 Rosalind_4888
    Rosalind_4232 Rosalind_4267
    Rosalind_6771 Rosalind_4912
    Rosalind_4226 Rosalind_2203
    Rosalind_4226 Rosalind_4725
    



```python

```
