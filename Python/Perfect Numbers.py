# Find perfect numbers
count = 0
max_number = int(input('Up to what value would you like to find the perfect numbers?  '))
lastFactor = 0
for n in range(1,max_number+1):
    factor_sum = 0
    for i in range(1,int(n/2)+1):
        if i!= 0:
            if n % i == 0:
                factor_sum += i
    if factor_sum  == n:
        print(n, ' is a perfect number!')
