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
print('--------------------')
def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(57)
print(f(0))
print(f(43))
print(f(12))

print('--------------------')
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five')]
pairs.sort(key = lambda pair: pair[1])
print(pairs)

print('--------------------')
def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass

print(my_function.__doc__)

print('--------------------')
squares = []
for x in range(10):
    squares.append(x**2)

print(squares)

print('--------------------')
squares = list(map(lambda x: x**2, range(10)))
print(squares)

print('--------------------')
squares = [x**2 for x in range(10)]
print(squares)

print('--------------------')
print([(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y])

print('--------------------')
combs = []
for x in [1, 2, 3, 4, 5]:
    for y in [5, 2, 4, 3, 1]:
        if x != y:
            combs.append((x, y))

print(combs)

print('--------------------')
vec = [-4, -2, 0, 2, 4]
print([x**2 for x in vec])
print([x for x in vec if x >= 0])
print([abs(x) for x in vec])
freshfruit = [' banana', '  loganberry', 'passion fruit ']
print([weapon.strip() for weapon in freshfruit])
print([(x, x**2) for x in range(6)])
vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([num for elem in vec for num in elem])

print('--------------------')
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

print([[row[i] for row in matrix] for i in range(4)])

print('--------------------')
basket = { 'apple', 'orange', 'apple', 'pear', 'orange', 'pear', 'banana' }
print(basket)

print('apple' in basket)
print('pear' in basket)
print('banana' in basket)
print('crabgrass' in basket)
print('mango' in basket)

print('--------------------')
a = set('abracadabra')
b = set('alacazam')

print(a)
print(a - b)
print(a | b)
print(a & b)
print(a ^ b)

print('--------------------')
tel = {
    'jack': 4098,
    'sape': 4139
}

tel['guido'] = 4127
print(tel)
print(tel['jack'])
print(tel['sape'])
del tel['sape']
tel['irv'] = 4127
print(tel)
print(list(tel))
print(sorted(tel))
print('guido' in tel)
print('jack' in tel)

new_dictionary_A = dict([('A', 0000), ('B', 1111), ('C', 2222), ('D', 3333)])
print(new_dictionary_A)
new_dictionary_B = { x: x**2 for x in (2, 4, 6, 8, 10) }
print(new_dictionary_B)
new_dictionary_C = dict(sape=4139, guido=4127, jack=4098)
print(new_dictionary_C)

#Looping techniques:

#1. Looping through dictionaries:
print('--------------------')
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

#2. Looping through sequences:
print('--------------------')
for i, v in enumerate(['Sun', 'Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Mercury', 'Pluto']):
    print(i, v)

#3. Looping through few sequences at the same time:
print('--------------------')
questions = ['name', 'position', 'polar radius', 'classification', 'surface gravity']
answers = ['Uranus', 7, '24973km', 'Gas giant', '8.69m/s2']
for q, a in zip(questions, answers):
    print('What is your {0}? - It is {1}.'.format(q, a))

#4. Looping over a sequence in reverse direction:
print('--------------------')
for i in reversed(range(1, 20, 2)):
    print(i)

#5. Looping over a sequence in sorter order:
print('--------------------')
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)

#6. Looping and changing values of list:
print('--------------------')
import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

print(filtered_data)

#Conditions:

#1. Assigning the result of comparison to the variable:
print('--------------------')
string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
print(non_null)

#Comparing sequences and other types:

#1. Few examples of comparing the same types of sequences:
print('--------------------')
print( (1, 2, 3) < (1, 2, 3) )
print( [1, 2, 3] < [1, 2, 4] )
print( 'ABC' < 'C' < 'Pascal' < 'Python' )
print( (1, 2, 3, 4) < (1, 2, 4) )
print( (1, 2) < (1, 2, -1) )
print( (1, 2, 3) == (1.0, 2.0, 3.0) )
print( (1, 2, ('aa', 'ab')) < (1, 2, ('ab', 'a'), 4) )

#Input and Output:

#1. Using formatted string literals:
print('--------------------')
year = 2235
event = 'Referendum'
country = 'Galactic Earth Empire'

#2 Using str.format():
print('--------------------')
yes_votes = 42572654
no_votes = 43132495
percentage = yes_votes / (yes_votes + no_votes)
print('{:-9} YES votes {:2.2%}'.format(yes_votes, percentage))

#3 Using str() and repr():
print('--------------------')
s = 'Hello, World!'
str(s)
repr(s)
str(1/7)
x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)
hello = 'hello, world\n'
hellos = repr(hello)
print(hellos)
repr((x, y, ('spam', 'eggs')))

#4 Basic usage of str.format() method:
print('--------------------')
print('We are the {} who say "{}!"'.format('knights', 'Ni'))

