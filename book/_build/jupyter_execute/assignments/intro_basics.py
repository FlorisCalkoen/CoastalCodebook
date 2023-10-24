#!/usr/bin/env python
# coding: utf-8

# ![](../docs/banner.png)

# # Chapter 1: Python Basics

# <h2>Chapter Outline<span class="tocSkip"></span></h2>
# <hr>
# <div class="toc"><ul class="toc-item"><li><span><a href="#1.-Introduction" data-toc-modified-id="1.-Introduction-1">1. Introduction</a></span></li><li><span><a href="#2.-Basic-Python-Data-Types" data-toc-modified-id="2.-Basic-Python-Data-Types-2">2. Basic Python Data Types</a></span></li><li><span><a href="#3.-Lists-and-Tuples" data-toc-modified-id="3.-Lists-and-Tuples-3">3. Lists and Tuples</a></span></li><li><span><a href="#4.-String-Methods" data-toc-modified-id="4.-String-Methods-4">4. String Methods</a></span></li><li><span><a href="#5.-Dictionaries" data-toc-modified-id="5.-Dictionaries-5">5. Dictionaries</a></span></li><li><span><a href="#6.-Empties" data-toc-modified-id="6.-Empties-6">6. Empties</a></span></li><li><span><a href="#7.-Conditionals" data-toc-modified-id="7.-Conditionals-7">7. Conditionals</a></span></li></ul></div>

# ## Chapter Learning Objectives
# <hr>

# - Create, describe and differentiate standard Python datatypes such as `int`, `float`, `string`, `list`, `dict`, `tuple`, etc.
# - Perform arithmetic operations like `+`, `-`, `*`, `**` on numeric values.
# - Perform basic string operations like `.lower()`, `.split()` to manipulate strings.
# - Compute boolean values using comparison operators operations (`==`, `!=`, `>`, etc.) and boolean operators (`and`, `or`, `not`).
# - Assign, index, slice and subset values to and from tuples, lists, strings and dictionaries.
# - Write a conditional statement with `if`, `elif` and `else`.
# - Identify code blocks by levels of indentation.
# - Explain the difference between mutable objects like a `list` and immutable objects like a `tuple`.

# ## 1. Introduction
# <hr>

# The material presented on this website assumes no prior knowledge of Python. Experience with programming concepts or another programming language will help, but is not required to understand the material.
# 
# The website comprises the following:
# 1. **Chapters**: these contain the core content. Read through these at your leisure.
# 2. **Practice Exercises**: there are optional practice exercise sets to complement each chapter (solutions included). Try your hand at these for extra practice and to help solidify concepts in the **Chapters**.

# ## 2. Basic Python Data Types
# <hr>

# A **value** is a piece of data that a computer program works with such as a number or text. There are different **types** of values: `42` is an integer and `"Hello!"` is a string. A **variable** is a name that refers to a value. In mathematics and statistics, we usually use variable names like $x$ and $y$. In Python, we can use any word as a variable name as long as it starts with a letter or an underscore. However, it should not be a [reserved word](https://docs.python.org/3.3/reference/lexical_analysis.html#keywords) in Python such as `for`, `while`, `class`, `lambda`, etc. as these words encode special functionality in Python that we don't want to overwrite!
# 
# It can be helpful to think of a variable as a box that holds some information (a single number, a vector, a string, etc). We use the **assignment operator** `=` to assign a value to a variable.
# 
# ![](img/chapter1/box.png)
# 
# Image modified from: [medium.com](https://www.google.com/url?sa=i&url=https%3A%2F%2Fmedium.com%2F%40stevenpcurtis.sc%2Fwhat-is-a-variable-3447ac1331b9&psig=AOvVaw3YbYfgb7XFOJ_sHP5eliob&ust=1595365663851000&source=images&cd=vfe&ved=0CA0QjhxqFwoTCMi8nrfe3OoCFQAAAAAdAAAAABAZ)
# 
# ```{tip}
# See the [Python 3 documentation](https://docs.python.org/3/library/stdtypes.html) for a summary of the standard built-in Python datatypes.
# ```

