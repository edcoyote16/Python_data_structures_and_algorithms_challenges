from collections import Counter


def makingAnagrams(s1, s2):
    # Write your code here
    base1 = Counter(s1)
    base2 = Counter(s2)
    final1 = base1 - base2
    final2 = base2 - base1

    return sum(list(final1.values()) + list(final2.values()))


s1 = 'WEWOUCUIDGCGTRMEZEPXZFEJWISRSBBSYXAYDFEJJDLEBVHHKS'
s2 = 'FDAGCXGKCTKWNECHMRXZWMLRYUCOCZHJRRJBOAJOQJZZVUYXIC'
makingAnagrams(s1, s2)
