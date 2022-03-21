  

0x00. Python - Hello, World
===========================

*   By Guillaume
*   Weight: 1
*   Project over - took place from 09-06-2021 to 09-07-2021 - you're done with 191% of tasks.
*   An auto review will be launched at the deadline

#### In a nutshell…

*   **Auto QA review:** 79.65/89 mandatory & 17.55/27 optional
*   **Altogether:**  **147.66%**
    *   Mandatory: 89.49%
    *   Optional: 65.0%
    *   Calculation:  89.49% + (89.49% \* 65.0%)  == **147.66%**

Concepts
--------

_For this project, students are expected to look at these concepts:_

*   [Python programming](/concepts/63)
*   [Python programming](/concepts/550)
*   [Python programming](/concepts/551)

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/231/48a9fdbd67c84a328a9df9ec8d93b9ac2458ac37721d7d53e51a27fb2bdc5263.jpg)

Author’s disclaimer
-------------------

    Welcome to the Python world!
    
    The first projects are more "C-oriented" - no tricks, no funky syntax - simple!
    If you've already played with Python, don't worry, fun things will come.
    You'll soon find that with Python (and the majority of higher level languages), there are ten different ways to do the same thing. Some tasks will expect only one implementation, while other tasks will have multiple possible implementations.
    Like C, Python also has a linter / style guide like Betty, called PEP8, also now known as PyCode. At Holberton, we won't start off with using PyCode, because it's much more strict compared to PEP8. Don't worry if you see a warning when you are running PEP8, you can ignore it.
    
    Enjoy!
    
    - Guillaume
    

Resources
---------

**Read or watch**:

*   [The Python tutorial](/rltoken/3mNweasE_b9U8vtCCFVB2g "The Python tutorial") (_only the first three chapters below_)
*   [Whetting Your Appetite](/rltoken/FRNro28k4Q_zlkpW_si2pw "Whetting Your Appetite")
*   [Using the Python Interpreter](/rltoken/M04rBQ5xGZtZ9yjaZsHxcA "Using the Python Interpreter")
*   [An Informal Introduction to Python](/rltoken/zVN1z9aa8L8jBhSp2AdbHw "An Informal Introduction to Python") (_Read up until “3.1.2. Strings” included_)
*   [How To Use String Formatters in Python 3](/rltoken/z6mk3Yep2tJVSF6KsBAYrg "How To Use String Formatters in Python 3")
*   [Learn to Program](/rltoken/gYgGXOth8N16KjUpXgO1uQ "Learn to Program")
*   [Pycodestyle – Style Guide for Python Code](/rltoken/fSEQ7fsRWu0uFg_wRR4KhQ "Pycodestyle -- Style Guide for Python Code")

Learning Objectives
-------------------

At the end of this project, you are expected to be able to [explain to anyone](/rltoken/xmqgbvTwSBDY_bN0pnDXeQ "explain to anyone"), **without the help of Google**:

### General

*   Why Python programming is awesome
*   Who created Python
*   Who is Guido van Rossum
*   Where does the name ‘Python’ come from
*   What is the Zen of Python
*   How to use the Python interpreter
*   How to print text and variables using `print`
*   How to use strings
*   What are indexing and slicing in Python
*   What is the official Python coding style and how to check your code with `pycodestyle`

Requirements
------------

### Python Scripts

*   Allowed editors: `vi`, `vim`, `emacs`
*   All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
*   All your files should end with a new line
*   The first line of all your files should be exactly `#!/usr/bin/python3`
*   A `README.md` file at the root of the repo, containing a description of the repository
*   A `README.md` file, at the root of the folder of _this_ project, is mandatory
*   Your code should use the pycodestyle (version 2.7.\*)
*   All your files must be executable
*   The length of your files will be tested using `wc`

### Shell Scripts

*   Allowed editors: `vi`, `vim`, `emacs`
*   All your scripts will be tested on Ubuntu 20.04 LTS
*   All your scripts should be exactly two lines long (`wc -l file` should print 2)
*   All your files should end with a new line
*   The first line of all your files should be exactly `#!/bin/bash`
*   All your files must be executable

### C Scripts

