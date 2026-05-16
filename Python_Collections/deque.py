import collections
my_colors = collections.deque(['red','blue','white','orange','green','purple'])
my_colors.appendleft(['brown', 'black'])
#my_colors.appendleft('yellow') 
my_colors.pop()
print(my_colors)
my_colors.popleft()
print(my_colors)
my_colors.reverse()
print(my_colors)

my_numbers = (2, 4, 6, 8)
my_numbers_deque = collections.deque(my_numbers)
print(my_numbers_deque)
my_numbers_deque.append(10)
print(my_numbers_deque)
my_numbers_more = (11, 22, 68, 28, 85, 90, 100)
my_numbers_deque.extend(my_numbers_more)
print(my_numbers_deque)
my_numbers_remove = (2, 4, 8)
for num in my_numbers_remove:
    if num in my_numbers_deque:
        my_numbers_deque.remove(num)
print(my_numbers_deque)
