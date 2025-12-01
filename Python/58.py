# ) Write a Python program to combine values in python list of dictionaries. 
# Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 
# 300}, o {'item': 'item1', 'amount': 750}] 
# Expected Output: 
# • Counter ({'item1': 1150, 'item2': 300})

from collections import Counter

data = [
    {'item': 'item1', 'amount': 400},
    {'item': 'item2', 'amount': 300},
    {'item': 'item1', 'amount': 750}
]

counter = Counter() #counter will store and add values in the dict 

for d in data:
    counter[d['item']] += d['amount']

print(counter)
