# Databricks notebook source
# MAGIC %run "../Init"

# COMMAND ----------

with open(home_path+"2. Transcribing DNA into RNA/sample_input.txt", "r") as file:
    input = file.read()

with open(home_path+"2. Transcribing DNA into RNA/sample_output.txt", "r") as file:
    output = file.read()

# COMMAND ----------

def transcribe_dna_to_rna(dna_sequence):
    return dna_sequence.replace("T", "U")

transcribe_dna_to_rna(input)

# COMMAND ----------

def test_transcribe_dna_to_rna():
    assert transcribe_dna_to_rna(input) == output, "Test failed: DNA to RNA transcription error"

test_transcribe_dna_to_rna()

# COMMAND ----------

with open(home_path+"2. Transcribing DNA into RNA/rosalind_rna.txt", "r") as file:
    real_input = file.read()

transcribe_dna_to_rna(real_input)

# COMMAND ----------


