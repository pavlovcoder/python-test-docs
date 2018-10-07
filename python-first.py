# The range() Function:
print('--------------------')
for i in range(5):
    print(i)

print('--------------------')
for i in range(5, 10):
    print(i)

print('--------------------')
for i in range(4, 34, 3):
    print(i)

print('--------------------')
for i in range(-10, -100, -20):
    print(i)

print('--------------------')
ww2_politician = ['Joseph', 'Adolf', 'Vladimir', 'Winston', 'John']
for i in range(len(ww2_politician)):
    print(i, ww2_politician[i])

print('--------------------')
print(range(33))

print('--------------------')
generated_list = list(range(7))
print(generated_list)

print('--------------------')
for n in range(2, 30):
    for x in range(2, n):
        if n % x == 0:
            print(n, ' = ', x, '*', n//x)
            break
    else:
        print(n, '- is a prime number.')

print('--------------------')
for num in range(2, 10):
    if num % 2 == 0:
        print('Found an even number', num)
        continue
    print('Found a number', num)
