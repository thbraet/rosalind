# Databricks notebook source
# MAGIC %run "../Init"

# COMMAND ----------

with open(home_path+"3. Complementing a Strand of DNA/sample_input.txt", "r") as file:
    input = file.read()

with open(home_path+"3. Complementing a Strand of DNA/sample_output.txt", "r") as file:
    output = file.read()

# COMMAND ----------

def complement_strand_of_dna(dna_sequence):
    # Define the translation table for nucleotide replacement
    translation_table = str.maketrans('ATCG', 'TAGC')
    # Reverse the DNA sequence and translate it using the table
    return dna_sequence[::-1].translate(translation_table)

complement_strand_of_dna(input)

# COMMAND ----------

def test_complement_strand_of_dna():
    assert complement_strand_of_dna(input) == output, "Test failed"

test_complement_strand_of_dna()

# COMMAND ----------

with open(home_path+"3. Complementing a Strand of DNA/rosalind_revc.txt", "r") as file:
    real_input = file.read()

complement_strand_of_dna(real_input)

# COMMAND ----------


