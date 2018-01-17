There are 33 keywords in Python 3.3.

All the keywords except True, False and None are in lowercase and they must be
written as it is.

Keywords in Python programming language:
False       class       finally   is        return
None        continue    for       lambda    try
True        def         from      nonlocal  while
and         del         global    not       with
as          elif        if        or        yield
assert      else        import    pass
break       except      in        raise


We can make a statement extend over multiple lines with the line continuation character (\).
For example:

a = 1 + 2 + 3 + \
    4 + 5 + 6 + \
    7 + 8 + 9

Line continuation is implied inside parentheses ( ), brackets [ ] and braces { }.
For example:

a = (1 + 2 + 3 +
    4 + 5 + 6 +
    7 + 8 + 9)

colors = ['red',
          'blue',
          'green']


Docstring is available to us as the attribute __doc__ of the function.
Issue the following code in shell once you run the above program.
>>> print(double.__doc__)
    => Function to double the value


# MULTIPLE ASSIGNMENT IN PYTHON

a, b, c = 5, 3.2, "Hello"
a = b = c = "same"


# VARIABLE TYPE

type():  function to know which class a variable or a value belongs toself.
isinstance(): function to check if an object belongs to a particular class.

For example:
    type("suyash") => <type 'str'>
    isinstance("suyash", int) => False
    isinstance("suyash", str) => True
Numbers can be either int, float or complex


Lists are mutable while tuples are immutable.
    lst[0:3] returns a list from index 0 to 2. Exclusive of the lastself.


# STRINGS ARE IMMUTABLE AND HENCE ARE NOT LIKE LISTS


# TYPE CONVERSION
int('25')
int(23.23)
str(232.3)
float('32')
set([1,2,3,4])

tuple([1,2,3])
list((1,2,3))
list({1:'a', 2:'b', 3:'c', 4:'d'})
    => return a list of the keys
list({1, 2, 3})

# dict takes in a list of pairs or a tuple of pairs and the pairs can be either
# lists or tuples. Pretty flexible!
dict([[1,2],[3,4]])
dict([(3,26),(4,44)])


# PRINT FORMATTING & INPUTS
print('I love {0} and {1}'.format('bread','butter')) # Can use indexes
print('I love {} and {}'.format('bread','butter'))
# Output: I love bread and butter

input("Write prompt here...") takes in an input. Need to convert that from a string.

eval("string to be evaluated")
THIS FUNCTION IS JUST META. ITS PYTHON INSIDE PYTHON. IT EVALUATES THE STRING PASSED TO IT.
So, if the string from input is "[1,2,3]", eval(input_string) will give the list [1,2,3].


# QUEUE IN PYTHON
from collections import deque
queue = deque(["Ram", "Tarun", "Asif", "John"])
queue.append("Akbar")
queue.append("Birbal")
print(queue.popleft())
print(queue.popleft())
print(queue)


# SETS
Python sets cannot contain mutable objects like sets dictionaries or lists.

set = {} is wrong. This creates a empty dictionary.
To make an empty set, use `k = set()`

Adding to set:
    .add()
    .update()
        hash = {1:3, 12:5, 7:11}
        s1.update(hash)
            => This adds only the keys to the set. To add values, use update(hash.values())

Remove from set:
    discard(): will not raise an exception if element not found
    remove():  will raise exception if element not found
    pop():     will remove a random element. KeyError if set is empty

.copy():    makes a copy of the set       # Can't copy a list in the same way

.isdisjoint(s2)
.issubset  (s2)
.issuperset(s2)

.union(s2)
.s1 | s2: union

.intersection(s2)
.s1 & s2: intersection

.difference(s2)
.s1 - s2: difference
    => This is s1 - the intersection(s1, s2)

.symmetric_difference(s2)
.s1 ^ s2: symmetric difference
    => This is (s1 + s2) - the intersection(s1, s2)
       Basically all the elements that exist in the two sets but not in their union

Membership test:
    a in s1
        => Checks if a is in set s1


all():	      Return True if all elements of the set are true (or if the set is empty).
any():	      Return True if any element of the set is true. If the set is empty, return False.
enumerate():  Return an enumerate object. It contains the index and value of all the items of set as a pair.
len():	      Return the length (the number of items) in the set.
max():	      Return the largest item in the set.
min():	      Return the smallest item in the set.
sorted():	  Return a new sorted list from elements in the set(does not sort the set itself).
sum(s1):	  Return the sum of all elements in the set


# RANGE
range(6)         => [0, 1, 2, 3, 4, 5]
range(0, 6)      => [0, 1, 2, 3, 4, 5]
range(0, 6, 2)   => [0, 2, 4]

# DICTIONARY

# Delete:
dict.pop(4))
del dict[5]
    => Deletes item with key 4.
    => Throws KeyError is key is not in dict

dict.popitem())
    => Remove an arbitrary item from dict

dict.clear()

del dict
    => Deletes the dictionary
    => print dict will throw Error

# Dictionary Comprehension:
squares = {x: x*x for x in range(6)}


# Converting between Integer and String
int('12312')
str(232313)
