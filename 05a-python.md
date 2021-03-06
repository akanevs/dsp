# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Python lists and tuples are both sequences of values, which can be of any type, and are indexed by integers. The main difference is that tuples are immutable and cannot be changed. Tuples will work as keys in dictionaries because they are immutable.

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Python lists are ordered collections/sequences of values, whereas sets are unordered collections of values. Since sets are unordered, they do not record element position and do not support indexing, slicing, etc... Sets are useful for quickly finding if an element is an the set (membership testing) and for eliminating duplicate entries. For lists, such searches are less efficient.

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Lambda functions are used to enable functional programming, and give the ability to pass functions to other functions, which can be much more convenient. For example, one may pass a function as an argument using lambdas.

Example:

temp = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]

sorted(temp)

[(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]

sorted(temp, key=lambda pair: pair[1])

[(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions allow for creation of lists using a compact format by specifying an expression that is applied to each member of some sequence/iterable. A list comprehension consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses. 

For example, to create a list of squares:

squares = [x**2 for x in range(10)]

print(squares)

[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

We can also do this using a map:

list(map((lambda x: x **2), dat))

[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

Now, we do this using a filter:

datsquared = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

list( filter((lambda x: sqrt(x)<10 ), datsquared))

[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937 days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513 days


c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850 days

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Write a script as indicated (using the football data) in [q8_parsing.py](python/q8_parsing.py)





