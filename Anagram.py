# string = list(string)
# length = len(string)
# result = 0
# mid = int(length / 2)
# string1=sorted(string[:mid])
# string2=sorted(string[mid:])
#
# if length % 2 != 0:
#     print(-1)
# else:
#     for index, n in enumerate(range(0, mid)):
#         if string1[index] != string2[index]:
#             result += 1
#
# print(result)
from collections import Counter
# n = int(input())
# for _ in range(n):
#     test = input()
test = 'csgokgibmftzeozyadcofpouaerckbbpwhdg'

length = len(test)
if len(test) % 2 != 0:
    print("-1")
else:
    s1 = Counter(test[:length//2])
    s2 = Counter(test[length//2:])
    diff = s1 - s2
    print(sum(diff.values()))
    both= s1 + s2
    print(sum(both.values()))


