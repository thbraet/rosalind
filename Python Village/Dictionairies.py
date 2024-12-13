# Databricks notebook source
# Example string
text = "When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be"

substrings = list(set(text.split(' ')))

# Dictionary to store counts
substring_counts = {substring: text.count(substring) for substring in substrings}

for key, value in substring_counts.items():
    print(f"{key} {value}")


# COMMAND ----------

from collections import Counter

s = "We tried list and we tried dicts also we tried Zen"
word_count = Counter(text.split())

for word, count in word_count.items():
    print(f"{word} {count}")

# COMMAND ----------