#5 Using numbers on the str.format():
print('--------------------')
print('--------------------')
print('{0} and {1}'.format('spam', 'eggs'))
print('{1} and {0}'.format('spam', 'eggs'))

#6 Using keywords om the str.format():
print('--------------------')
print('This {food} is {adjective}'.format(food='spam', adjective='absolutely horrible'))

#7 Using combination of keywords and numbers on the str.format():
print('--------------------')
print('The story of {0}, {1} and {other}'.format('Bill', 'Manfred', other='Melinda'))

#8 Using dictionary and square brackets for accesing keys of str.format():
print('--------------------')
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; ' 'Dcab: {0[Dcab]:d}'.format(table))

#9 Using **syntax of dict for accesing the whole data:
print('--------------------')
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))

#10 Creating a new tidily-aligned columns of data:
print('--------------------')
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

#11 Manual string formatting:
print('--------------------')
for x in range(1, 20):
    print(repr(x).rjust(2), repr(x*x).rjust(3))
    print(repr(x*x*x).rjust(4))

#12 Using zfill() function for numeric string filling:
print('--------------------')
print('12'.zfill(5))
print('-3.14'.zfill(7))
print('3.14159265359'.zfill(5))

#Exceptions and Error Handling:

#1 Syntax Errors:
#print('--------------------')
#while True:
   #print('Simple Error Example...')

#2 Exceptions handling:
#print('--------------------')
#10 * (1/0)
#print('--------------------')
#4 + spam * 3
#print('--------------------')
#'3' * 3 / 2

#3 Handling Exceptions using user interruptions:
print('--------------------')
while True:
  try:
    x = int(input('Please enter a number:'))
    break
  except ValueError:
    print('Oops! That was no valid number. Try again...')

#4 Creating multiple names of exceptions on the tuples:
print('--------------------')
while True:
  try:
    y = int(input('Please enter a number:'))
    break
  except (RuntimeError, TypeError, NameError, ValueError):
    print('Oops! That was no valid number. Try again...')

#5 Handling multiple excepts clauses:
print('--------------------')
class B(Exception):
  pass

class C(B):
  pass

class D(C):
  pass

for cls in [B, C, D]:
  try:
    raise(cls)
  except D:
    print('D')
  except C:
    print('C')
  except B:
    print('B')

#7 Testing multiple excepts clauses with empty name of last clause:
print('--------------------')
'''
import sys

try:
  f = open('myfile.txt')
  s = f.readline()
  i = int(s.strip())
except OSError as err:
  print("OS Error: {0}".format(err))
except ValueError:
  print("Could not convert data to an integer.")
except:
  print('Unexpected error:', sys.exc_info()[0])
'''

#8 Using else clause for handling try execution clause:
print('--------------------')
import sys

for arg in sys.argv[1:]:
  try:
    f = open(arg, 'r')
  except OSError:
    print('cannot open', arg)
  else:
    print(arg, 'has', len(f.readlines()), 'lines')
    f.close()

#9 Creating an instance variable:
print('--------------------')
try:
  raise Exception('spam', 'eggs')
except Exception as inst:
  print(type(inst))
  print(inst.args)
  print(inst)
  x, y = inst.args
  print('x = ', x)
  print('y = ', y) 

#10 Handling exceptions on the function definition:
'''
print('--------------------')
def this_fails():
  x = 1/0

try:
  this_fails()
except ZeroDivisionError as err:
  print('Handling run-time error:', err)

#11 Simple example raising of exception without handling it:
try:
  raise NameError('HiThere')
except NameError:
  print('An exception flew by!')
  raise

'''

#11 User defined exceptions:

class Error(Exception):
  """Base class for exceptionsin this module."""
  pass

class InputError(Error):
  def __init__(self, expression, message):
    self.expression = expression
    self.message = message

class TransitionError(Error):
  def __init__(self, previous, next, message):
    self.previous = previous
    self.next = next
    self.message = message

#12 Defining a clean-up actions:s
'''
print('--------------------')
try:
  raise KeyboardInterrupt
finally:
  print('Goodbye, world!')
'''

#13 Defining a few examples of finally clause:
print('--------------------')
def divide(x, y):
  try:
    result = x / y
  except ZeroDivisionError:
    print('division by zero!')
  else:
    print('result is', result)
  finally:
    print('executing finally clause')

#14 Testing opening a selected file from the file system (without clean-up actions):
print('--------------------')
for line in open('test-python.txt'):
  print(line, end="")

#15 Testing predefined clean-up actions when open a file:
print('\n--------------------')
with open('test-python.txt') as f:
  for line in f:
    print(line, end="")
