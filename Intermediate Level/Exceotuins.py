###########################################

a = 5 print(a)

###########################################

a = 5 + '10'

###########################################

x = -5
if x < 0:
    raise Exception('x should not be negative')

##########################################

# This will catch all possible exceptions
try:
    a = 5 / 0
except:
    print('some error occured.')
    
# You can also catch the type of exception
try:
    a = 5 / 0
except Exception as e:
    print(e)
    
# It is good practice to specify the type of Exception you want to catch.
# Therefore, you have to know the possible errors
try:
    a = 5 / 0
except ZeroDivisionError:
    print('Only a ZeroDivisionError is handled here')
    
# You can run multiple statements in a try block, and catch different possible exceptions
try:
    a = 5 / 1 # Note: No ZeroDivisionError here
    b = a + '10'
except ZeroDivisionError as e:
    print('A ZeroDivisionError occured:', e)
except TypeError as e:
    print('A TypeError occured:', e)

##########################################

try:
    a = 5 / 1
except ZeroDivisionError as e:
    print('A ZeroDivisionError occured:', e)
else:
    print('Everything is ok')

##########################################

try:
    a = 5 / 1 # Note: No ZeroDivisionError here
    b = a + '10'
except ZeroDivisionError as e:
    print('A ZeroDivisionError occured:', e)
except TypeError as e:
    print('A TypeError occured:', e)
else:
    print('Everything is ok')
finally:
    print('Cleaning up some stuff...')

##########################################

# ImportError
import nonexistingmodule

# NameError
a = someundefinedvariable

# FileNotFoundError
with open('nonexistingfile.txt') as f:
    read_data = f.read()

# ValueError
a = [0, 1, 2]
a.remove(3)

# TypeError
a = 5 + "10"

# IndexError
a = [0, 1, 2]
value = a[5]

# KeyError
my_dict = {"name": "Max", "city": "Boston"}
age = my_dict["age"]

##########################################

# minimal example for own exception class
class ValueTooHighError(Exception):
    pass

# or add some more information for handlers
class ValueTooLowError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def test_value(a):
    if a > 1000:
        raise ValueTooHighError('Value is too high.')
    if a < 5:
        raise ValueTooLowError('Value is too low.', a) # Note that the constructor takes 2 arguments here
    return a

try:
    test_value(1)
except ValueTooHighError as e:
    print(e)
except ValueTooLowError as e:
    print(e.message, 'The value is:', e.value)

##########################################