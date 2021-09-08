def is_prime(n: int):
    """Primality test using 6k+-1 optimization."""
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
n = int(input())
arr = list(map(int, input().split()))

total_step=[0]

for i in arr:
    if(not is_prime(i)):
        # print(i)
        i_left=i
        i_right=i
        while(not is_prime(i_left) and not is_prime(i_right)):
            i_left-=1
            i_right+=1
        step=min(i-i_left,i_right-i)
        total_step.append(step)

   
print(max(total_step))
