


x = 8
s = 'GAAATAAA'
dic = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
for i in s:
    dic[i] += 1
x = len(s)
n = x / 4
i = 0
j = 0
min = x
if dic['A'] == n and dic['T'] == n and dic['C'] == n and dic['G'] == n:
    print(0)
else:
    while i < x and j < x:
        while (dic['A'] > n or dic['C'] > n or dic['T'] > n or dic['G'] > n) and i < x:
            dic[s[i]] -= 1
            i += 1
        while dic['A'] <= n and dic['C'] <= n and dic['T'] <= n and dic['G'] <= n:
            dic[s[j]] += 1
            j += 1
        if i - j < min:
            min = i - j + 1
    print(min)