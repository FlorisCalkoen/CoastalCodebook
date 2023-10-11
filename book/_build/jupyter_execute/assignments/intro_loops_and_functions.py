#!/usr/bin/env python
# coding: utf-8

# ![](../docs/banner.png)

# # Chapter 2: Loops & Functions

# <h2>Chapter Outline<span class="tocSkip"></span></h2>
# <hr>
# <div class="toc"><ul class="toc-item"><li><span><a href="#1.-for-Loops" data-toc-modified-id="1.-for-Loops-1">1. <code>for</code> Loops</a></span></li><li><span><a href="#2.-while-loops" data-toc-modified-id="2.-while-loops-2">2. <code>while</code> loops</a></span></li><li><span><a href="#3.-Comprehensions" data-toc-modified-id="3.-Comprehensions-3">3. Comprehensions</a></span></li><li><span><a href="#4.-try-/-except" data-toc-modified-id="4.-try-/-except-4">4. <code>try</code> / <code>except</code></a></span></li><li><span><a href="#5.-Functions" data-toc-modified-id="5.-Functions-5">5. Functions</a></span></li><li><span><a href="#6.-Functions-as--a-data-type" data-toc-modified-id="6.-Functions-as--a-data-type-6">6. Functions as  a data type</a></span></li><li><span><a href="#7.-Anonymous-functions" data-toc-modified-id="7.-Anonymous-functions-7">7. Anonymous functions</a></span></li><li><span><a href="#8.-DRY-principle,-designing-good-functions" data-toc-modified-id="8.-DRY-principle,-designing-good-functions-8">8. DRY principle, designing good functions</a></span></li><li><span><a href="#9.-Generators" data-toc-modified-id="9.-Generators-9">9. Generators</a></span></li><li><span><a href="#10.-Docstrings" data-toc-modified-id="10.-Docstrings-10">10. Docstrings</a></span></li></ul></div>

# ## Chapter Learning Objectives
# <hr>

# - Write `for` and `while` loops in Python.
# - Identify iterable datatypes which can be used in `for` loops.
# - Create a `list`, `dictionary`, or `set` using comprehension.
# - Write a `try`/`except` statement.
# - Define a function and an anonymous function in Python.
# - Describe the difference between positional and keyword arguments.
# - Describe the difference between local and global arguments.
# - Apply the `DRY principle` to write modular code.
# - Assess whether a function has side effects.
# - Write a docstring for a function that describes parameters, return values, behaviour and usage.

# ## 1. `for` Loops
# <hr>

# For loops allow us to execute code a specific number of times.

# In[1]:


for n in [2, 7, -1, 5]:
    print(f"The number is {n} and its square is {n**2}")
print("I'm outside the loop!")


# The main points to notice:
# 
# * Keyword `for` begins the loop. Colon `:` ends the first line of the loop.
# * Block of code indented is executed for each value in the list (hence the name "for" loops)
# * The loop ends after the variable `n` has taken all the values in the list
# * We can iterate over any kind of "iterable": `list`, `tuple`, `range`, `set`, `string`.
# * An iterable is really just any object with a sequence of values that can be looped over. In this case, we are iterating over the values in a list.

# In[2]:


word = "Python"
for letter in word:
    print("Gimme a " + letter + "!")

print(f"What's that spell?!! {word}!")


# A very common pattern is to use `for` with the `range()`. `range()` gives you a sequence of integers up to some value (non-inclusive of the end-value) and is typically used for looping.

# In[3]:


range(10)


# In[4]:


list(range(10))


# In[5]:


for i in range(10):
    print(i)


# We can also specify a start value and a skip-by value with `range`:

# In[6]:


for i in range(1, 101, 10):
    print(i)


# We can write a loop inside another loop to iterate over multiple dimensions of data:

# In[7]:


for x in [1, 2, 3]:
    for y in ["a", "b", "c"]:
        print((x, y))


# In[8]:


list_1 = [0, 1, 2]
list_2 = ["a", "b", "c"]
for i in range(3):
    print(list_1[i], list_2[i])


# There are many clever ways of doing these kinds of things in Python. When looping over objects, I tend to use `zip()` and `enumerate()` quite a lot in my work. `zip()` returns a zip object which is an iterable of tuples.

