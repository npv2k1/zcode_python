
# xoay ký tự c đi k đơn vị
def rotate_char(c, k):
    return chr((ord(c)-ord('A')+k) % 26+ord('A'))

# xoay chuỗi s
def rotate(s):
    k = 0
    s = list(s)
    for i in range(len(s)):
        k += ord(s[i])-ord('A')
    for i in range(len(s)):
        s[i] = rotate_char(s[i], k)

    s = ''.join(s)
    return s

# drm
def drm(s):
    left_s = s[:len(s)//2]
    right_s = s[len(s)//2:]
    left_s = rotate(left_s)
    right_s = rotate(right_s)
    res = ['']*len(left_s)
    for i in range(len(left_s)):
        res[i] = rotate_char(left_s[i], ord(right_s[i])-ord('A'))
    return ''.join(res)


t = int(input())
while t:
    print(drm(input()))
    t -= 1
