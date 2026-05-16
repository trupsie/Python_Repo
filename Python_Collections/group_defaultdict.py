from collections import defaultdict
#dic = defaultdict()
def group_dict(lst):
    dic = defaultdict(list)
    for c, v in lst:
        dic[c].append(v)
    return dict(dic)
colors_value = [('blue', 1), ('red', 2), ('green', 3), ('orange', 4)]
print(group_dict(list(colors_value)))

    