# In[9]:


for i in zip(list_1, list_2):
    print(i)


# We can even "unpack" these tuples directly in the `for` loop:

# In[10]:


for i, j in zip(list_1, list_2):
    print(i, j)


# `enumerate()` adds a counter to an iterable which we can use within the loop.

# In[11]:


for i in enumerate(list_2):
    print(i)


# In[12]:


for n, i in enumerate(list_2):
    print(f"index {n}, value {i}")


# We can loop through key-value pairs of a dictionary using `.items()`. The general syntax is `for key, value in dictionary.items()`.

# In[13]:


courses = {521 : "awesome",
           551 : "riveting",
           511 : "naptime!"}

for course_num, description in courses.items():
    print(f"DSCI {course_num}, is {description}")


# We can even use `enumerate()` to do more complex un-packing:

# In[14]:


for n, (course_num, description) in enumerate(courses.items()):
    print(f"Item {n}: DSCI {course_num}, is {description}")


# ## 2. `while` loops
# <hr>

# We can also use a [`while` loop](https://docs.python.org/3/reference/compound_stmts.html#while) to excute a block of code several times. But beware! If the conditional expression is always `True`, then you've got an infintite loop! 

# In[15]:


n = 10
while n > 0:
    print(n)
    n -= 1

print("Blast off!")


# Let's read the `while` statement above as if it were in English. It means, “While `n` is greater than 0, display the value of `n` and then decrement `n` by 1. When you get to 0, display the word Blast off!”
# 
# For some loops, it's hard to tell when, or if, they will stop! Take a look at the [Collatz conjecture](https://en.wikipedia.org/wiki/Collatz_conjecture). The conjecture states that no matter what positive integer `n` we start with, the sequence will always eventually reach 1 - we just don't know how many iterations it will take.

# In[16]:


n = 11
while n != 1:
    print(int(n))
    if n % 2 == 0: # n is even
        n = n / 2
    else: # n is odd
        n = n * 3 + 1
print(int(n))


# Hence, in some cases, you may want to force a `while` loop to stop based on some criteria, using the `break` keyword.

# In[17]:


n = 123
i = 0
while n != 1:
    print(int(n))
    if n % 2 == 0: # n is even
        n = n / 2
    else: # n is odd
        n = n * 3 + 1
    i += 1
    if i == 10:
        print(f"Ugh, too many iterations!")
        break


# The `continue` keyword is similar to `break` but won't stop the loop. Instead, it just restarts the loop from the top.

# In[18]:


n = 10
while n > 0:
    if n % 2 != 0: # n is odd
        n = n - 1
        continue
        break  # this line is never executed because continue restarts the loop from the top
    print(n)
    n = n - 1

print("Blast off!")


# ## 3. Comprehensions
# <hr>

# Comprehensions allow us to build lists/tuples/sets/dictionaries in one convenient, compact line of code. I use these quite a bit! Below is a standard `for` loop you might use to iterate over an iterable and create a list:

# In[19]:


subliminal = ['Tom', 'ingests', 'many', 'eggs', 'to', 'outrun', 'large', 'eagles', 'after', 'running', 'near', '!']
first_letters = []
for word in subliminal:
    first_letters.append(word[0])
print(first_letters)


# List comprehension allows us to do this in one compact line:

# In[20]:


letters = [word[0] for word in subliminal]  # list comprehension
letters


# We can make things more complicated by doing multiple iteration or conditional iteration:

# In[21]:


[(i, j) for i in range(3) for j in range(4)]


# In[22]:


[i for i in range(11) if i % 2 == 0]  # condition the iterator, select only even numbers


# In[23]:


[-i if i % 2 else i for i in range(11)]  # condition the value, -ve odd and +ve even numbers


# There is also set comprehension:

# In[24]:


words = ['hello', 'goodbye', 'the', 'antidisestablishmentarianism']
y = {word[-1] for word in words}  # set comprehension
y  # only has 3 elements because a set contains only unique items and there would have been two e's


# Dictionary comprehension:

# In[25]:


word_lengths = {word:len(word) for word in words} # dictionary comprehension
word_lengths


