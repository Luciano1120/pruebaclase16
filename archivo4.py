import collections as cl 

# empty Counter
counter = cl.Counter()
print(counter)  # Counter()

# Counter with initial values
counter = cl.Counter(['a', 'a', 'b']) #cuenta elementos
print(counter)  # Counter({'a': 2, 'b': 1})

counter = cl.Counter(a=2, b=3, c=1)
print(counter)  # Counter({'b': 3, 'a': 2, 'c': 1})