---
---

# Genes are Discontiguous

In “Transcribing DNA into RNA”, we mentioned that a strand of DNA is copied into a strand of RNA during transcription, but we neglected to mention how transcription is achieved.

In the nucleus, an enzyme (i.e., a molecule that accelerates a chemical reaction) called RNA polymerase (RNAP) initiates transcription by breaking the bonds joining complementary bases of DNA. It then creates a molecule called precursor mRNA, or pre-mRNA, by using one of the two strands of DNA as a template strand: moving down the template strand, when RNAP encounters the next nucleotide, it adds the complementary base to the growing RNA strand, with the provision that uracil must be used in place of thymine; see Figure 1.

Because RNA is constructed based on complementarity, the second strand of DNA, called the coding strand, is identical to the new strand of RNA except for the replacement of thymine with uracil. See Figure 2 and recall “Transcribing DNA into RNA”.

After RNAP has created several nucleotides of RNA, the first separated complementary DNA bases then bond back together. The overall effect is very similar to a pair of zippers traversing the DNA double helix, unzipping the two strands and then quickly zipping them back together while the strand of pre-mRNA is produced.

For that matter, it is not the case that an entire substring of DNA is transcribed into RNA and then translated into a peptide one codon at a time. In reality, a pre-mRNA is first chopped into smaller segments called introns and exons; for the purposes of protein translation, the introns are thrown out, and the exons are glued together sequentially to produce a final strand of mRNA. This cutting and pasting process is called splicing, and it is facilitated by a collection of RNA and proteins called a spliceosome. The fact that the spliceosome is made of RNA and proteins despite regulating the splicing of RNA to create proteins is just one manifestation of a molecular chicken-and-egg scenario that has yet to be fully resolved.

In terms of DNA, the exons deriving from a gene are collectively known as the gene's coding region.

[Link to Rosalind](https://rosalind.info/problems/splc/)

# Problem

After identifying the exons and introns of an RNA string, we only need to delete the introns and concatenate the exons to form a new string ready for translation.

<span style="color:rgba(70,165,70,255); font-weight:bold">Given</span>: A DNA string $s$ (of length at most 1 kbp) and a collection of substrings of $s$ acting as introns. All strings are given in FASTA format.

<span style="color:rgba(70,165,70,255); font-weight:bold">Return</span>: A protein string resulting from transcribing and translating the exons of $s$. (Note: Only one solution will exist for the dataset provided.)

# Read Example Input and Output Files


```python
%run ../../functions/read_files.ipynb
```


```python
input = read_fasta('sample_input.txt')
print(input)

output = read_text('sample_output.txt')
print(output)
```

        Identifier                                           Sequence
    0  Rosalind_10  ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCT...
    1  Rosalind_12                                         ATCGGTCGAA
    2  Rosalind_15                                    ATCGGTCGAGCGTGT
    MVYIADKQHVASREAYGHMFKVCA


# Problem solving logic


```python
def splice(rna, introns):
    for intron in introns:
        rna = rna.replace(intron, "")
    rna = rna.replace("T", "U")
    return rna

def translate(spliced_rna, codon_dict):
    protein = ""
    for i in range(0, len(spliced_rna), 3):
        codon = spliced_rna[i:i + 3]
        # print(i, codon)
        amino_acid = codon_dict[codon]
        if amino_acid == "Stop":
            break
        protein += amino_acid
    return protein

def get_protein(input):
    rna = input.iloc[0].Sequence
    introns = input.iloc[1:].Sequence.tolist()
    
    # rna, introns = read_fasta(file_path)
    spliced_rna = splice(rna, introns)
    protein = translate(spliced_rna, codon_dict)
    return protein

get_protein(input)
```




    'MVYIADKQHVASREAYGHMFKVCA'




```python
get_protein(input) == output
```




    True



# Run real input


```python
real_input = read_fasta('rosalind_splc.txt')
get_protein(real_input)
```




    'MSWPREDTIGPPPKSRLDKHITCLGPKCNGISRVVTTLDRGLYDGMSPDHHVVPSAAYRQTRIVYEQCCAVRRWNQQRTQRSYRSYVPSQRTLRGDISVSLIALIFTPSSPCIPQTQAAYRHRPRDEEGTPPWEDPKVGPPILLSCRETYRSYSVFIRSLAISGGGHYLVNMEECGEASRVRHLALDSCRQAGQ'


