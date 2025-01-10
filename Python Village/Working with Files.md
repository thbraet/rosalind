---
---

```python
f_input = open("./sample_input_file.txt", 'r')
f_output = open("./sample_output_file.txt", 'w')
for i, line in enumerate(f_input):
    if i % 2 == 1:
        print(line)
        f_output.write(line)

f_input.close()
f_output.close()

```

    Yes, brave Sir Robin turned about
    
    And gallantly he chickened out
    
    Bravely talking to his feet
    
    He beat a very brave retreat



```python

f_input = open("./rosalind_ini5.txt", 'r')
f_output = open("./rosalind_ini5_output.txt", 'w')
for i, line in enumerate(f_input):
    if i % 2 == 1:
        print(line)
        f_output.write(line)

f_input.close()
f_output.close()
```

    Some things in life are bad, they can really make you mad
    
    Other things just make you swear and curse
    
    When you're chewing on life's gristle, don't grumble give a whistle
    
    This will help things turn out for the best
    
    Always look on the bright side of life
    
    Always look on the right side of life
    
    If life seems jolly rotten, there's something you've forgotten
    
    And that's to laugh and smile and dance and sing
    
    When you're feeling in the dumps, don't be silly, chumps
    
    Just purse your lips and whistle, that's the thing
    
    So, always look on the bright side of death
    
    Just before you draw your terminal breath
    
    Life's a counterfeit and when you look at it
    
    Life's a laugh and death's the joke, it's true
    
    You see, it's all a show, keep them laughing as you go
    
    Just remember the last laugh is on you
    
    Always look on the bright side of life
    
    And always look on the right side of life
    
    Always look on the bright side of life
    
    And always look on the right side of life
    



```python

```
