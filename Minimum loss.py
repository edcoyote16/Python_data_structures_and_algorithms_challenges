


# price=[20,15,8,2,12]
# result=[]
# counter=1
# value=10**16
# for a in price:
#     for b in range(counter, len(price)):
#         if (a-price[b])>0 and (a-price[b])<value:
#             #result+=[[a,price[b]]]
#             value=a-price[b]
#     counter+=1
# print(value)
################################################
def minimumLoss(price):
    # This dictionary register the original order of the years
    # so that only the difference between past years and recent years
    # are considered. This is kept in in a dictiorny and keeps track
    # with the "if prices_dict[price[i+1]]<prices_dict[price[i]]"
    prices_dict = {pr:idx for (pr,idx) in zip(price,range(len(price)))}
    # Now,it gets sorted to get the minimum differences
    price.sort()
    # Only valid minimum differences are kept.
    result=min([price[i+1]-price[i]
                for i in range(len(price)-1)
                if prices_dict[price[i+1]]<prices_dict[price[i]]])
    return result
################################################
# price=[20,15,8,2,12]
# price.sort()
# my_=[price[i+1]-price[i] for i in range(len(price)-1)]
#
#
# prices_dict = {pr:idx for (pr,idx) in zip(price,range(len(price)))}
# result=min([price[i+1]-price[i]
#                 for i in range(len(price)-1)
#                 if prices_dict[price[i+1]]<prices_dict[price[i]]])
############################
# price=[20,15,8,2,12]
# prices_dict = {pr:idx for (pr,idx) in zip(price,range(len(price)))}
# price.sort()
#
# check=[]
# for i in range(len(price)-1):
#     check+= [[price[i + 1], price[i]]]