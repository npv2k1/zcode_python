s = input()
num_upper = 0
num_lower = 0
for i in s:
    if(i >= 'a'):
        num_lower += 1
    elif(i >= 'A'):
        num_upper += 1
if(num_upper > num_lower):
    print(s.upper())
else:
    print(s.lower())
