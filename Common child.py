from collections import Counter
string1='WEWOUCUIDGCGTRMEZEPXZFEJWISRSBBSYXAYDFEJJDLEBVHHKS'
string2='FDAGCXGKCTKWNECHMRXZWMLRYUCOCZHJRRJBOAJOQJZZVUYXIC'
string1=[n for n in string1]
string2=[n for n in string2]
string1_new=string1[::]
string2_new=string2[::]

for index_a, a in enumerate(string1):
     if a not in string2:
         string1_new.remove(a)
for index_b, b in enumerate(string2):
     if b not in string1:
         string2_new.remove(b)

string1_new=''.join(string1_new)
string2_new=''.join(string2_new)

findings1=[]
findings2=[]
counter=0
second_counter=0
results=[]
for index_c, c in enumerate(string1_new):
    for index_d, d in enumerate(string2_new):
        if string1_new[index_c:index_d+1] not in findings1 and string1_new[index_c:index_d+1]!='':
            findings1+=[string1_new[index_c:index_d+1]]
        if string2_new[index_c:index_d+1] not in findings2 and string2_new[index_c:index_d+1]!='':
            findings2+= [string2_new[index_c:index_d+1]]
for e in findings1:
    for f in findings2:
        if e == f:
            results+=[len(e)]


         # if string1_new[index_c:index_d]==string2_new[index_c:index_d]:
         #     findings+=[string2_new[index_c:index_d]]

#             if string2_new[index_c:index_d]=='':
#                 findings+=[0]
#             elif len(string2_new[index_c:index_d])>0:
#                 findings += [len(string2_new[index_c:index_d])]


if not results:
    print(0)
else:
    print(max(results))