# ### Common built-in Python data types
# 
# | English name          | Type name  | Type Category  | Description                                   | Example                                    |
# | :-------------------- | :--------- | :------------- | :-------------------------------------------- | :----------------------------------------- |
# | integer               | `int`      | Numeric Type   | positive/negative whole numbers               | `42`                                       |
# | floating point number | `float`    | Numeric Type   | real number in decimal form                   | `3.14159`                                  |
# | boolean               | `bool`     | Boolean Values | true or false                                 | `True`                                     |
# | string                | `str`      | Sequence Type  | text                                          | `"I Can Has Cheezburger?"`                 |
# | list                  | `list`     | Sequence Type  | a collection of objects - mutable & ordered   | `['Ali', 'Xinyi', 'Miriam']`               |
# | tuple                 | `tuple`    | Sequence Type  | a collection of objects - immutable & ordered | `('Thursday', 6, 9, 2018)`                 |
# | dictionary            | `dict`     | Mapping Type   | mapping of key-value pairs                    | `{'name':'DSCI', 'code':511, 'credits':2}` |
# | none                  | `NoneType` | Null Object    | represents no value                           | `None`                                     |

# ### Numeric data types

# There are three distinct numeric types: `integers`, `floating point numbers`, and `complex numbers` (not covered here). We can determine the type of an object in Python using `type()`. We can print the value of the object using `print()`.

# In[1]:


x = 42


# In[2]:


type(x)


# In[3]:


print(x)


# In Jupyter/IPython (an interactive version of Python), the last line of a cell will automatically be printed to screen so we don't actually need to explicitly call `print()`.

# In[4]:


x  # Anything after the pound/hash symbol is a comment and will not be run


# In[5]:


pi = 3.14159
pi


# In[6]:


type(pi)


# ### Arithmetic Operators
# 
# Below is a table of the syntax for common arithmetic operations in Python:
# 
# | Operator |   Description    |
# | :------: | :--------------: |
# |   `+`    |     addition     |
# |   `-`    |   subtraction    |
# |   `*`    |  multiplication  |
# |   `/`    |     division     |
# |   `**`   |  exponentiation  |
# |   `//`   | integer division / floor division |
# |   `%`    |      modulo      |
# 
# Let's have a go at applying these operators to numeric types and observe the results.

# In[7]:


1 + 2 + 3 + 4 + 5  # add


# In[8]:


2 * 3.14159  # multiply


# In[9]:


2 ** 10  # exponent


# Division may produce a different `dtype` than expected, it will change `int` to `float`.

# In[10]:


int_2 = 2
type(int_2)


# In[11]:


int_2 / int_2  # divison


# In[12]:


type(int_2 / int_2)


# But the syntax `//` allows us to do "integer division" (aka "floor division") and retain the `int` data type, it always rounds down.

# In[13]:


101 / 2


# In[14]:


101 // 2  # "floor division" - always rounds down


# We refer to this as "integer division" or "floor division" because it's like calling `int` on the result of a division, which rounds down to the nearest integer, or "floors" the result.

# In[15]:


int(101 / 2)


# The `%` "modulo" operator gives us the remainder after division.

# In[16]:


100 % 2  # "100 mod 2", or the remainder when 100 is divided by 2


# In[17]:


101 % 2  # "101 mod 2", or the remainder when 101 is divided by 2


# In[18]:


100.5 % 2


# ### None
# 
# `NoneType` is its own type in Python. It only has one possible value, `None` - it represents an object with no value. We'll see it again in a later chapter.

# In[19]:


x = None


# In[20]:


print(x)


# In[21]:


type(x)


# ### Strings
# 
# Text is stored as a data type called a `string`. We can think of a string as a sequence of characters. 
# 
# ```{tip}
# Actually they are a sequence of Unicode code points. Here's a [great blog post](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/) on Unicode if you're interested.
# ```
# 
# We write strings as characters enclosed with either:
#   - single quotes, e.g., `'Hello'` 
#   - double quotes, e.g., `"Goodbye"`
# 
# There's no difference between the two methods, but there are cases where having both is useful (more on that below)! We also have triple double quotes, which are typically used for function documentation (more on that in a later chapter), e.g., `"""This function adds two numbers"""`.

# In[22]:


my_name = "Tomas Beuzen"


# In[23]:


my_name


# In[24]:


type(my_name)


# In[25]:


course = 'DSCI 511'


# In[26]:


course


# In[27]:


type(course)


# If the string contains a quotation or apostrophe, we can use a combination of single and double quotes to define the string.

# In[28]:


sentence = "It's a rainy day."


# In[29]:


sentence


# In[30]:


type(sentence)


# In[31]:


quote = 'Donald Knuth: "Premature optimization is the root of all evil."'


# In[32]:


quote


# ### Boolean
# 
# The Boolean (`bool`) type has two values: `True` and `False`.