# Tuple comprehension doesn't work as you might expect... We get a "generator" instead (more on that later).

# In[26]:


y = (word[-1] for word in words)  # this is NOT a tuple comprehension - more on generators later
print(y)


# ## 4. `try` / `except`
# <hr>

# ![](img/chapter2/bsod.jpg)

# Above: the [Blue Screen of Death](https://en.wikipedia.org/wiki/Blue_Screen_of_Death) at a Nine Inch Nails concert! Source: [cnet.com](https://www.cnet.com/news/nine-inch-nails-depresses-with-a-big-blue-screen-of-death/).

# If something goes wrong, we don't want our code to crash - we want it to **fail gracefully**. In Python, this can be accomplished using `try`/`except`. Here is a basic example:

# In[27]:


this_variable_does_not_exist
print("Another line")  # code fails before getting to this line


# In[28]:


try:
    this_variable_does_not_exist
except:
    pass # do nothing
    print("You did something bad! But I won't raise an error.") # print something
print("Another line")


# Python tries to execute the code in the `try` block. If an error is encountered, we "catch" this in the `except` block (also called `try`/`catch` in other languages). There are many different error types, or **exceptions** - we saw `NameError` above. 

# In[29]:


5/0  # ZeroDivisionError


# In[30]:


my_list = [1,2,3]
my_list[5]  # IndexError


# In[31]:


my_tuple = (1,2,3)
my_tuple[0] = 0  # TypeError


# Ok, so there are apparently a bunch of different errors one could run into. With `try`/`except` you can also catch the exception itself:

# In[32]:


try:
    this_variable_does_not_exist
except Exception as ex:
    print("You did something bad!")
    print(ex)
    print(type(ex))


# In the above, we caught the exception and assigned it to the variable `ex` so that we could print it out. This is useful because you can see what the error message would have been, without crashing your program. You can also catch specific exceptions types. This is typically the recommended way to catch errors, you want to be specific in catching your error so you know exactly where and why your code failed.

# In[33]:


try:
    this_variable_does_not_exist  # name error
#     (1, 2, 3)[0] = 1  # type error
#     5/0  # ZeroDivisionError
except TypeError:
    print("You made a type error!")
except NameError:
    print("You made a name error!")
except:
    print("You made some other sort of error")


# The final `except` would trigger if the error is none of the above types, so this sort of has an `if`/`elif`/`else` feel to it. There is also an optional `else` and `finally` keyword (which I almost never used), but you can read more about [here](https://docs.python.org/3/tutorial/errors.html).

# In[34]:


try:
    this_variable_does_not_exist
except:
    print("The variable does not exist!")
finally:
    print("I'm printing anyway!")


# We can also write code that raises an exception on purpose, using `raise`:

# In[35]:


def add_one(x):  # we'll get to functions in the next section
    return x + 1


# In[36]:


add_one("blah")


# In[37]:


def add_one(x):
    if not isinstance(x, float) and not isinstance(x, int):
        raise TypeError(f"Sorry, x must be numeric, you entered a {type(x)}.")
        
    return x + 1


# In[38]:


add_one("blah")


# This is useful when your function is complicated and would fail in a complicated way, with a weird error message. You can make the cause of the error much clearer to the _user_ of the function. If you do this, you should ideally describe these exceptions in the function documentation, so a user knows what to expect if they call your function.
# 
# Finally, we can even define our own exception types. We do this by inheriting from the `Exception` class - we'll explore classes and inheritance more in the next chapter!

# In[39]:


class CustomAdditionError(Exception):
    pass


# In[40]:


def add_one(x):
    if not isinstance(x, float) and not isinstance(x, int):
        raise CustomAdditionError("Sorry, x must be numeric")
        
    return x + 1


# In[41]:


add_one("blah")


# ## 5. Functions
# <hr>

# A [function](https://docs.python.org/3/tutorial/controlflow.html#defining-functions) is a reusable piece of code that can accept input parameters, also known as "arguments". For example, let's define a function called `square` which takes one input parameter `n` and returns the square `n**2`:

# In[42]:


def square(n):
    n_squared = n**2
    return n_squared


# In[43]:


square(2)


# In[44]:


square(100)


# In[45]:


square(12345)


# Functions begin with the `def` keyword, then the function name, arguments in parentheses, and then a colon (`:`). The code executed by the function is defined by indentation. The output or "return" value of the function is specified using the `return` keyword.

# ### Side Effects & Local Variables
# 
# When you create a variable inside a function, it is local, which means that it only exists inside the function. For example:

# In[46]:


def cat_string(str1, str2):
    string = str1 + str2
    return string


# In[47]:


cat_string('My name is ', 'Tom')


# In[48]:


string


# If a function changes the variables passed into it, then it is said to have **side effects**. For example:

# In[49]:


def silly_sum(my_list):
    my_list.append(0)
    return sum(my_list)


# In[50]:


l = [1, 2, 3, 4]
out = silly_sum(l)
out


# The above looks like what we wanted? But wait... it changed our `l` object...

# In[51]:


l


# If your function has side effects like this, you must mention it in the documentation (which we'll touch on later in this chapter).

# ### Null Return Type
# 
# If you do not specify a return value, the function returns `None` when it terminates:

# In[52]:


def f(x):
    x + 1 # no return!
    if x == 999:
        return
print(f(0))


# ### Optional & Required Arguments
# 
# Sometimes it is convenient to have _default values_ for some arguments in a function. Because they have default values, these arguments are optional, and are hence called "optional arguments". For example:

# In[53]:


def repeat_string(s, n=2):
    return s*n


# In[54]:


repeat_string("mds", 2)


# In[55]:


repeat_string("mds", 5)


# In[56]:


repeat_string("mds") # do not specify `n`; it is optional


# Ideally, the default value for optional arguments should be carefully chosen. In the function above, the idea of "repeating" something makes me think of having 2 copies, so `n=2` feels like a reasonable default.
# 
# You can have any number of required arguments and any number of optional arguments. All the optional arguments must come after the required arguments. The required arguments are mapped by the order they appear. The optional arguments can be specified out of order when using the function.

# In[57]:


def example(a, b, c="DEFAULT", d="DEFAULT"):
    print(a, b, c, d)
    
example(1, 2, 3, 4)


# Using the defaults for `c` and `d`:

# In[58]:


example(1, 2)


# Specifying `c` and `d` as **keyword arguments** (i.e. by name):

# In[59]:


example(1, 2, c=3, d=4)


# Specifying only one of the optional arguments, by keyword:

# In[60]:


example(1, 2, c=3)


# Specifying all the arguments as keyword arguments, even though only `c` and `d` are optional:

# In[61]:


example(a=1, b=2, c=3, d=4)


# Specifying `c` by the fact that it comes 3rd (I do not recommend this because I find it is confusing):

# In[62]:


example(1, 2, 3)


# Specifying the optional arguments by keyword, but in the wrong order (this can also be confusing, but not so terrible - I am fine with it):

# In[63]:


example(1, 2, d=4, c=3)


# Specifying the non-optional arguments by keyword (I am fine with this):

# In[64]:


example(a=1, b=2)


# Specifying the non-optional arguments by keyword, but in the wrong order (not recommended, I find it confusing):

# In[65]:


example(b=2, a=1)


# Specifying keyword arguments before non-keyword arguments (this throws an error):

# In[66]:


example(a=2, 1)


# ### Multiple Return Values
# 
# In many programming languages, functions can only return one object. That is technically true in Python too, but there is a "workaround", which is to return a tuple.

# In[67]:


def sum_and_product(x, y):
    return (x + y, x * y)


# In[68]:


sum_and_product(5, 6)


# The parentheses can be omitted (and often are), and a `tuple` is implicitly returned as defined by the use of the comma: 

# In[69]:


def sum_and_product(x, y):
    return x + y, x * y


# In[70]:


sum_and_product(5, 6)


# It is common to immediately unpack a returned tuple into separate variables, so it really feels like the function is returning multiple values:

# In[71]:


s, p = sum_and_product(5, 6)


# In[72]:


s


# In[73]:


p


# As an aside, it is conventional in Python to use `_` for values you don't want:

# In[74]:


s, _ = sum_and_product(5, 6)


# In[75]:


s


# In[76]:


_


