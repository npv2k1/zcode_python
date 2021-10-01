def checkPalindromeB(N, B):

    # Stores the reverse of N
    rev = 0

    # Stores the value of N
    N1 = N

    # Extract all the digits of N
    while (N1 > 0):

        # Generate its reverse
        rev = rev * B + N1 % B
        N1 = N1 // B

    return N == rev


a, b, m = list(map(int, input().split()))

arr = range(a, b+1)
# Duyệt các cơ số

# for base in range(2, m+1):
#     arr_tmp = []
#     for i in arr:
#         if(checkPalindromeB(i, base)):
#             arr_tmp.append(i)
#     arr = arr_tmp
#     if(len(arr) == 0):
#         break
c = 0
for i in arr:
    ok = True
    for base in range(i-1, m+1):
        print(checkPalindromeB(i, base))
        # if(not checkPalindromeB(i,base)):
        #     ok = False
        #     break
    if(ok):
        c += 1


print(c)
