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

def ask_ok(propmt, retries=4, reminder='Please, try again!'):
    while True:
        ok = input(propmt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

print('--------------------')
# print('#3 Calling the defined fucntion:')
# ask_ok('OK to overwrite the file', 2, 'Come on, only yes or no!')
i = 5
def f(arg=i):
    print(arg)

i = 6
f()
print('--------------------')
def f_2(a, L=[]):
    L.append(a)
    return L

print(f_2(1))
print(f_2(2))
print(f_2(3))

print('--------------------')
def f_3(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f_3(1))
print(f_3(2))
print(f_3(3))

print('--------------------')
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.", "It's really very, VERY runny, sir.", shopkeeper="Michael Palin", client="John Cleese", sketch="Cheese Shop Sketch")

print('--------------------')
def concat(sep="/", *args):
    return sep.join(args)

concat("earth", "mars", "venus")

print('--------------------')
print(list(range(3, 6)))
args = [3, 6]
print(list(range(*args)))

print('--------------------')
def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action)
    print("if you put", voltage, "volts through it.")
    print("E's", state, "!")

data = {
    "voltage": "5356222",
    "state": "bleedin' demised",
    "action": "VOOM"
}

parrot(**data)