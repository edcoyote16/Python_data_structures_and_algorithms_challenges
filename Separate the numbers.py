#s='59257246870315695925724687031570'
#s='99910001001'
#s='7891011'
#s = '9899100'
#s='999100010001'
#s='13'
#s='010203'
#s='10001001100210031004100510061007'
s='999100010001'

s = [int(b) for b in s]
length = len(s)
digits_found = 0
for index_a, a in enumerate(s):
    first_number=s[0:index_a]
    length_of_first_number=len(first_number)
    second_number=s[index_a:index_a+len(s[0:index_a])]
    length_of_second_number = len(second_number)
    if length == 1:
        print('NO')
        break
    elif length_of_first_number>0:

        try:
            first_number=int(''.join(map(str, first_number)))
        except ValueError:
            pass
        try:
            second_number=int(''.join(map(str, second_number)))
        except ValueError:
            pass
        try:
            nines=int('9' * length_of_first_number)
        except ValueError:
            pass
        if second_number-first_number==1 and first_number==0:
            print('NO')
            break
        elif second_number-first_number==1:
            print('YES {}'.format(first_number))
            break
        elif second_number == nines or first_number == nines:

            try:
                if first_number == nines:

                    second_number = s[index_a:index_a + len(s[0:index_a])+1]
                    second_number = int(''.join(map(str, second_number)))
                    #second_number = int(''.join(map(str, second_number)))
                    if second_number-first_number==1:
                        print('YES {}'.format(first_number))
                        break
                elif second_number==nines:
                    third_number = s[index_a+length_of_second_number:index_a + len(s[0:index_a])+length_of_second_number+1]
                    third_number = int(''.join(map(str, third_number)))
                    if third_number - second_number == 1:
                        print('YES {}'.format(first_number))
                        break


            except NameError:
                pass
            #print('Yes {}'.format(first_number))
            # if len([int(b) for b in list(str(second_number))]) + len([int(e) for e in list(str(first_number))]) == length:
            #     pass
        # elif second_number-first_number==1:
        #     print('Yes {}'.format(first_number))
else:
    print('NO')
        #
        #     break
#print('NO')



