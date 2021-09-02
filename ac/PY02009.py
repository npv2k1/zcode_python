t = int(input())
while t:
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(int(input()))
    # print(arr)
    dic = {}
    for i in arr:
        if(dic.get(i, -1) == -1):
            dic[i] = 1
        else:
            dic[i] += 1
    m_key = 1000
    m_value = 0
    for (key, value) in dic.items():
        if(value > m_value):
            m_value = value
            m_key = key
        if(m_value==value and key<m_key):            
            m_key = key
    print(m_key)
    t -= 1
