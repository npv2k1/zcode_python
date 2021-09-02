
# def solve(n):
#     n = list(map(int, n.strip().lstrip('0')))
#     d = n.copy()
#     for i in range(len(n)-1, 0, -1):
#         # print(n[i-1] , n[i])
#         if(n[i-1] > n[i]):
#             for j in range(len(n)-1, i-1, -1):
#                 if(n[j] < n[i-1]):
#                     n[j], n[i-1] = n[i-1], n[j]
#                     break
#             break

#     # số 0 bị lên đầu hoặc chuối mới bằng chuỗi cũ
#     if(n[0] == 0 or n >= d):
#         return(-1)
#     else:
#         return(''.join(map(str, n)))
# t = int(input())
# for tt in range(t):
#     print(solve(input()))


#! new solution

# Python3 tìm số lớn nhất nhỏ hơn n chỉ với 1 lần swap

import sys


def prevNum(string, n):
    index = -1

    # tìm index số tăng trong dãy giảm  -> 123451234 -> kết quả là index số 5
    for i in range(n - 2, -1, -1):
        if int(string[i]) > int(string[i + 1]):
            index = i
            break

    # We can also use binary search here as
    # digits after index are sorted in
    # increasing order.
    # Find the biggest digit in the right of
    # arr[index] which is smaller than arr[index]
    smallGreatDgt = -1
    for i in range(n - 1, index, -1):
        if (smallGreatDgt == -1 and int(string[i]) < int(string[index])):
            smallGreatDgt = i
        elif (index > -1 and int(string[i]) >= int(string[smallGreatDgt]) and int(string[i]) < int(string[index])):
            smallGreatDgt = i

    # If index is -1 i.e. digits are
    # in increasing order.
    if index == -1:
        return "" . join("-1")
    else:

        # Swap both values
        (string[index],  string[smallGreatDgt]) = (
            string[smallGreatDgt],  string[index])
    if(string[0] == '0'):
        return "-1"
    else:
        return "" . join(string)


# Driver Code
if __name__ == '__main__':

    t = int(input())
    for tt in range(t):
        n_str = input().strip()
        print(prevNum(list(n_str), len(n_str)))

# https://www.geeksforgeeks.org/largest-smaller-number-possible-using-one-swap-operation/
