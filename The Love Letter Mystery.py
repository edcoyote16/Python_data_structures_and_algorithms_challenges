
# find the half
s='abcd'
s=list(s)
mid=len(s)//2
lower_case = 'abcdefghijklmnopqrstuvwxyz'
lower_case=list(lower_case)
# sequence=[str(n) for n in range(1, 27)]
#res = {lower_case[i]: sequence[i] for i in range(len(lower_case))}
res={'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '10', 'k': '11', 'l': '12', 'm': '13', 'n': '14', 'o': '15', 'p': '16', 'q': '17', 'r': '18', 's': '19', 't': '20', 'u': '21', 'v': '22', 'w': '23', 'x': '24', 'y': '25', 'z': '26'}
print(res)
base=[]
for n in s:
    base+=[res[n]]
# print(base)
# check which side is greater than
counter=0
if len(s)%2==0:
    mid= int((len(base)/2)-1)

    # mid = int(len(base)/2)
    for n in range(mid+1):
        if int(base[mid+1+n]) > int(base[mid-n]):
            counter += int(base[mid + 1+ n]) - int(base[mid - n])
            base[mid + 1 + n] = base[mid - n]

        elif int(base[mid+1+n] )< int(base[mid-n]):
            counter += int(base[mid - n]) - int(base[mid + 1+ n])
            base[mid - n] = base[mid + 1+n]

else:
    mid = int(len(base)/2)
    for n in range(mid+1):
        if int(base[mid+n]) > int(base[mid-n]):
            counter += int(base[mid + n]) - int(base[mid - n])
            base[mid + n] = base[mid - n]

        elif int(base[mid+n] )< int(base[mid-n]):
            counter += int(base[mid - n]) - int(base[mid + n])
            base[mid - n] = base[mid + n]


# print(base[mid])
print(counter)
# get the palindrome


# compare the difference


# count the difference