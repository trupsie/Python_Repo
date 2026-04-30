def find_max_min(lst1):
   max_lst = lst1[0]
   min_lst = lst1[0]
   for n in lst1:
      if n > max_lst:
        max_lst = n
   for n in lst1:
      if n < min_lst:
        min_lst = n
   return max_lst, min_lst
print(find_max_min([1, 20, 33, 24, 5, 76, -6]))
