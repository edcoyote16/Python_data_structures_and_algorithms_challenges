def pairs4(k, price):
    price.sort()
    prices_dict = {pr: idx for (pr, idx) in zip(range(len(price)),price)}
    counter=0
    result=0
    for i in range(len(prices_dict)-1):
        for b in range(len(prices_dict)-1):
            if (prices_dict[b + 1] - prices_dict[i]) == k:
                result+=1#[[price[b + 1],price[i]]]
            counter += 1
    return result

################################################
print(pairs(2,[1, 5, 3, 4, 2]))

######
def pairs2(k, price):
    price.sort()
    prices_dict = {pr: idx for (pr, idx) in zip(range(len(price)),price)}
    counter=0
    result=0
    for i in range(len(prices_dict)-1):
        for b in range(len(prices_dict)-1):
            if (prices_dict[b + 1] - prices_dict[i]) == k:
                result+=1#[[price[b + 1],price[i]]]
            counter += 1
    return result
def pairs1(k,a):
    # a is the list of numbers and k is the difference value
    a.sort()
    left = 0
    right = 1
    answer = 0
    while right < len(a):
        val = a[right]-a[left]
        if val == k:
            answer += 1
            left += 1
            right += 1
        elif val < k:
            right += 1
        else:
            left += 1
            if left == right:
                right += 1
    return answer
def pairs(k,arr):
    if k == 0:
        return 0
    valueMap= set(arr)
    count=0
    for n in arr:
        if n + k in valueMap:
            count+=1
    return count