from itertools import combinations
from collections import Counter
sentences = [    
             "the cat sat on the mat",   
             "the dog chased the cat",    
             "the dog and the cat are friends", 
            ] 
#wspolwystepujace pary slow
def words_co_occurrence(sentences):
    count_pairs = Counter()
    for sentence in sentences:
        words = set(sentence.split()) #split podzieli liste na trzy osobne zdania bo jest przecinek 
        pairs = combinations(sorted(words), 2) #sorted zapewni ze np. cat,sat i sat,cat to bedzie ta sama para, 2 to ilczba elementow 
        count_pairs.update(pairs)
    
    return count_pairs
# print(words_co_occurrence(sentences)) # to mi da dobry wynik, ale nie taki jak w spodziewany wyniku 
#rozwiazanie to uzycie .most_common() - w zadaniu ma byc top 3
print(words_co_occurrence(sentences).most_common(3)) 
    
    
# expected (top 3): 
# # (cat, the): 3   
# # cat appears with ‘the’ across all 3 sentences (counted per sentence with duplicates) 
# # (dog, the): 2 
# # (cat, dog): 2
