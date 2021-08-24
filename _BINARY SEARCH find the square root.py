def Sqrt(Num):
    # Base cases
    if (Num == 0 or Num == 1):
        return Num
        # Do Binary Search for(sqrt(Num))
    start = 1
    end = Num
    while (start <= end):
        mid = (start + end) // 2
        # If Num is a perfect square
        if (mid * mid == Num):
            return mid
            # when mid*mid is smaller
        # than x , move closer to sqrt(x)
        if (mid * mid < Num):
            start = mid + 1
            answer = mid
        else:
            # If mid*mid is greater than Num
            end = mid - 1
    return answer
print(Sqrt(10))