# ### Functions with Arbitrary Number of Arguments
# 
# You can also call/define functions that accept an arbitrary number of positional or keyword arguments using `*args` and `**kwargs`.

# In[77]:


def add(*args):
    print(args)
    return sum(args)


# In[78]:


add(1, 2, 3, 4, 5, 6)


# In[79]:


def add(**kwargs):
    print(kwargs)
    return sum(kwargs.values())


# In[80]:


add(a=3, b=4, c=5)


# ## 6. Functions as  a Data Type
# <hr>

# In Python, functions are actually a data type:

# In[81]:


def do_nothing(x):
    return x


# In[82]:


type(do_nothing)


# In[83]:


print(do_nothing)


# This means you can pass functions as arguments into other functions.

# In[84]:


def square(y):
    return y**2

def evaluate_function_on_x_plus_1(fun, x):
    return fun(x+1)


# In[85]:


evaluate_function_on_x_plus_1(square, 5)


# So what happened above?
# - `fun(x+1)` becomes `square(5+1)`
# - `square(6)` becomes `36`

# ## 7. Anonymous Functions
# <hr>

# There are two ways to define functions in Python. The way we've beenusing up until now:

# In[86]:


def add_one(x):
    return x+1


# In[87]:


add_one(7.2)


# Or by using the `lambda` keyword:

# In[88]:


add_one = lambda x: x+1 


# In[89]:


type(add_one)


# In[90]:


add_one(7.2)


# The two approaches above are identical. The one with `lambda` is called an **anonymous function**. Anonymous functions can only take up one line of code, so they aren't appropriate in most cases, but can be useful for smaller things.

# In[91]:


evaluate_function_on_x_plus_1(lambda x: x ** 2, 5)


# Above:
# 
# - First, `lambda x: x**2` evaluates to a value of type `function` (otice that this function is never given a name - hence "anonymous functions").
# - Then, the function and the integer `5` are passed into `evaluate_function_on_x_plus_1`
# - At which point the anonymous function is evaluated on `5+1`, and we get `36`.

# ## 8. DRY Principle, Designing Good Functions
# <hr>

# DRY stands for **Don't Repeat Yourself**. See the relevant [Wikipedia article](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) for more about this principle.
# 
# As an example, consider the task of turning each element of a list into a palindrome.

# In[92]:


names = ["milad", "tom", "tiffany"]


# In[93]:


name = "tom"
name[::-1]  # creates a slice that starts at the end and moves backwards, syntax is [begin:end:step]


# In[94]:


names_backwards = list()

names_backwards.append(names[0] + names[0][::-1])
names_backwards.append(names[1] + names[1][::-1])
names_backwards.append(names[2] + names[2][::-1])
names_backwards


# The code above is gross, terrible, yucky code for several reasons:
# 1. It only works for a list with 3 elements;
# 2. It only works for a list named `names`;
# 3. If we want to change its functionality, we need to change 3 similar lines of code (Don't Repeat Yourself!!);
# 4. It is hard to understand what it does just by looking at it.
# 
# Let's try this a different way:

# In[95]:


names_backwards = list()

for name in names:
    names_backwards.append(name + name[::-1])
    
names_backwards


# The above is slightly better and we have solved problems (1) and (3). But let's create a function to make our life easier:

# In[96]:


def make_palindromes(names):
    names_backwards = list()
    
    for name in names:
        names_backwards.append(name + name[::-1])
    
    return names_backwards

make_palindromes(names)


# Okay, this is even better. We have now also solved problem (2), because you can call the function with any list, not just `names`. For example, what if we had multiple _lists_:

# In[97]:


names1 = ["milad", "tom", "tiffany"]
names2 = ["apple", "orange", "banana"]


# In[98]:


make_palindromes(names1)


# In[99]:


make_palindromes(names2)


# ### Designing Good Functions

# How far you go and how you choose to apply the DRY principle is up to you and the programming context. These decisions are often ambiguous. Should `make_palindromes()` be a function if I'm only ever doing it once? Twice? Should the loop be inside the function, or outside? Should there be TWO functions, one that loops over the other?
# 
# In my personal opinion, `make_palindromes()` does a bit too much to be understandable. I prefer this:

# In[100]:


