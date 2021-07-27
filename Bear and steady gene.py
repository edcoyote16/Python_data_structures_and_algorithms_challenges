
from collections import Counter
s1='tttttttttttttttttttttttttttttttttttttsssssssssssssssss'
s2='sssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss'
base1=Counter(s1)
base2=Counter(s2)
final1=base1-base2
final2=base2-base1

results=sum(list(final1.values())+list(final2.values()))
# gene='GAAATAAA'
# length=len(gene)
# beautiful_amount=int(length/4)
# base='CGAT'*beautiful_amount
# base=Counter(base)
# my_counter_gene=Counter(gene)
#
# quantity=sum(list(my_counter_gene.values()))
# final=base-my_counter_gene
# final2=my_counter_gene-base
# final2=sum(final2.values())
#
#
# init = 0
# final = 0
# #while base!=my_counter_gene:
# test=gene
# for counter in range(length):
#     for second_counter in range(length):
#
#         substitution=gene[init+counter:final+1+counter+second_counter]
#
#         test=test.replace(substitution,'')
#
#         my_counter_gene2 = Counter(test)
#         # tengo AATAA y con ello requiero saber qué letras faltan
#
#         # y hacer la prueba para saber si estas quedan
#         if base == my_counter_gene2:
#             print('ok')
#
#
#
#
#
#
print(results)