# In[33]:


the_truth = True


# In[34]:


the_truth


# In[35]:


type(the_truth)


# In[36]:


lies = False


# In[37]:


lies


# In[38]:


type(lies)


# ### Comparison Operators
# 
# We can compare objects using comparison operators, and we'll get back a Boolean result:
# 
# | Operator  | Description                          |
# | :-------- | :----------------------------------- |
# | `x == y ` | is `x` equal to `y`?                 |
# | `x != y`  | is `x` not equal to `y`?             |
# | `x > y`   | is `x` greater than `y`?             |
# | `x >= y`  | is `x` greater than or equal to `y`? |
# | `x < y`   | is `x` less than `y`?                |
# | `x <= y`  | is `x` less than or equal to `y`?    |
# | `x is y`  | is `x` the same object as `y`?       |

# In[39]:


2 < 3


# In[40]:


"Deep learning" == "Solve all the world's problems"


# In[41]:


2 != "2"


# In[42]:


2 is 2


# In[43]:


2 == 2.0


# ### Boolean Operators
# 
# We also have so-called "boolean operators" which also evaluates to either `True` or `False`:
# 
# | Operator | Description |
# | :---: | :--- |
# |`x and y`| are `x` and `y` both True? |
# |`x or y` | is at least one of `x` and `y` True? |
# | `not x` | is `x` False? | 

# In[44]:


True and True


# In[45]:


True and False


# In[46]:


True or False


# In[47]:


False or False


# In[48]:


("Python 2" != "Python 3") and (2 <= 3)


# In[49]:


True


# In[50]:


not True


# In[51]:


not not True


# ```{note}
# Python also has [bitwise operators](https://wiki.python.org/moin/BitwiseOperators) like `&` and `|`. Bitwise operators literally compare the bits of two integers. That's beyond the scope of this course but I've included a code snippet below to show you them in action.
# ```

# In[52]:


print(f"Bit representation of the number 5: {5:0b}")
print(f"Bit representation of the number 4: {4:0b}")
print(f"                                    ↓↓↓")
print(f"                                    {5 & 4:0b}")
print(f"                                     ↓ ")
print(f"                                     {5 & 4}")


# ### Casting
# 
# Sometimes we need to explicitly **cast** a value from one type to another. We can do this using functions like `str()`, `int()`, and `float()`. Python tries to do the conversion, or throws an error if it can't.

# In[53]:


x = 5.0
type(x)


# In[54]:


x = int(5.0)
x


# In[55]:


type(x)


# In[56]:


x = str(5.0)
x


# In[57]:


type(x)


# In[58]:


str(5.0) == 5.0


# In[59]:


int(5.3)


# In[60]:


float("hello")


# ## 3. Lists and Tuples
# <hr>

# Lists and tuples allow us to store multiple things ("elements") in a single object. The elements are _ordered_ (we'll explore what that means a little later). We'll start with lists. Lists are defined with square brackets `[]`.

# In[61]:


my_list = [1, 2, "THREE", 4, 0.5]


# In[62]:


my_list


# In[63]:


type(my_list)


# Lists can hold any datatype - even other lists!

# In[64]:


another_list = [1, "two", [3, 4, "five"], True, None, {"key": "value"}]
another_list


# You can get the length of the list with the function `len()`:

# In[65]:


len(my_list)


# Tuples look similar to lists but have a key difference (they are immutable - but more on that a bit later). They are defined with parentheses `()`.

# In[66]:


today = (1, 2, "THREE", 4, 0.5)


# In[67]:


today


# In[68]:


type(today)


# In[69]:


len(today)


# ### Indexing and Slicing Sequences
# 
# We can access values inside a list, tuple, or string using square bracket syntax. Python uses *zero-based indexing*, which means the first element of the list is in position 0, not position 1.

# In[70]:


my_list


# In[71]:


my_list[0]


# In[72]:


my_list[2]


# In[73]:


len(my_list)


# In[74]:


my_list[5]


# We can use negative indices to count backwards from the end of the list.

# In[75]:


my_list


# In[76]:


my_list[-1]


# In[77]:


my_list[-2]


# We can use the colon `:` to access a sub-sequence. This is called "slicing".

# In[78]:


my_list[1:3]


# Note from the above that the start of the slice is inclusive and the end is exclusive. So `my_list[1:3]` fetches elements 1 and 2, but not 3.

# Strings behave the same as lists and tuples when it comes to indexing and slicing. Remember, we think of them as a *sequence* of characters.