def make_palindrome(name):
    return name + name[::-1]

make_palindrome("milad")


# From here, if we want to "apply `make_palindrome` to every element of a list" we could use list comprehension:

# In[101]:


[make_palindrome(name) for name in names]


# There is also the in-built `map()` function which does exactly this, applies a function to every element of a sequence:

# In[102]:


list(map(make_palindrome, names))


# ## 9. Generators
# <hr>

# Recall list comprehension from earlier in the chapter:

# In[103]:


[n for n in range(10)]


# Comprehensions evaluate the entire expression at once, and then returns the full data product. Sometimes, we want to work with just one part of our data at a time, for example, when we can't fit all of our data in memory. For this, we can use *generators*.

# In[104]:


(n for n in range(10))


# Notice that we just created a `generator object`. Generator objects are like a "recipe" for generating values. They don't actually do any computation until they are asked to. We can get values from a generator in three main ways:
# - Using `next()`
# - Using `list()`
# - Looping

# In[105]:


gen = (n for n in range(10))


# In[106]:


next(gen)


# In[107]:


next(gen)


# Once the generator is exhausted, it will no longer return values:

# In[108]:


gen = (n for n in range(10))
for i in range(11):
    print(next(gen))


# We can see all the values of a generator using `list()` but this defeats the purpose of using a generator in the first place:

# In[109]:


gen = (n for n in range(10))
list(gen)


# Finally, we can loop over generator objects too:

# In[110]:


gen = (n for n in range(10))
for i in gen:
    print(i)


# Above, we saw how to create a generator object using comprehension syntax but with parentheses. We can also create a generator using functions and the `yield` keyword (instead of the `return` keyword):

# In[111]:


def gen():
    for n in range(10):
        yield (n, n ** 2)


# In[112]:


g = gen()
print(next(g))
print(next(g))
print(next(g))


# Below is some real-world motivation of a case where a generator might be useful. Say we want to create a list of dictionaries containing information about houses in Canada.

# In[113]:


import random  # we'll learn about imports in a later chapter
import time
import memory_profiler
city = ['Vancouver', 'Toronto', 'Ottawa', 'Montreal']


# In[73]:


def house_list(n):
    houses = []
    for i in range(n):
        house = {
            'id': i,
            'city': random.choice(city),
            'bedrooms': random.randint(1, 5),
            'bathrooms': random.randint(1, 3),
            'price ($1000s)': random.randint(300, 1000)
        }
        houses.append(house)
    return houses


# In[74]:


house_list(2)


# What happens if we want to create a list of 1,000,000 houses? How much time/memory will it take?

# In[75]:


start = time.time()
mem = memory_profiler.memory_usage()
print(f"Memory usage before: {mem[0]:.0f} mb")
people = house_list(500000)
print(f"Memory usage after: {memory_profiler.memory_usage()[0]:.0f} mb")
print(f"Time taken: {time.time() - start:.2f}s")


# In[76]:


def house_generator(n):
    for i in range(n):
        house = {
            'id': i,
            'city': random.choice(city),
            'bedrooms': random.randint(1, 5),
            'bathrooms': random.randint(1, 3),
            'price ($1000s)': random.randint(300, 1000)
        }
        yield house


# In[77]:


start = time.time()
print(f"Memory usage before: {mem[0]:.0f} mb")
people = house_generator(500000)
print(f"Memory usage after: {memory_profiler.memory_usage()[0]:.0f} mb")
print(f"Time taken: {time.time() - start:.2f}s")


# Although, if we used `list()` to extract all of the genertator values, we'd lose our memory savings:

# In[17]:


print(f"Memory usage before: {mem[0]:.0f} mb")
people = list(house_generator(500000))
print(f"Memory usage after: {memory_profiler.memory_usage()[0]:.0f} mb")


# ## 10. Docstrings
# <hr>

# One problem we never really solved when talking about writing good functions was: "4. It is hard to understand what it does just by looking at it". This brings up the idea of function documentation, called "docstrings". The [docstring](https://www.python.org/dev/peps/pep-0257/) goes right after the `def` line and is wrapped in **triple quotes** `"""`.

# In[78]:


