# Databricks notebook source
with open("/Workspace/Users/pmm203@fluvius.be/rosalind/Counting DNA Nucleotides/rosalind_dna.txt", "r") as file:
    dna = file.read().strip()


# COMMAND ----------

dna

# COMMAND ----------

for i in 'ACGT':
    print(dna.count(i))

# COMMAND ----------


