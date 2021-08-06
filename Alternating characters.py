
s='AAAA'
s=[n for n in list(s)]
counter = 0
for index, n in enumerate(s):
    try:
        if n == s[index + 1]:
            counter += 1

    except IndexError:
        pass
print(counter)