# In[79]:


alphabet = "abcdefghijklmnopqrstuvwxyz"


# In[80]:


alphabet[0]


# In[81]:


alphabet[-1]


# In[82]:


alphabet[-3]


# In[83]:


alphabet[:5]


# In[84]:


alphabet[12:20]


# ### List Methods
# 
# A list is an object and it has methods for interacting with its data. A method is like a function, it performs some operation with the data, but a method differs to a function in that it is defined on the object itself and accessed using a period `.`. For example, `my_list.append(item)` appends an item to the end of the list called `my_list`. You can see the documentation for more [list methods](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists).

# In[85]:


primes = [2, 3, 5, 7, 11]
primes


# In[86]:


len(primes)


# In[87]:


primes.append(13)


# In[88]:


primes


# ### Sets
# 
# Another built-in Python data type is the `set`, which stores an _un-ordered_ list of _unique_ items. Being unordered, sets do not record element position or order of insertion and so do not support indexing.

# In[89]:


s = {2, 3, 5, 11}
s


# In[90]:


{1, 2, 3} == {3, 2, 1}


# In[91]:


[1, 2, 3] == [3, 2, 1]


# In[92]:


s.add(2)  # does nothing
s


# In[93]:


s[0]


# Above: throws an error because elements are not ordered and can't be indexing.

# ### Mutable vs. Immutable Types
# 
# Strings and tuples are immutable types which means they can't be modified. Lists are mutable and we can assign new values for its various entries. This is the main difference between lists and tuples.

# In[94]:


names_list = ["Indiana", "Fang", "Linsey"]
names_list


# In[95]:


names_list[0] = "Cool guy"
names_list


# In[96]:


names_tuple = ("Indiana", "Fang", "Linsey")
names_tuple


# In[97]:


names_tuple[0] = "Not cool guy"


# Same goes for strings. Once defined we cannot modifiy the characters of the string.

# In[98]:


my_name = "Tom"


# In[99]:


my_name[-1] = "q"


# In[100]:


x = ([1, 2, 3], 5)


# In[101]:


x[1] = 7


# In[102]:


x


# In[103]:


x[0][1] = 4


# In[104]:


x


# ## 4. String Methods
# <hr>

# There are various useful string methods in Python.

# In[105]:


all_caps = "HOW ARE YOU TODAY?"
all_caps


# In[106]:


new_str = all_caps.lower()
new_str


# Note that the method lower doesn't change the original string but rather returns a new one.

# In[107]:


all_caps


# There are *many* string methods. Check out the [documentation](https://docs.python.org/3/library/stdtypes.html#string-methods).

# In[108]:


all_caps.split()


# In[109]:


all_caps.count("O")


# One can explicitly cast a string to a list:

# In[110]:


caps_list = list(all_caps)
caps_list


# In[111]:


"".join(caps_list)


# In[112]:


"-".join(caps_list)


# We can also chain multiple methods together (more on this when we get to NumPy and Pandas in later chapters):

# In[113]:


"".join(caps_list).lower().split(" ")


# ### String formatting
# 
# Python has ways of creating strings by "filling in the blanks" and formatting them nicely. This is helpful for when you want to print statements that include variables or statements. There are a few ways of doing this but I use and recommend [f-strings](https://docs.python.org/3.6/whatsnew/3.6.html#whatsnew36-pep498) which were introduced in Python 3.6. All you need to do is put the letter "f" out the front of your string and then you can include variables with curly-bracket notation `{}`.

# In[114]:


name = "Newborn Baby"
age = 4 / 12
day = 10
month = 6
year = 2020
template_new = f"Hello, my name is {name}. I am {age:.2f} years old. I was born {day}/{month:02}/{year}."
template_new


# ```{note} Notes require **no** arguments,
# In the code above, the notation after the colon in my curly braces is for formatting. For example, `:.2f` means, print this variable with 2 decimal places. See format code options [here](https://docs.python.org/3.4/library/string.html#format-specification-mini-language).
# ```

# ## 5. Dictionaries
# <hr>

# A dictionary is a mapping between key-values pairs and is defined with curly-brackets:

# In[115]:


house = {
    "bedrooms": 3,
    "bathrooms": 2,
    "city": "Vancouver",
    "price": 2499999,
    "date_sold": (1, 3, 2015),
}

condo = {
    "bedrooms": 2,
    "bathrooms": 1,
    "city": "Burnaby",
    "price": 699999,
    "date_sold": (27, 8, 2011),
}


