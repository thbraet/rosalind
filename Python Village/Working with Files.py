# Databricks notebook source
f_input = open("/Workspace/Users/pmm203@fluvius.be/rosalind/Python Village/rosalind_ini5.txt", 'r')
f_output = open("/Workspace/Users/pmm203@fluvius.be/rosalind/Python Village/sample_output_file.txt", 'w')
for i, line in enumerate(f_input):
    if i % 2 == 1:
        print(line)
        f_output.write(line)

f_input.close()
f_output.close()


# COMMAND ----------

f_input = open("/Workspace/Users/pmm203@fluvius.be/rosalind/Python Village/rosalind_ini5.txt", 'r')
f_output = open("/Workspace/Users/pmm203@fluvius.be/rosalind/Python Village/rosalind_ini5_output.txt", 'w')
for i, line in enumerate(f_input):
    if i % 2 == 1:
        print(line)
        f_output.write(line)

f_input.close()
f_output.close()

# COMMAND ----------


