from math import log
def probs(s):
    counts = {}
    for char in s:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    total = len(s)
    probabilities = [[count / total, char] for char, count in counts.items()]
    return probabilities

s = "тевелевартёмдмитриевич"
entr = sum([-probs(s)[i][0] * log(probs(s)[i][0], 2) for i in range(len(probs(s)))])

print(entr)