*   Allowed editors: `vi`, `vim`, `emacs`
*   All your files will be compiled on Ubuntu 20.04 LTS using gcc, using the options -Wall -Werror -Wextra -pedantic -std=gnu89
*   All your files should end with a new line
*   Your code should use the `Betty` style. It will be checked using [betty-style.pl](https://github.com/holbertonschool/Betty/blob/master/betty-style.pl "betty-style.pl") and [betty-doc.pl](https://github.com/holbertonschool/Betty/blob/master/betty-doc.pl "betty-doc.pl")
*   You are not allowed to use global variables
*   No more than 5 functions per file
*   In the following examples, the `main.c` files are shown as examples. You can use them to test your functions, but you don’t have to push them to your repo (if you do we won’t take them into account). We will use our own `main.c` files at compilation. Our `main.c` files might be different from the one shown in the examples
*   The prototypes of all your functions should be included in your header file called `lists.h`
*   Don’t forget to push your header file
*   All your header files should be include guarded

More Info
---------

### Zen

    The Zen of Python, by Tim Peters
    
    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!
    

### Pycodestyle

`Pycodestyle` is now the [new standard of Python style code](/rltoken/D67mmHg2X9ZI7QHlQxayyw "new standard of Python style code")

  
  
![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/231/Flyingcircus_2.jpg)

Quiz questions
--------------

**Great!** You've completed the quiz successfully! Keep going!

#### Question #0

Who created Python?

*   Julien Barbier
    
*   Yukihiro Matsumoto
    
*   Guido van Rossum
    

#### Question #1

What does this command line print?

    >>> print("Holberton school")
    

*   Holberton
    
*   “Holberton school”
    
*   Holberton school
    
*   ‘Holberton school’
    

#### Question #2

What does this command line print?

    >>> print("{:d} Battery street".format(98))
    

*   98 Battery street
    
*   “98 Battery street”
    
*   9 Battery street
    
*   8 Battery street
    

#### Question #3

What does this command line print?

    >>> print("{:d} Battery street, {}".format(98, "San Francisco"))
    

*   “98 Battery street, San Francisco”
    
*   8 Battery street, San
    
*   98 Battery street, San Francisco
    
*   San Francisco Battery street, 98
    

#### Question #4

What does this command line print?

    >>> a = "Python is cool"
    >>> print(a[4])
    

*   P
    
*   n
    
*   o
    
*   h
    

#### Question #5

What does this command line print?

    >>> a = "Python is cool"
    >>> print(a[0:6])
    

*   Python
    
*   Pytho
    
*   Python is
    
*   Python is cool
    

#### Question #6

What does this command line print?

    >>> a = "Python is cool"
    >>> print(a[:6])
    

*   Pytho
    
*   Python
    
*   Python is
    
*   is cool
    

#### Question #7

What does this command line print?

    >>> a = "Python is cool"
    >>> print(a[7:])
    

*   Python i
    
*   Python is
    
*   cool
    
*   is cool
    

#### Question #8

What does this command line print?

    >>> a = "Python is cool"
    >>> print(a[7:-5])
    

*   on
    
*   nohtyP
    
*   Python
    
*   si
    
*   is
    

#### Question #9

What does this command line print?

    >>> a = "Python is cool"
    >>> print(a[-2])
    

*   ol
    
*   l
    
*   o
    
*   Nothing
    

Tasks
-----

### 0\. Run Python file

mandatory

Score: 0% (Checks completed: 0%)

Write a Shell script that runs a Python script.

The Python file name will be saved in the environment variable `$PYFILE`

    guillaume@ubuntu:~/py/0x00$ cat main.py 
    #!/usr/bin/python3
    print("Best School")
    
    guillaume@ubuntu:~/py/0x00$ export PYFILE=main.py
    guillaume@ubuntu:~/py/0x00$ ./0-run
    Best School
    guillaume@ubuntu:~/py/0x00$ 
    

**Repo:**

*   GitHub repository: `holbertonschool-higher_level_programming`
*   Directory: `0x00-python-hello_world`
*   File: `0-run`

Done?! Help

×

#### Students who are done with "0. Run Python file"

Check your code

×

#### Correction of "0. Run Python file"

Start a new test Close

[![](/assets/checker_whm_pre_cora_coralina-68647f8f6e33159b68aac5d0bd52a6d4f832b7dc3675cbe2e4095ec206e48eea.png)](https://twitter.com/hashtag/HbtnWomensHistoryMonth)

[![](/assets/checker_whm_post_womens_history_month-618fe8a6d6d64b25389b52d869911e91d8800af725550de35d77bfb29bff2056.png)](https://twitter.com/hashtag/HbtnWomensHistoryMonth)

Requirement success

Requirement fail

Code success

Code fail

Efficiency success

Efficiency fail

Text answer success

Text answer fail

Skipped - Previous check failed

Get a sandbox QA Review

×

#### 0\. Run Python file

##### Commit used:

*   **User:** \---
*   **URL:** Click here
*   **ID:** `---`
*   **Author:** \---
*   **Subject:** _\---_
*   **Date:** \---

### 1\. Run inline

mandatory

Score: 0% (Checks completed: 0%)

Write a Shell script that runs Python code.

The Python code will be saved in the environment variable `$PYCODE`

    guillaume@ubuntu:~/py/0x00$ export PYCODE='print("Best School: {}".format(88+10))'
    guillaume@ubuntu:~/py/0x00$ ./1-run_inline 
    Best School: 98
    guillaume@ubuntu:~/py/0x00$ 
    

**Repo:**

*   GitHub repository: `holbertonschool-higher_level_programming`
*   Directory: `0x00-python-hello_world`
*   File: `1-run_inline`

Done?! Help

×

#### Students who are done with "1. Run inline"

Check your code

×

#### Correction of "1. Run inline"

Start a new test Close

[![](/assets/checker_whm_pre_cora_coralina-68647f8f6e33159b68aac5d0bd52a6d4f832b7dc3675cbe2e4095ec206e48eea.png)](https://twitter.com/hashtag/HbtnWomensHistoryMonth)

[![](/assets/checker_whm_post_womens_history_month-618fe8a6d6d64b25389b52d869911e91d8800af725550de35d77bfb29bff2056.png)](https://twitter.com/hashtag/HbtnWomensHistoryMonth)

Requirement success

Requirement fail

Code success

Code fail

Efficiency success

Efficiency fail

Text answer success

Text answer fail

Skipped - Previous check failed

Get a sandbox QA Review

×

#### 1\. Run inline

##### Commit used:

*   **User:** \---
*   **URL:** Click here
*   **ID:** `---`
*   **Author:** \---
*   **Subject:** _\---_
*   **Date:** \---

### 2\. Hello, print

mandatory

Score: 0% (Checks completed: 0%)

Write a Python script that prints exactly `"Programming is like building a multilingual puzzle`, followed by a new line.

*   Use the function `print`

    guillaume@ubuntu:~/py/0x00$ ./2-print.py 
    "Programming is like building a multilingual puzzle
    guillaume@ubuntu:~/py/0x00$
    

**Repo:**

*   GitHub repository: `holbertonschool-higher_level_programming`
*   Directory: `0x00-python-hello_world`
*   File: `2-print.py`

Done?! Help

×

#### Students who are done with "2. Hello, print"

Check your code

×

#### Correction of "2. Hello, print"

Start a new test Close

[![](/assets/checker_whm_pre_cora_coralina-68647f8f6e33159b68aac5d0bd52a6d4f832b7dc3675cbe2e4095ec206e48eea.png)](https://twitter.com/hashtag/HbtnWomensHistoryMonth)

[![](/assets/checker_whm_post_womens_history_month-618fe8a6d6d64b25389b52d869911e91d8800af725550de35d77bfb29bff2056.png)](https://twitter.com/hashtag/HbtnWomensHistoryMonth)

Requirement success

Requirement fail

Code success

Code fail

Efficiency success

Efficiency fail

Text answer success

Text answer fail

Skipped - Previous check failed

Get a sandbox QA Review

×

#### 2\. Hello, print

##### Commit used:

*   **User:** \---
*   **URL:** Click here
*   **ID:** `---`
*   **Author:** \---
*   **Subject:** _\---_
*   **Date:** \---

### 3\. Print integer

mandatory

Score: 0% (Checks completed: 0%)

Complete this [source code](https://github.com/holbertonschool/0x00.py/blob/master/3-print_number.py "source code") in order to print the integer stored in the variable `number`, followed by `Battery street`, followed by a new line.

*   You can find the source code [here](https://github.com/holbertonschool/0x00.py/blob/master/3-print_number.py "here")
*   The output of the script should be:
    *   the number, followed by `Battery street`,
    *   followed by a new line
*   You are not allowed to cast the variable `number` into a string
*   Your code must be 3 lines long
*   You have to use the new print numbers [tips](/rltoken/k33L_JH5NMcE3c4LsUkVlA "tips") (with `.format(...)`)

    guillaume@ubuntu:~/py/0x00$ ./3-print_number.py
    98 Battery street
    guillaume@ubuntu:~/py/0x00$ 
    

> C is strongly typed… not in Python! The variable `number` can be assigned to a string, a float, a bool etc… Forcing the type during a string format (`"...".format(...)`) is a way to control the type of a variable

**Repo:**

*   GitHub repository: `holbertonschool-higher_level_programming`
*   Directory: `0x00-python-hello_world`
*   File: `3-print_number.py`

Done?! Help

×

#### Students who are done with "3. Print integer"

Check your code

×

#### Correction of "3. Print integer"

Start a new test Close

[![](/assets/checker_whm_pre_cora_coralina-68647f8f6e33159b68aac5d0bd52a6d4f832b7dc3675cbe2e4095ec206e48eea.png)](https://twitter.com/hashtag/HbtnWomensHistoryMonth)

[![](/assets/checker_whm_post_womens_history_month-618fe8a6d6d64b25389b52d869911e91d8800af725550de35d77bfb29bff2056.png)](https://twitter.com/hashtag/HbtnWomensHistoryMonth)

Requirement success

Requirement fail

Code success

Code fail

Efficiency success

Efficiency fail

Text answer success

Text answer fail

Skipped - Previous check failed

Get a sandbox QA Review

×

#### 3\. Print integer

##### Commit used:

*   **User:** \---
*   **URL:** Click here
*   **ID:** `---`
*   **Author:** \---
*   **Subject:** _\---_
*   **Date:** \---

### 4\. Print float

mandatory

Score: 0% (Checks completed: 0%)

Complete the source code in order to print the float stored in the variable `number` with a precision of 2 digits.

*   You can find the source code [here](https://github.com/holbertonschool/0x00.py/blob/master/4-print_float.py "here")
*   The output of the program should be:
    *   `Float:`, followed by the float with only 2 digits
    *   followed by a new line
*   You are not allowed to cast `number` to string
*   You have to use the new print formatting [tips](/rltoken/CLkyFheLlanPlBS4ySOg7A "tips") (with `.format(...)`)

    guillaume@ubuntu:~/py/0x00$ ./4-print_float.py
    Float: 3.14
    guillaume@ubuntu:~/py/0x00$ 
    

**Repo:**

*   GitHub repository: `holbertonschool-higher_level_programming`
*   Directory: `0x00-python-hello_world`
*   File: `4-print_float.py`

Done?! Help

×

#### Students who are done with "4. Print float"

Check your code

×

#### Correction of "4. Print float"

Start a new test Close

[![](/assets/checker_whm_pre_cora_coralina-68647f8f6e33159b68aac5d0bd52a6d4f832b7dc3675cbe2e4095ec206e48eea.png)](https://twitter.com/hashtag/HbtnWomensHistoryMonth)

[![](/assets/checker_whm_post_womens_history_month-618fe8a6d6d64b25389b52d869911e91d8800af725550de35d77bfb29bff2056.png)](https://twitter.com/hashtag/HbtnWomensHistoryMonth)

Requirement success

Requirement fail

Code success

Code fail

Efficiency success

Efficiency fail

Text answer success

Text answer fail

Skipped - Previous check failed

Get a sandbox QA Review

×

#### 4\. Print float

##### Commit used:

*   **User:** \---
*   **URL:** Click here
*   **ID:** `---`
*   **Author:** \---
*   **Subject:** _\---_
*   **Date:** \---

### 5\. Print string

mandatory

Score: 0% (Checks completed: 0%)

Complete this [source code](https://github.com/holbertonschool/0x00.py/blob/master/5-print_string.py "source code") in order to print 3 times a string stored in the variable `str`, followed by its first 9 characters.

*   You can find the source code [here](https://github.com/holbertonschool/0x00.py/blob/master/5-print_string.py "here")
*   The output of the program should be:
    *   3 times the value of `str`
    *   followed by a new line
    *   followed by the 9 first characters of `str`
    *   followed by a new line
*   You are not allowed to use any loops or conditional statement
*   Your program should be maximum 5 lines long

    guillaume@ubuntu:~/py/0x00$ ./5-print_string.py 
    Holberton SchoolHolberton SchoolHolberton School
    Holberton
    guillaume@ubuntu:~/py/0x00$ 
    

**Repo:**

*   GitHub repository: `holbertonschool-higher_level_programming`
*   Directory: `0x00-python-hello_world`
*   File: `5-print_string.py`

Done?! Help

×

#### Students who are done with "5. Print string"

Check your code

×

#### Correction of "5. Print string"

Start a new test Close

[![](/assets/checker_whm_pre_cora_coralina-68647f8f6e33159b68aac5d0bd52a6d4f832b7dc3675cbe2e4095ec206e48eea.png)](https://twitter.com/hashtag/HbtnWomensHistoryMonth)

[![](/assets/checker_whm_post_womens_history_month-618fe8a6d6d64b25389b52d869911e91d8800af725550de35d77bfb29bff2056.png)](https://twitter.com/hashtag/HbtnWomensHistoryMonth)

Requirement success

Requirement fail

Code success

Code fail

Efficiency success

Efficiency fail

Text answer success

Text answer fail

Skipped - Previous check failed

Get a sandbox QA Review

×

#### 5\. Print string

##### Commit used:

*   **User:** \---
*   **URL:** Click here
*   **ID:** `---`
*   **Author:** \---
*   **Subject:** _\---_
*   **Date:** \---

### 6\. Play with strings

mandatory

Score: 0% (Checks completed: 0%)

Complete this [source code](https://github.com/holbertonschool/0x00.py/blob/master/6-concat.py "source code") to print `Welcome to Holberton School!`

*   You can find the source code [here](https://github.com/holbertonschool/0x00.py/blob/master/6-concat.py "here")
*   You are not allowed to use any loops or conditional statements.
*   You have to use the variables `str1` and `str2` in your new line of code
*   Your program should be exactly 5 lines long

    guillaume@ubuntu:~/py/0x00$ ./6-concat.py
    Welcome to Holberton School!
    guillaume@ubuntu:~/py/0x00$ wc -l 6-concat.py
    5 6-concat.py
    guillaume@ubuntu:~/py/0x00$ 
    

**Repo:**

*   GitHub repository: `holbertonschool-higher_level_programming`
*   Directory: `0x00-python-hello_world`
*   File: `6-concat.py`

Done?! Help

×

#### Students who are done with "6. Play with strings"

Check your code

×

#### Correction of "6. Play with strings"

Start a new test Close

[![](/assets/checker_whm_pre_cora_coralina-68647f8f6e33159b68aac5d0bd52a6d4f832b7dc3675cbe2e4095ec206e48eea.png)](https://twitter.com/hashtag/HbtnWomensHistoryMonth)

[![](/assets/checker_whm_post_womens_history_month-618fe8a6d6d64b25389b52d869911e91d8800af725550de35d77bfb29bff2056.png)](https://twitter.com/hashtag/HbtnWomensHistoryMonth)

Requirement success

Requirement fail

Code success

Code fail

Efficiency success

Efficiency fail

Text answer success

Text answer fail

Skipped - Previous check failed

Get a sandbox QA Review

×

#### 6\. Play with strings

##### Commit used:

*   **User:** \---
*   **URL:** Click here
*   **ID:** `---`
*   **Author:** \---
*   **Subject:** _\---_
*   **Date:** \---

### 7\. Copy - Cut - Paste

mandatory

Score: 0% (Checks completed: 0%)

Complete this [source code](https://github.com/holbertonschool/0x00.py/blob/master/7-edges.py "source code")

*   You can find the source code [here](https://github.com/holbertonschool/0x00.py/blob/master/7-edges.py "here")
*   You are not allowed to use any loops or conditional statements
*   Your program should be exactly 8 lines long
*   `word_first_3` should contain the first 3 letters of the variable `word`
*   `word_last_2` should contain the last 2 letters of the variable `word`
*   `middle_word` should contain the value of the variable `word` without the first and last letters

    guillaume@ubuntu:~/py/0x00$ ./7-edges.py
    First 3 letters: Hol
    Last 2 letters: on
    Middle word: olberto
    guillaume@ubuntu:~/py/0x00$ wc -l 7-edges.py
    8 7-edges.py
    guillaume@ubuntu:~/py/0x00$ 
    

**Repo:**

*   GitHub repository: `holbertonschool-higher_level_programming`
*   Directory: `0x00-python-hello_world`
*   File: `7-edges.py`

Done?! Help

×

#### Students who are done with "7. Copy - Cut - Paste"

Check your code

×

#### Correction of "7. Copy - Cut - Paste"

Start a new test Close

[![](/assets/checker_whm_pre_cora_coralina-68647f8f6e33159b68aac5d0bd52a6d4f832b7dc3675cbe2e4095ec206e48eea.png)](https://twitter.com/hashtag/HbtnWomensHistoryMonth)

[![](/assets/checker_whm_post_womens_history_month-618fe8a6d6d64b25389b52d869911e91d8800af725550de35d77bfb29bff2056.png)](https://twitter.com/hashtag/HbtnWomensHistoryMonth)

Requirement success

Requirement fail

Code success

Code fail

Efficiency success

Efficiency fail

Text answer success

Text answer fail

Skipped - Previous check failed

Get a sandbox QA Review

×

#### 7\. Copy - Cut - Paste

##### Commit used:

*   **User:** \---
*   **URL:** Click here
*   **ID:** `---`
*   **Author:** \---
*   **Subject:** _\---_
*   **Date:** \---

### 8\. Create a new sentence

mandatory

Score: 0% (Checks completed: 0%)

Complete this [source code](https://github.com/holbertonschool/0x00.py/blob/master/8-concat_edges.py "source code") to print `object-oriented programming with Python`, followed by a new line.

*   You can find the source code [here](https://github.com/holbertonschool/0x00.py/blob/master/8-concat_edges.py "here")
*   You are not allowed to use any loops or conditional statements
*   Your program should be exactly 5 lines long
*   You are not allowed to create new variables
*   You are not allowed to use string literals

    guillaume@ubuntu:~/py/0x00$ ./8-concat_edges.py
    object-oriented programming with Python
    guillaume@ubuntu:~/py/0x00$ wc -l 8-concat_edges.py
    5 8-concat_edges.py
    guillaume@ubuntu:~/py/0x00$ 
    

**Repo:**

*   GitHub repository: `holbertonschool-higher_level_programming`
*   Directory: `0x00-python-hello_world`
*   File: `8-concat_edges.py`

Done?! Help

×

#### Students who are done with "8. Create a new sentence"

Check your code

×

#### Correction of "8. Create a new sentence"

Start a new test Close

[![](/assets/checker_whm_pre_cora_coralina-68647f8f6e33159b68aac5d0bd52a6d4f832b7dc3675cbe2e4095ec206e48eea.png)](https://twitter.com/hashtag/HbtnWomensHistoryMonth)

[![](/assets/checker_whm_post_womens_history_month-618fe8a6d6d64b25389b52d869911e91d8800af725550de35d77bfb29bff2056.png)](https://twitter.com/hashtag/HbtnWomensHistoryMonth)

Requirement success

Requirement fail

Code success

Code fail

Efficiency success

Efficiency fail

Text answer success

Text answer fail

Skipped - Previous check failed

Get a sandbox QA Review

×

#### 8\. Create a new sentence

##### Commit used:

*   **User:** \---
*   **URL:** Click here
*   **ID:** `---`
*   **Author:** \---
*   **Subject:** _\---_
*   **Date:** \---

### 9\. Easter Egg

mandatory

Score: 0% (Checks completed: 0%)

Write a Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.

*   Your script should be maximum 98 characters long (please check with `wc -m 9-easter_egg.py`)

    guillaume@ubuntu:~/py/0x00$ ./9-easter_egg.py
    The Zen of Python, by Tim Peters
    
    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!
    guillaume@ubuntu:~/py/0x00$
    

**Repo:**

*   GitHub repository: `holbertonschool-higher_level_programming`
*   Directory: `0x00-python-hello_world`
*   File: `9-easter_egg.py`

Done?! Help

×

#### Students who are done with "9. Easter Egg"

Check your code

×

#### Correction of "9. Easter Egg"

Start a new test Close

[![](/assets/checker_whm_pre_cora_coralina-68647f8f6e33159b68aac5d0bd52a6d4f832b7dc3675cbe2e4095ec206e48eea.png)](https://twitter.com/hashtag/HbtnWomensHistoryMonth)

[![](/assets/checker_whm_post_womens_history_month-618fe8a6d6d64b25389b52d869911e91d8800af725550de35d77bfb29bff2056.png)](https://twitter.com/hashtag/HbtnWomensHistoryMonth)

Requirement success

Requirement fail

Code success

Code fail

Efficiency success

Efficiency fail

Text answer success

Text answer fail

Skipped - Previous check failed

Get a sandbox QA Review

×

#### 9\. Easter Egg

##### Commit used:

*   **User:** \---
*   **URL:** Click here
*   **ID:** `---`
*   **Author:** \---
*   **Subject:** _\---_
*   **Date:** \---

### 10\. Linked list cycle

mandatory

Score: 0% (Checks completed: 0%)

**Technical interview preparation**:

*   You are not allowed to google anything
*   Whiteboard first
*   This task and all future technical interview prep tasks will include checks for the efficiency of your solution, i.e. is your solution’s runtime fast enough, does your solution require extra memory usage / mallocs, etc.

Write a function in C that checks if a singly linked list has a cycle in it.

*   Prototype: `int check_cycle(listint_t *list);`
*   Return: `0` if there is no cycle, `1` if there is a cycle

Requirements:

*   Only these functions are allowed: `write`, `printf`, `putchar`, `puts`, `malloc`, `free`

    carrie@ubuntu:~/0x00$ cat lists.h
    #ifndef LISTS_H
    #define LISTS_H
    
    #include <stdlib.h>
    
    /**
     * struct listint_s - singly linked list
     * @n: integer
     * @next: points to the next node
     *
     * Description: singly linked list node structure
     * 
     */
    typedef struct listint_s
    {
        int n;
        struct listint_s *next;
    } listint_t;
    
    size_t print_listint(const listint_t *h);
    listint_t *add_nodeint(listint_t **head, const int n);
    void free_listint(listint_t *head);
    int check_cycle(listint_t *list);
    
    #endif /* LISTS_H */
    

    carrie@ubuntu:~/0x00$ cat 10-linked_lists.c
    #include <stdio.h>
    #include <stdlib.h>
    #include "lists.h"
    
    /**
     * print_listint - prints all elements of a listint_t list
     * @h: pointer to head of list
     * Return: number of nodes
     */
    size_t print_listint(const listint_t *h)
    {
        const listint_t *current;
        unsigned int n; /* number of nodes */
    
        current = h;
        n = 0;
        while (current != NULL)
        {
            printf("%i\n", current->n);
            current = current->next;
            n++;
        }
    
        return (n);
    }
    
    /**
     * add_nodeint - adds a new node at the beginning of a listint_t list
     * @head: pointer to a pointer of the start of the list
     * @n: integer to be included in node
     * Return: address of the new element or NULL if it fails
     */
    listint_t *add_nodeint(listint_t **head, const int n)
    {
        listint_t *new;
    
        new = malloc(sizeof(listint_t));
        if (new == NULL)
            return (NULL);
    
        new->n = n;
        new->next = *head;
        *head = new;
    
        return (new);
    }
    
    /**
     * free_listint - frees a listint_t list
     * @head: pointer to list to be freed
     * Return: void
     */
    void free_listint(listint_t *head)
    {
        listint_t *current;
    
        while (head != NULL)
        {
            current = head;
            head = head->next;
            free(current);
        }
    }
    

    carrie@ubuntu:~/0x00$ cat 10-main.c
    #include <stdlib.h>
    #include <string.h>
    #include <stdio.h>
    #include "lists.h"
    
    /**
     * main - check the code
     *
     * Return: Always 0.
     */
    int main(void)
    {
        listint_t *head;
        listint_t *current;
        listint_t *temp;
        int i;
    
        head = NULL;
        add_nodeint(&head, 0);
        add_nodeint(&head, 1);
        add_nodeint(&head, 2);
        add_nodeint(&head, 3);
        add_nodeint(&head, 4);
        add_nodeint(&head, 98);
        add_nodeint(&head, 402);
        add_nodeint(&head, 1024);
        print_listint(head);
    
        if (check_cycle(head) == 0)
            printf("Linked list has no cycle\n");
        else if (check_cycle(head) == 1)
            printf("Linked list has a cycle\n");
    
        current = head;
        for (i = 0; i < 4; i++)
            current = current->next;
        temp = current->next;
        current->next = head;
    
        if (check_cycle(head) == 0)
            printf("Linked list has no cycle\n");
        else if (check_cycle(head) == 1)
            printf("Linked list has a cycle\n");
    
        current = head;
        for (i = 0; i < 4; i++)
            current = current->next;
        current->next = temp;
    
        free_listint(head);
    
        return (0);
    }
    

    carrie@ubuntu:~/0x00$ gcc -Wall -Werror -Wextra -pedantic -std=gnu89 10-main.c 10-check_cycle.c 10-linked_lists.c -o cycle
    carrie@ubuntu:~/0x00$$ ./cycle 
    1024
    402
    98
    4
    3
    2
    1
    0
    Linked list has no cycle
    Linked list has a cycle
    carrie@ubuntu:~/0x00$
    

> Solving a problem is already a big win! but finding the best and optimal way to solve it, it’s way better! Think about the most optimal / fastest way to do it.

**Repo:**

*   GitHub repository: `holbertonschool-higher_level_programming`
*   Directory: `0x00-python-hello_world`
*   File: `10-check_cycle.c, lists.h`

Done?! Help

×

#### Students who are done with "10. Linked list cycle"

Check your code

×

#### Correction of "10. Linked list cycle"

Start a new test Close

[![](/assets/checker_whm_pre_cora_coralina-68647f8f6e33159b68aac5d0bd52a6d4f832b7dc3675cbe2e4095ec206e48eea.png)](https://twitter.com/hashtag/HbtnWomensHistoryMonth)

[![](/assets/checker_whm_post_womens_history_month-618fe8a6d6d64b25389b52d869911e91d8800af725550de35d77bfb29bff2056.png)](https://twitter.com/hashtag/HbtnWomensHistoryMonth)

Requirement success

Requirement fail

Code success

Code fail

Efficiency success

Efficiency fail

Text answer success

Text answer fail

Skipped - Previous check failed

Ask for a new correction : in progress...: an error occured Get a sandbox QA Review

×

#### 10\. Linked list cycle

##### Commit used:

*   **User:** \---
*   **URL:** Click here
*   **ID:** `---`
*   **Author:** \---
*   **Subject:** _\---_
*   **Date:** \---

### 11\. Hello, write

#advanced

Score: 0% (Checks completed: 0%)

Write a Python script that prints exactly `and that piece of art is useful - Dora Korpar, 2015-10-19`, followed by a new line.

*   Use the function `write` from the `sys` module
*   You are not allowed to use `print`
*   Your script should print to `stderr`
*   Your script should exit with the status code `1`

    guillaume@ubuntu:~/py/0x00$ ./100-write.py
    and that piece of art is useful - Dora Korpar, 2015-10-19
    guillaume@ubuntu:~/py/0x00$ echo $?
    1
    guillaume@ubuntu:~/py/0x00$ ./100-write.py 2> q
    guillaume@ubuntu:~/py/0x00$ cat q
    and that piece of art is useful - Dora Korpar, 2015-10-19
    guillaume@ubuntu:~/py/0x00$ 
    

**Repo:**

*   GitHub repository: `holbertonschool-higher_level_programming`
*   Directory: `0x00-python-hello_world`
*   File: `100-write.py`

Done?! Help

×

#### Students who are done with "11. Hello, write"

Check your code

×

#### Correction of "11. Hello, write"

Start a new test Close

[![](/assets/checker_whm_pre_cora_coralina-68647f8f6e33159b68aac5d0bd52a6d4f832b7dc3675cbe2e4095ec206e48eea.png)](https://twitter.com/hashtag/HbtnWomensHistoryMonth)

[![](/assets/checker_whm_post_womens_history_month-618fe8a6d6d64b25389b52d869911e91d8800af725550de35d77bfb29bff2056.png)](https://twitter.com/hashtag/HbtnWomensHistoryMonth)

Requirement success

Requirement fail

Code success

Code fail

Efficiency success

Efficiency fail

Text answer success

Text answer fail

Skipped - Previous check failed

Get a sandbox QA Review

×

#### 11\. Hello, write

##### Commit used:

*   **User:** \---
*   **URL:** Click here
*   **ID:** `---`
*   **Author:** \---
*   **Subject:** _\---_
*   **Date:** \---

### 12\. Compile

#advanced

Score: 0% (Checks completed: 0%)

Write a script that compiles a Python script file.

The Python file name will be stored in the environment variable `$PYFILE`

The output filename has to be `$PYFILEc` (ex: `export PYFILE=my_main.py` => output filename: `my_main.pyc`)

    guillaume@ubuntu:~/py/0x00$ cat main.py 
    #!/usr/bin/python3
    print("Best School")
    
    guillaume@ubuntu:~/py/0x00$ export PYFILE=main.py
    guillaume@ubuntu:~/py/0x00$ ./101-compile
    Compiling main.py ...
    guillaume@ubuntu:~/py/0x00$ ls
    101-compile  main.py  main.pyc
    guillaume@ubuntu:~/py/0x00$ cat main.pyc | zgrep -c "Best School"
    1
    guillaume@ubuntu:~/py/0x00$ od -t x1 main.pyc # SYSTEM DEPENDANT => CAN BE DIFFERENT
    0000000 ee 0c 0d 0a 91 26 3e 58 31 00 00 00 e3 00 00 00
    0000020 00 00 00 00 00 00 00 00 00 02 00 00 00 40 00 00
    0000040 00 73 0e 00 00 00 65 00 00 64 00 00 83 01 00 01
    0000060 64 01 00 53 29 02 7a 10 48 6f 6c 62 65 72 74 6f
    0000100 6e 20 53 63 68 6f 6f 6c 4e 29 01 da 05 70 72 69
    0000120 6e 74 a9 00 72 02 00 00 00 72 02 00 00 00 fa 07
    0000140 6d 61 69 6e 2e 70 79 da 08 3c 6d 6f 64 75 6c 65
    0000160 3e 02 00 00 00 73 00 00 00 00
    0000172
    guillaume@ubuntu:~/py/0x00$ 
    

**Repo:**

*   GitHub repository: `holbertonschool-higher_level_programming`
*   Directory: `0x00-python-hello_world`
*   File: `101-compile`

Done?! Help

×

#### Students who are done with "12. Compile"

Check your code

×

#### Correction of "12. Compile"

Start a new test Close

[![](/assets/checker_whm_pre_cora_coralina-68647f8f6e33159b68aac5d0bd52a6d4f832b7dc3675cbe2e4095ec206e48eea.png)](https://twitter.com/hashtag/HbtnWomensHistoryMonth)

[![](/assets/checker_whm_post_womens_history_month-618fe8a6d6d64b25389b52d869911e91d8800af725550de35d77bfb29bff2056.png)](https://twitter.com/hashtag/HbtnWomensHistoryMonth)

Requirement success

Requirement fail

Code success

Code fail

Efficiency success

Efficiency fail

Text answer success

Text answer fail

Skipped - Previous check failed

Get a sandbox QA Review

×

#### 12\. Compile

##### Commit used:

*   **User:** \---
*   **URL:** Click here
*   **ID:** `---`
*   **Author:** \---
*   **Subject:** _\---_
*   **Date:** \---

### 13\. ByteCode -> Python #1

#advanced

Score: 0% (Checks completed: 0%)

Write the Python function `def magic_calculation(a, b):` that does exactly the same as the following Python bytecode:

      3           0 LOAD_CONST               1 (98)
                  3 LOAD_FAST                0 (a)
                  6 LOAD_FAST                1 (b)
                  9 BINARY_POWER
                 10 BINARY_ADD
                 11 RETURN_VALUE
    

*   Tip: [Python bytecode](/rltoken/FYK4MePotTrqXCfiKYxL7Q "Python bytecode")

**Repo:**

*   GitHub repository: `holbertonschool-higher_level_programming`
*   Directory: `0x00-python-hello_world`
*   File: `102-magic_calculation.py`

Done?! Help

×

#### Students who are done with "13. ByteCode -> Python #1"

Check your code

×

#### Correction of "13. ByteCode -> Python #1"

Start a new test Close

[![](/assets/checker_whm_pre_cora_coralina-68647f8f6e33159b68aac5d0bd52a6d4f832b7dc3675cbe2e4095ec206e48eea.png)](https://twitter.com/hashtag/HbtnWomensHistoryMonth)

[![](/assets/checker_whm_post_womens_history_month-618fe8a6d6d64b25389b52d869911e91d8800af725550de35d77bfb29bff2056.png)](https://twitter.com/hashtag/HbtnWomensHistoryMonth)

Requirement success

Requirement fail

Code success

Code fail

Efficiency success

Efficiency fail

Text answer success

Text answer fail

Skipped - Previous check failed

Get a sandbox QA Review

×

#### 13\. ByteCode -> Python #1

##### Commit used:

*   **User:** \---
*   **URL:** Click here
*   **ID:** `---`
*   **Author:** \---
*   **Subject:** _\---_
*   **Date:** \---

×

#### Recommended Sandbox

Copyright © 2022 Holberton Inc, All rights reserved.

×

#### Markdown Guide

#### Emphasis

\*\***bold**\*\*
\*_italics_\*
~~strikethrough~~

#### Headers

\# Big header
## Medium header
### Small header
#### Tiny header

#### Lists

\* Generic list item
\* Generic list item
\* Generic list item

1. Numbered list item
2. Numbered list item
3. Numbered list item

#### Links

\[Text to display\](http://www.example.com)

#### Quotes

\> This is a quote.
> It can span multiple lines!

#### Images

CSS style available: `width, height, opacity`

!\[\](http://www.example.com/image.jpg)
!\[\](http://www.example.com/image.jpg | width: 200px)
!\[\](http://www.example.com/image.jpg | height: 124px | width: 80px | opacity: 0.6)

#### Tables

| Column 1 | Column 2 | Column 3 |
| -------- | -------- | -------- |
| John     | Doe      | Male     |
| Mary     | Smith    | Female   |

_Or without aligning the columns..._

| Column 1 | Column 2 | Column 3 |
| -------- | -------- | -------- |
| John | Doe | Male |
| Mary | Smith | Female |

#### Displaying code

\`var example = "hello!";\`

_Or spanning multiple lines..._

\`\`\`
var example = "hello!";
alert(example);
\`\`\`

(function(i,s,o,g,r,a,m){i\['GoogleAnalyticsObject'\]=r;i\[r\]=i\[r\]||function(){ (i\[r\].q=i\[r\].q||\[\]).push(arguments)},i\[r\].l=1\*new Date();a=s.createElement(o), m=s.getElementsByTagName(o)\[0\];a.async=1;a.src=g;m.parentNode.insertBefore(a,m) })(window,document,'script','//www.google-analytics.com/analytics.js','ga'); ga('create', 'UA-67152800-6', 'auto', { userId: '3400' } ); ga('send', 'pageview'); $(document).ready(function() { ga(function(tracker) { var clientId = tracker.get('clientId'); $('.ga-client-id').val(clientId); }); });