# We can access a specific field of a dictionary with square brackets:

# In[116]:


house["price"]


# In[117]:


condo["city"]


# We can also edit dictionaries (they are mutable):

# In[118]:


condo["price"] = 5  # price already in the dict
condo


# In[119]:


condo["flooring"] = "wood"


# In[120]:


condo


# We can also delete fields entirely (though I rarely use this):

# In[121]:


del condo["city"]


# In[122]:


condo


# And we can easily add fields:

# In[123]:


condo[5] = 443345


# In[124]:


condo


# Keys may be any immutable data type, even a `tuple`!

# In[125]:


condo[(1, 2, 3)] = 777
condo


# You'll get an error if you try to access a non-existent key:

# In[126]:


condo["not-here"]


# ## 6. Empties

# Sometimes you'll want to create empty objects that will be filled later on.

# In[127]:


lst = list()  # empty list
lst


# In[128]:


lst = []  # empty list
lst


# There's no real difference between the two methods above, `[]` is apparently [marginally faster](https://stackoverflow.com/questions/2972212/creating-an-empty-list-in-python)...

# In[129]:


tup = tuple()  # empty tuple
tup


# In[130]:


tup = ()  # empty tuple
tup


# In[131]:


dic = dict()  # empty dict
dic


# In[132]:


dic = {}  # empty dict
dic


# In[133]:


st = set()  # empty set
st


# ## 7. Conditionals
# <hr>

# [Conditional statements](https://docs.python.org/3/tutorial/controlflow.html) allow us to write programs where only certain blocks of code are executed depending on the state of the program. Let's look at some examples and take note of the keywords, syntax and indentation. 

# In[134]:


name = "Tom"

if name.lower() == "tom":
    print("That's my name too!")
elif name.lower() == "santa":
    print("That's a funny name.")
else:
    print(f"Hello {name}! That's a cool name!")
print("Nice to meet you!")


# The main points to notice:
# - Use keywords `if`, `elif` and `else`
# - The colon `:` ends each conditional expression
# - Indentation (by 4 empty space) defines code blocks
# - In an `if` statement, the first block whose conditional statement returns `True` is executed and the program exits the `if` block
# - `if` statements don't necessarily need `elif` or `else`
# - `elif` lets us check several conditions
# - `else` lets us evaluate a default block if all other conditions are `False`
# - the end of the entire `if` statement is where the indentation returns to the same level as the first `if` keyword

# If statements can also be **nested** inside of one another:

# In[135]:


name = "Super Tom"

if name.lower() == "tom":
    print("That's my name too!")
elif name.lower() == "santa":
    print("That's a funny name.")
else:
    print(f"Hello {name}! That's a cool name.")
    if name.lower().startswith("super"):
        print("Do you really have superpowers?")

print("Nice to meet you!")


# ### Inline if/else

# We can write simple `if` statements "inline", i.e., in a single line, for simplicity.

# In[136]:


words = ["the", "list", "of", "words"]

x = "long list" if len(words) > 10 else "short list"
x


# In[137]:


if len(words) > 10:
    x = "long list"
else:
    x = "short list"


# In[138]:


x


# ### Truth Value Testing

# Any object can be tested for "truth" in Python, for use in `if` and `while` (next chapter) statements.
# - `True` values: all objects return `True` unless they are a `bool` object with value `False` or have `len()` == 0
# - `False` values: `None`, `False`, `0`, empty sequences and collections: `''`, `()`, `[]`, `{}`, `set()`
# 
# ```{tip}
# Read more in the [docs here](https://docs.python.org/3/library/stdtypes.html#truth-value-testing).
# ```

# In[139]:


x = 1

if x:
    print("I'm truthy!")
else:
    print("I'm falsey!")


# In[140]:


x = False

if x:
    print("I'm truthy!")
else:
    print("I'm falsey!")


# In[141]:


x = []

if x:
    print("I'm truthy!")
else:
    print("I'm falsey!")


# ### Short-circuiting

# Python supports a concept known as "short-circuting". This is the automatic stopping of the execution of boolean operation if the truth value of expression has already been determined.

# In[142]:


fake_variable  # not defined


# In[143]:


True or fake_variable


# In[144]:


True and fake_variable


# In[145]:


False and fake_variable


# |Expression|Result|Detail|
# |---|---|---|
# |A or B|If A is `True` then A else B|B only executed if A is `False`|
# |A and B|If A is `False` then A else B|B only executed if A is `True`|
