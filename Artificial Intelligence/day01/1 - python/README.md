# Module 1: Python 📓

Welcome and thank you for participating in the Artificial Intelligence Pool by PoC Innovation ! Our team has worked hard to create a great learning resource and introduction to the incredible world of Artificial Intelligence and what better way to start than the most popular programming language for Machine Learning - **Python** !

During this week, you will use Python to tackle Machine Learning subjects of increasing difficulty, so never hesitate to ask the PoC staff for help, they'll be happy to answer your questions and don't worry about not completing each Pool Day: **the subjects are difficult to finish by design** !

Ultimately, the goal is for you to achieve a good knowledge of the field of AI after this week. So make sure you take your time to truly grasp the concepts you will see throughout this course. **Learning AI is not something you can rush; so make sure you understand the theory behind what you do during this Pool**.

Now, buckle up: **your adventure begins now** !


## Python3 🐍

Python is a high-level interpreted language, which has become very popular in the academic and scientific community for its simplicity and its layer of abstraction of several rules of computer science, such as the fact that you don't need to type your variables. Python is also able to interpret different programming paradigms like imperative, object-oriented...

So you may ask yourself: Why do we use Python which is slower than C/C++ for AI, a domain that requires a lot of resources?
Well, quite simply, libraries like TensorFlow work with a Python interface on the surface but use the C++ language behind.

### Example

> "Hello World" Function

```py
def myFunc(name="Undefined"):
""" A function is defined using the keyword `def` followed by a space
and the name of the function, between brackets we put the different parameters
for the example we have the parameter `name` which by default is equal to Undefined.
This comment is called a docstring: it provides a way for developers to explain the usage of a function / class / etc. so that other developers can understand how to use them. For a function, you'll generally find the required arguments as well as the returned values and maybe some usage examples.

Args:
    name: name of the user

Returns:
    None
"""
    print("Hello " + name)

# myFunc() will display "Hello Undefined"
# myFunc("PoC") will display "Hello PoC"

```

## Python Command Line

Before we get started with **iPython notebooks**, which you will be using for most of the week, we'd like to show you a cool party trick that you can do using any terminal with Python installed !

Open up a new terminal window: inside, simply run the `python` command !

```bash
> python
```

This command will open up the python command line:

```bash
> python
Python 3.X.XX (main, XXX XX XXXX, XX:XX:XX)
[GCC 7.5.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

The output **will** differ based on your Python version and other variables but it **should** open a command line where you can execute any python code !

That's right: you can even build an entire neural network inside this command line (although we **will** be very scared if you choose to do so)

Of course, you will not be writing your code inside this command line very often, because most of the time, you wish to save your code inside a `.py` or `.ipynb` file 😄.

However, this command line can help you troubleshoot your code in a smaller scope.

You can try using the `print()` method to print some stuff on your terminal.

```bash
Type "help", "copyright", "credits" or "license" for more information.
>>> print("Hello world")
Hello world
>>>
```

Pretty cool, right ? What if you instead want to know what the result of 2 + 2 is ?

```bash
Type "help", "copyright", "credits" or "license" for more information.
>>> print(2 + 2)
4
>>> a = 2 + 2
>>> print(a)
4
>>> 2 + 2
4
>>>
```

Interesting... these three inputs have the same output, "4".

One of them uses the `print()` method, the other stores 2 + 2 inside a and then prints it and the last one only calculates 2 + 2 but still, the output is 4 despite the fact that we didn't even ask Python to display the result !

Try to open your own Python command line and run your own experiments to see what's happening.

In python, the result of each line of code is displayed in the console. This behaviour is particularly useful for visualisation inside Jupyter Notebooks, which we will talk about just after this small explanation of data types:

## Python Data Types

But the last result being displayed might not be the only thing that surprised you with how python works.

Many of you might be familiar with the C language and its `printf()` function. In C, in order to print the result of 2 + 2, you would need to do the following:

```c
printf("%i\n", 2 + 2);
```

In python, it's enough to just do:

```py
print(2 + 2)
```

Why is that ? Well, python is both a strongly and dynamically typed language:

| Typing   | Static    | Dynamic   |
| -------- | --------- | --------- |
| Variable | typed     | not typed |
| Value    | not typed | typed     |

| Typing         | Strong | Weak | Strong & Dynamic |
| -------------- | ------ | ---- | ---------------- |
| "I am " + 13   | ❌      | ✅    | ✅                |
| "I am " + "13" | ✅      | ✅    | ✅                |

Static typing (for example C) means that variables have a type which must be known by the interpretor from the moment the variable is declared.\
Dynamic (for example JavaScript) typing means that values / objects have types which can be changed at any given time.

Strong typing (C) means that you can not perform operations between different types of variables.\
Weak typing (JavaScript) means that you can perform any operation between any types of variables.

A strongly and dynamically typed language (Python) allows the developer to benefit from dynamic typing but still has the safety provided by strong typing.

You can open a Python command line and use the `type()` method to check out the different data types for each value:

```bash
>>> type(1)
<class 'int'>
>>> type("hello world")
<class 'str'>
>>>
```

Before heading over to the `.ipynb` notebook, please fill in and submit a file called `data_types.txt` which contains the corresponding built-in types for the following values in order:

- 1
- "hello world"
- 1.0
- ["apples", "oranges", "bananas"]
- {"answer": 42}
- 2 + 2 == 4
- None

Simply write the output of `type()` for each of the above values in order, one by line.

```bash
❯ cat data_types.txt -e
<class 'int'>$
<class 'str'>$
```

## Submit 🏆

- Fill the `data_types.txt` file with the required data types.

- Fill the ``Python.ipynb`` notebook.

To submit your work, think about pushing your changes. It is important to push so that we are able to assess participation.
If you have any concerns, talk to a supervisor.

## Resources 📖

 - [Python3 Documentation](https://docs.python.org/3/)
 - [Why Python3 more than C++ ?](https://fr.quora.com/Pourquoi-Python-est-tr%C3%A8s-utilis%C3%A9-en-IA-Big-Data-alors-quil-nest-pas-le-plus-performant-en-rapidit%C3%A9-de-calcul)
 - [Python3 courses](https://courspython.com/introduction-python.html)
 - [Python3 Machine Learnia](https://www.youtube.com/watch?v=82KLS2C_gNQ)
