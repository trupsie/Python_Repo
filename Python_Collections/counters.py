'''from collections import Counter
#def counter_elements(count):
counts = Counter(Trupti = 2, Patel = 3)
print(list(counts.elements()))'''

from collections import Counter  
def counter_elements(count):
    return list(count.elements())
counts = Counter(Trupti = 2, Patel = 3)
print(counter_elements(counts))