# Databricks notebook source
a = 4306 
b = 8428

total_sum = 0

if a % 2 == 0:
    a = a+1

for i in range(a,b,2):
    total_sum += i

print(total_sum)


# COMMAND ----------


