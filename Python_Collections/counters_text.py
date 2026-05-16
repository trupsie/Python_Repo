from collections import Counter

text = "Python stories span from the creation of the widely used programming language by Guido van Rossum in 1989 to dramatic real-world accounts of massive reticulated pythons in Southeast Asia. Key success stories highlight Python's role in powering companies like Rackspace and WordStream, while other narratives detail how learning the language has transformed careers."
def counters_text(str1, n=20):
    return Counter(str1).most_common(n)
print(counters_text(text))