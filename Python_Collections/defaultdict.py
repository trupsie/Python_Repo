from collections import defaultdict
emp_rank = [('Jen', 1), ('Dan', 2), ('John', 3)]
dic = defaultdict(list)
for p, r in emp_rank:
    dic[p].append(r)
print(sorted(dic.items()))
