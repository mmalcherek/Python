from itertools import combinations
from collections import Counter

scores = {"a": 90, "b": 85, "c": 90, "d": 70, "e": 85, "f": 60}
sorted_scores = sorted(scores.values(), reverse=True)
# print(sorted_scores)
#[90, 90, 85, 85, 70, 60]
# 0   1   2   3   4   5 to indeksy

def top_k_with_ties(scores, K):
    sorted_scores = sorted(scores.values(), reverse=True)
    find_k = sorted_scores[K] 
    return {name: score for name, score in scores.items() if score >= find_k}
print(top_k_with_ties(scores, 2))   


#opcje z lista składaną
def top_k_with_ties_comp_list(scores, K):
    find_k = sorted(scores.values(), reverse=True)[K]
    return sorted(
        [name for name, score in scores.items() if score >= find_k],
        key=lambda name: scores[name], reverse=True
    )
print(top_k_with_ties_comp_list(scores, 2))
