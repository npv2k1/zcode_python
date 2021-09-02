# def solve(n):
#     n = list(input().strip().lstrip('0'))
#     d = n.copy()
#     for i in range(len(n)-1, 0, -1):
#         if(int(n[i-1])-int(n[i]) > 0):
#             n[i], n[i-1] = n[i-1], n[i]
#             break
    # print(n,d)
   
def solve(n):
    n = list(map(int,n.strip().lstrip('0')))
    d = n.copy()
    current=0
    for i in range(len(n)-1, 0, -1):
        # print(n[i-1] , n[i])
        if(n[i-1]>n[i]):
            for j in range(len(n)-1,i-1,-1):
                if(n[j]<n[i-1]):
                    n[j],n[i-1]=n[i-1],n[j]
                    break            
            break
    if(n[0] == 0 or n == d):
        return(-1)
    else:
        return(''.join(map(str,n)))


print(solve('998'))
print(solve('354'))
print(solve('100'))
print(solve('111011'))
#991469126
#991466129


#991465126 -> trong dãy giảm tìm số đang tăng. ->5 tìm đoạn cuối số lớn nhất nhỏ hơn nó rồi swap
#991462156
#991461526

#991465216

#354
#345
