from arepl_dump import dump 




place = ['new york', 'singapo','tokyo','ha noi','pari']
#1
print('*'*10+'1'+10*'*')
print('\n'.join(place))

#2
print('*'*10+'2'+10*'*')
print('\n'.join(sorted(place)))

#3
print('*'*10+'3'+10*'*')
print('\n'.join(place))

#4
print('*'*10+'4'+10*'*')
print('\n'.join(sorted(place,reverse=True)))

#5
print('*'*10+'5'+10*'*')
place.reverse()
print('\n'.join(place))

#6
print('*'*10+'6'+10*'*')
place.reverse()
print('\n'.join(place))

#7
print('*'*10+'7'+10*'*')
place.sort()
print('\n'.join(place))

#8
print('*'*10+'8'+10*'*')
place.sort(reverse=True)
print('\n'.join(place))


#ex2


arr = [1, 3, 5, 'a', 'c', 'b']
print(arr)
# 1
arr.pop(-1)
print(arr)
arr.insert(3, 10)
print(arr)
arr[0] = 'python'
print(arr)
# 2
arr[0], arr[-1] = arr[-1], arr[0]
print(arr)
# 3
sum_arr = 0
avg_arr = 0
c = 0
for i in arr:
    if(type(i) == int):
        sum_arr += i
        c += 1
avg_arr = sum_arr/c
print(sum_arr, avg_arr)
# 4
num_arr = [i for i in arr if type(i) == int]
for i in range(len(num_arr)):
    if(type(num_arr[i]) == int):
        num_arr[i] = num_arr[i]**2
num_arr.sort(reverse=True)
print(num_arr)
# 5
print(len(set(arr)))