def make_palindrome(string):
    """Turns the string into a palindrome by concatenating itself with a reversed version of itself."""
    
    return string + string[::-1]


# In Python we can use the `help()` function to view another function's documentation. In IPython/Jupyter, we can use `?` to view the documentation string of any function in our environment.

# In[79]:


get_ipython().run_line_magic('pinfo', 'make_palindrome')


# But, even easier than that, if your cursor is in the function parentheses, you can use the shortcut `shift + tab` to open the docstring at will.

# In[80]:


# make_palindrome('uncomment this line and try pressing shift+tab here.')


# ### Docstring Structure
# 
# General docstring convention in Python is described in [PEP 257 - Docstring Conventions](https://www.python.org/dev/peps/pep-0257/). There are many different docstring style conventions used in Python. The exact style you use can be important for helping you to render your documentation, or for helping your IDE parse your documentation. Common styles include:
# 
# 1. **Single-line**: If it's short, then just a single line describing the function will do (as above).
# 2. **reST style**: see [here](https://www.python.org/dev/peps/pep-0287/).
# 3. **NumPy style**: see [here](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html). (RECOMMENDED! and MDS-preferred)
# 4. **Google style**: see [here](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html#example-google).
# 

# The NumPy style:

# In[102]:


def function_name(param1, param2, param3):
    """First line is a short description of the function.
    
    A paragraph describing in a bit more detail what the
    function does and what algorithms it uses and common
    use cases.
    
    Parameters
    ----------
    param1 : datatype
        A description of param1.
    param2 : datatype
        A description of param2.
    param3 : datatype
        A longer description because maybe this requires
        more explanation and we can use several lines.
    
    Returns
    -------
    datatype
        A description of the output, datatypes and behaviours.
        Describe special cases and anything the user needs to
        know to use the function.
    
    Examples
    --------
    >>> function_name(3,8,-5)
    2.0
    """


# In[1]:


def make_palindrome(string):
    """Turns the string into a palindrome by concatenating 
    itself with a reversed version of itself.
    
    Parameters
    ----------
    string : str
        The string to turn into a palindrome.
        
    Returns
    -------
    str
        string concatenated with a reversed version of string
        
    Examples
    --------
    >>> make_palindrome('tom')
    'tommot'
    """
    return string + string[::-1]


# In[2]:


get_ipython().run_line_magic('pinfo', 'make_palindrome')


# ### Docstrings with Optional Arguments
# 
# When specifying function arguments, we specify the defaults for optional arguments:

# In[81]:


# scipy style
def repeat_string(s, n=2):
    """
    Repeat the string s, n times.
    
    Parameters
    ----------
    s : str 
        the string
    n : int, optional
        the number of times, by default = 2
        
    Returns
    -------
    str
        the repeated string
        
    Examples
    --------
    >>> repeat_string("Blah", 3)
    "BlahBlahBlah"
    """
    return s * n


# ### Type Hints

# [Type hinting](https://docs.python.org/3/library/typing.html) is exactly what it sounds like, it hints at the data type of function arguments. You can indicate the type of an argument in a function using the syntax `argument : dtype`, and the type of the return value using `def func() -> dtype`. Let's see an example:

# In[83]:


# NumPy style
def repeat_string(s: str, n: int = 2) -> str:  # <---- note the type hinting here
    """
    Repeat the string s, n times.
    
    Parameters
    ----------
    s : str 
        the string
    n : int, optional (default = 2)
        the number of times
        
    Returns
    -------
    str
        the repeated string
        
    Examples
    --------
    >>> repeat_string("Blah", 3)
    "BlahBlahBlah"
    """
    return s * n


# In[84]:


get_ipython().run_line_magic('pinfo', 'repeat_string')


# Type hinting just helps your users and IDE identify dtypes and identify bugs. It's just another level of documentation. They do not force users to use that date type, for example, I can still pass an `dict` to `repeat_string` if I want to:

# In[85]:


repeat_string({'key_1': 1, 'key_2': 2})


# Most IDE's are clever enough to even read your type hinting and warn you if you're using a different dtype in the function, e.g., this VScode screenshot:

# ![](img/chapter2/type_hint_1.png)
# ![](img/chapter2/type_hint_2.png)
