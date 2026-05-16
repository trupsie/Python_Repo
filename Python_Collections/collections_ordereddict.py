#This program will print the ordered list in the same way it was entered or listed

import collections
import re
subjects = int(input('Enter Number of Subjects: '))
subjects_order = collections.OrderedDict()
for s in range(subjects):
    subjects_marks = re.split(r'(\d+)$', input('Input Subject Name and Marks:').strip())
    subjects_name = subjects_marks[0]         #subject name
    subjects_number = int(subjects_marks[1])  #subject number
    if subjects_name not in subjects_order:
        subjects_order[subjects_name] = subjects_number
    else:
        subjects_order[subjects_name] = subjects_order[subjects_name] + subjects_number
for i in subjects_order:
    print(i+str(subjects_order[i]))
