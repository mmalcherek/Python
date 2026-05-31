from collections import Counter
worker_a = ["bolt", "nut", "nut", "screw", "washer", "bolt", "bolt"] 
worker_b = ["bolt", "bolt", "nut", "screw", "screw", "washer"]

count_a = Counter(worker_a)
count_b = Counter(worker_b)

#operatory na zbiorach
#przykładowo dla zbiorów A i B:
# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}
# A | B - suma zbiorów, czyli {1, 2, 3, 4, 5, 6}, lub metoda A.union(B) 
# A & B - część wspólna zbiorów, czyli {3, 4}, lub metoda A.intersection(B)
# A - B - różnica zbiorów, czyli {1, 2}, lub metoda A.difference(B)
# B - A - różnica zbiorów, czyli {5, 6}, lub metoda B.difference(A)
# A ^ B - różnica symetryczna zbiorów, czyli {1, 2, 5, 6}, lub metoda A.symmetric_difference(B)

result = {}
for words in set(count_a) | set(count_b):
    a, b = count_a[words], count_b[words]
    result[words] = {'a': a, 'b': b, 'diff': abs(a - b)}
    
#lub tak za pomocą list comprehension(lista składana)
result2 = {words: {'a': count_a[words], 'b': count_b[words], 'diff': abs(count_a[words] - count_b[words])} for words in set(count_a) | set(count_b)}
print(result)
print(result2)
