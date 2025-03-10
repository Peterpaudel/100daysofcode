# 100Daysofcode
### Welcome to my journey of 100 days of coding . I will be documenting my journey from zero to advance in python
![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/e7ee7319e636cdee1503cfe6611303c2a91d5b28/images/100daysofcode.png)
| Projects Completed|
| -------- |
|1.[**Rock,paper and scissors**](https://github.com/Utshav-paudel/python-project/blob/52492569a6fd370715038381271212741a8f8256/day4.6%20rock%20paper%20scissore.py)|
|2.[**Kaun bangega crorepati**](https://github.com/Utshav-paudel/python-project/blob/f245d82d6a740061001ef4e8759fc683a4879e18/KBC.py) |
|3.[**Coffee machine**](https://github.com/Utshav-paudel/100Daysofcode/blob/ca68172d64863eb80a029d209471cde284b7fb24/code/day25/main.py)|
|4.[**Betting on turtle race game**](https://github.com/Utshav-paudel/100Daysofcode/blob/ffa55b2723c0efa577db88d91162810966088a0e/code/day31/tutlerace.py)|
|5.[**Snake game**](https://github.com/Utshav-paudel/100Daysofcode/tree/Utshav-paudel/code/day35)|
|6.[**Mile to km app**](https://github.com/Utshav-paudel/100Daysofcode/blob/20324106cb5b59bb1e05a0b9f63fd7e5054b4a50/code/day41/main.py)|
|7.[**Pomodoro app**](https://github.com/Utshav-paudel/100Daysofcode/tree/20324106cb5b59bb1e05a0b9f63fd7e5054b4a50/code/day42)|
|8.[**Password manager app**](https://github.com/Utshav-paudel/100Daysofcode/tree/dbba964e915e0f32bd3585298c936859a8add30c/code/day43)|
|9.[**Flash card app**](https://github.com/Utshav-paudel/100Daysofcode/tree/79bb2667f4412f3d7c6e6a479202e08ed73da6b0/code/day45)|
|10.[**Kanye West Quote generator app**](https://github.com/Utshav-paudel/100Daysofcode/tree/77b5e9617d3ed22c680d3afb3f6cfe4d1d23eaef/code/day46/kanye%20west%20quote%20app)|
|11.[**Iss satellite checker**](https://github.com/Utshav-paudel/100Daysofcode/tree/77b5e9617d3ed22c680d3afb3f6cfe4d1d23eaef/code/day46/iss%20overhead)|
### Core python 
|**Core python**|
|---------------|
|1.Language Fundamentals|
|2.Operators|
|3.Input and Output statements|
|4.Flow Control|
|5.Strings|
|6.List Data Structure|
|7.Tuple Data Structure|
|8.Set Data Structure|
|9.Dictonary Data Structure|
|10.Functions|
|11.Modules|
|12.Packages|


# Day 1
<p>Today I learned some basics in python like data types in python and about typecasting in python.
There are two types of typecasting in python </P>
1.Implicit typecasting:
conversion data types by program itself for e.g: 
  
```
  a=10
     b=2.0
     sum=a+b
     print(sum)
     #sum will be in float because of implicit typecasting
   
 ```
 
2. Explicit typecasting:
conversion of data types by programmer is called explicit typecasting .
  for e.g :
  <break>
  
 ```
  a=10
     b=2
     sum=a+b
     print(float(sum))
     #sum is in integer and changed to float using explicit typecasting
 
  ```

# Day 1 project Calculator :
![alt text](https://github.com/Peterpaudel/100Daysofcode/blob/c3f966a86f9b31b7ab15ca3c510dfb08c7e142f8/images/day1.png)

# Day 2 
  
<p>Here is day2 codes I have learned about string slicing . String in python is similar to array .
  </p>

```
  
 name="Elephant"
 length=len(name) #this len function provides the length of name
 print(name[2:3]) #this print e
 print(name[1:5]) #this print leph
 #this above example is string slicing
  ```
  
# Greeting program
  <p>This program greet you according to your time .
    It import time from your computer using 
    
import time
    
### Then it convert time into string using
 
strftime()
    
    
After that greeting is done using elif codition as seen below :
![alt text](https://github.com/Peterpaudel/100Daysofcode/blob/93fbbe9995de8412ee7ee40ad2198a4bae846e40/images/day2.png)
    
# Day3
    
### Match case statement 
    
 Match case is similar to switch case in c and c++ but there is no necesary of using break
    If you donot know about c and c++
    Match case is used to select case according to option here is a sample program:
![alt text](https://github.com/Peterpaudel/100Daysofcode/blob/5c6c149cad4c4ad67ca330a028c828d6187dce79/images/day3.png)
    
# Day4
### List
   
It is a sequence data types in python that is a collection of sequence of  elements.
for e.g:
    
`lst=[1,2,56,"hari","alex",false]`
    
 Yes as you can see list can contains different data types.
    
 Tuples is also similar to list but it cannot be changed (i.e immutable)
 Clear explanation of list is shown below
 ![alt text](https://github.com/Peterpaudel/100Daysofcode/blob/59128304cd86677286b6edf1c348fc0c3353813f/images/day4.png)

 ### List method
  There are various method to perform with list that help in program some of them are:
  
  #### list.sort()
    
It sort the list in ascending order
    
![alt text](https://github.com/Peterpaudel/100Daysofcode/blob/245832c2f68774d3a609da722b8b3992e3782a63/images/day4.1.png)
    
#### list.index()
     
It gives index of first occurence of the list item
    
![alt text](https://github.com/Peterpaudel/100Daysofcode/blob/c47288693ca44e444e6a927b8bb489792378db55/images/day4.2.png)
    
here output will be 1 for colours list and 3 for num list .
    
#### list.count
    
It counts number the number of items of given value 
for e.g `colors.count("green")`
This will count number of time green occured in list colors 
    
All others important list method are as follows :

  ![alt text](https://github.com/Peterpaudel/100Daysofcode/blob/e2ec5aea55ef65ef785927616f4c51ebaf665b98/images/day4.3.png)
    
  ![alt text](https://github.com/Peterpaudel/100Daysofcode/blob/e2ec5aea55ef65ef785927616f4c51ebaf665b98/images/day4.4.png)
    
# Day5
   
Today we are going to learn about the tuples in python . Tuples are similar to list but it is immutable(i.e it cannot be changed).
It also hold collection of data items . Tuples items are separated with comma and enclosed with small brackets for e.g:

    tuple=(1,4,6,7)
    tuple=(1)
    print(type(tuple))  #this is printed as class int it should contain one , to be tuple
    tuple=(1,)           
    print(type(tuple))  #this is printed as class tuple
    
##### Note : Tuples cannot be changed it is constant and use in cases where we want constant list .
![alt enter](https://github.com/Peterpaudel/100Daysofcode/blob/4584edefb0d8a4ca56495ed1b7d8b17480db45b3/images/day5.png)

# Day6
Today I learned about the method on tuples . Tuples exactly is immutable so it does not have any method that changes data item but we can perform this by changing tuples into list changing data items and changing it to tuples . Although we can perform some operation like index,len,etc .
Code for the method in tuples is shared below hope you get some insights .

![alt text](https://github.com/Peterpaudel/100Daysofcode/blob/80dff58495fd5b62d44aa44661f10ce792b65148/images/day6.png)
    
# Day7
### f-string
 f-string is a new string formatting mechanism that allow us to enter variable directly in between the string according to our format.
 for e.g:
 
    val="geek"
    print(f"{val} for {val} is a portal for {val}")
    
![alt text](https://github.com/Peterpaudel/100Daysofcode/blob/cb31e2c50667345c4ed21c81453d9659086e7548/images/day7.png)
    
### Docstrings
Python docstrings are the string literals that appears right after the definition of function,class,method or module.
Its like comment but its not ignored by python interpreter and cannot be used anywhere it mostly used to describe function workflow

![alt text](https://github.com/Peterpaudel/100Daysofcode/blob/bef684dc84d366f49f1c137c537b9c9bec0f87ca/images/day7.png)
    
### PEP 8
PEP 8 is a guidline in python programming that makes python readable,maintainable and consistent . It stands for Python Enhancement Proposals
    
### Set
Set is an unordered collection of data items in a single variable enclosed by curly braces and element separated by comma . Set doesnot contain duplicate item 
    
![alt text](https://github.com/Peterpaudel/100Daysofcode/blob/dc5121c0f0733c8c27e2a5e4082100236f090538/images/day7.2.png)
    
# Day8
### Recursion
Recursion is the special case in which function call itself directly or indirectly to meet desired result.
such function is called recursive function 

![alt text](https://github.com/Peterpaudel/100Daysofcode/blob/f93fd737e715a8762c40d780a707fc772fc9423d/images/day8.png)
    
# Day9
### Methods on sets
#### 1.union() and update()
  union() helps to find the union of two sets and update helps to update the sets value.
    
    s1={1,4,5,7,9}
    s2={1,4,6,7,8,9}
    print(s1.union(s2))
    s1.update(s2)
    print(s1)
![alt text](https://github.com/Peterpaudel/100Daysofcode/blob/94caa59a9b69ec41fc31f6b36c5f3784140367b8/images/day9(union%20and%20update).png)
#### 2.intersection() and intersection_update()
  intersection() finds common value of two sets wherease intersection_update() update the sets with intersection.
![alt text](https://github.com/Peterpaudel/100Daysofcode/blob/94caa59a9b69ec41fc31f6b36c5f3784140367b8/images/day9(difference%20and%20difference_update).png)
#### 3.symmetric_difference() and symmetric_difference_update()
  symmetric_difference() gets items that are not similar on two sets and symmetric_difference_update() the sets with different items of two sets
![alt text](https://github.com/Peterpaudel/100Daysofcode/blob/ed75cd2e3c6dfbeb06e97f91bcae6081b16462ed/images/day9(symmetric%20difference).png)  
### 4. difference() and difference_update()
difference() gets items that are not similar from original sets and difference_update() update the sets with difference items from original sets.
![alt text](https://github.com/Peterpaudel/100Daysofcode/blob/ed75cd2e3c6dfbeb06e97f91bcae6081b16462ed/images/day9(difference).png)
  
# Day10
### Other sets methods
Some of other sets methods that we can use are:
![alt text](https://github.com/Peterpaudel/100Daysofcode/blob/ee1483cb0912d16477f904b686c16efa6aa44304/images/day10.png)
    
# Day11
### Dictionaries in python
Dictionaries are ordered collection of data items. They store multiple items in a single variable.Dictionaries items are key-value pairs that are separated by commas and enclosed with curly brackets.Dictionaries doesnot allow duplicate items.
    
    dict={"name":"ram",
    "age":"21"}
    print=(dict)
    
![alt text](https://github.com/Peterpaudel/100Daysofcode/blob/05603fe735eb03a71ef43ab42451e6a734385372/images/day11.png)
# Day12
### Dictionaries methods in python
There are lots of methods in dictionaries some of them are listed below:

#### 1. update()
The update() methods update the values of the key provided else creates a new key:value pairs if the key used in update doesn't exists in that dictionaries.
<br>
<b>Example:</b>

    dict1={234:12,235:89,238:23}
    dict2={234:17,239:45}
    dict1.update(dict2)
    
Here,Since value of key 234 already exists i.e 12 gets overwrite as 17 dueto update methods
whereas new key value pair is updated on dict1 i.e 239:45.
sample program for update method is given below:<br>
    
![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/e46d1007b83309e71906f7a6261010287e58e5a2/images/day12.1.png)
    
#### 2. Removing items from dictionaries:
    
#### pop() and del :
    
pop() methods is used to remove key value pairs from dictionary and del is used to remove entire dictionary.
![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/248b24013cd46f95ab08af716b515efed28013a3/images/day12.2.png)
    
For learning more about [dictionaries](https://docs.python.org/3/tutorial/datastructures.html)

# Day13
Today I am creating KBC(Kaun banega crorepati) using my concepts of loop and list .
Here is the code ,Hope you get some insight
![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/9ce08a5f1457450bc356db10fe018b6a00d40c13/images/day13.png)
# Day14
### Exception handling :
Exception handling is the way of dealing with unwanted errors in programs.
one of the way of exception handling by using try and except
### try and expect:
#### Syntax: 
    
    try:
     #statements which could generate 
     #exception
    except:
     #Soloution of generated exception
     
#### Example :
    
    try:
      num = int(input("Enter an integer: "))
    except ValueError:
      print("Number entered is not an integer.")
    
![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/2bc8234800f2617978c7a5b232cbcb75007cd49d/images/day14.png)
    
### Finally clause:
Finally is also type of exception handling  it is use when some statement or code had to be excecuted anyway .
finally is executed no matter what error occured or not (it also executed if it is running after return 0)
### Syntax: 

          try:
             #statements which could generate 
             #exception
          except:
             #solution of generated exception
          finally:
              #block of code which is going to 
              #execute in any situation
    
### Example:
![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/b42bf4f6336259efaca9453664ad69e8547022a7/images/day14.1(finally%20exception%20handling).png)
    
### Output:
![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/b42bf4f6336259efaca9453664ad69e8547022a7/images/day14.3(finally%20output).png)

In the above index is out of range so error occured and code inside except: is executed and after that code inside finally: is executed.Code inside finally: is executed whether error occurs or doesnot occurs.
# Day15    
#### Raising custom error in python 
In python, we can create custom error by using `raise` keyword .
We raise error to throw the exception from program .
Lets see a example:
** Objective: **To throw error if user enter number not between 1-4.
![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/896630d72319225dedf3c67fec86cd2da61bbcda/images/day15.png)
    
### if....else in one line
There is a shorthand syntax for if...else statement that can be used when condition is simple and codeblocks to be executed is short.
`Caution:`It is not used when codeblock is long and complex as this reduce code readability.
Here is a sample example :
![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/4fce9737af324129a0bb28d60b2aeca04d994257/images/day15.1(shorthand%20if%20else).png)
    
# Day16
### Object Oriented Programming
lets get start with some difference betweem POP and OOP
Procedure Oriented Programming(POP): Total activity is divided into multiple functions and we call those based on our requirements.
Object Oriented Programming(OOp) : Total activity is divided into realtime entities called objects.
* **Class** : Class is a blueprint/model which contains different entity inside it like properties(variable) and method(actions) which is inherited by objects.
* **Objects** : Objects is the physical existence of class.
![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/12ea7a5ff67055b3d7e5119c666257236970d312/images/day16%20class%20and%20object%20difference.png)
    
Here is a simplest program that reflects OOP in python :
![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/12ea7a5ff67055b3d7e5119c666257236970d312/images/day16%20(class%20and%20objects).png)

# Day17
### File handling 
Before performing any operation on file we have to know about the modes of file handling 
* Read : 'r' it allows reading file 
* Write : 'w' it allows to write in file 
* Append : 'a' it allows to append in file

Here is simplest program to clear your basic in filehandling
![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/bd7fb9cd630c002e2432142a9ace11fefbfde348/images/day17.png)    

You can practice more on file handling [Click here for read in filehandling](https://github.com/Utshav-paudel/100Daysofcode/blob/d8e2e0436a7fd8c63329e93ccceb0e8546abf2c1/jupyternotebook/filehandling%20read%20file.ipynb)

You can practice more on file handling [Click here for write in filehandling](https://github.com/Utshav-paudel/100Daysofcode/blob/d8e2e0436a7fd8c63329e93ccceb0e8546abf2c1/jupyternotebook/filehandling%20write%20file.ipynb)
 
    
# Day18
### Enumerate funciton in python:
Enumerate function is a built in function in pythons that allows you to loop over a sequence such as list,tuple,string and get the `index` and value of element at the sametime. Some basic examples on how it works are shown below :
![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/b5a1f1590a9914ddbf2d392fd229f74db8e2411e/images/day18.png)
# Day19
### Importing in python:
Importing in python is the process of loading code from a python module to the current script.This allows you to use functions and variables defined in the module in your current script. You can simply import any module by writing import followed by the name of the module.
for e.g:
```python
import math
```
After importing math function as shown above you can use various function provided by math module like sqrt(),floor() and manymore

sample:

```python
    import math 
    square_root=sqrt(9)            
    floor_number=floor(4.676)
```
### from keyword
from keyword is used to import specific function from module .
```python
    from math import sqrt
```
### importing everything
we can everything available on module by using  from followed by module* But this isnot recommended because it make harder to understand where the specific function and variables are coming from.
```python
from  math import*
```
### The 'as' keyword
We can rename the module in python by the use of as keyword 
for e.g:
```python
import pandas as pd
import math as m
```
### The dir function
Python has built in function dir that allow you to view all the functions and variable available in modules.It help to understand and explore new module .
    
for e.g:
```python
import math
print(dir(math))
  ```

# Day20
### if ```__name__=="__main__"``` in python
This is a common idom used in python to determine whether the module imported should run directly or use as module . So  when we import any module it get executed 
directly in our script and to avoid this direct execution we used ```__name__=="__main__"```.
one sample is given below:
### Before using ```__name__=="__main__"```
We can see that welcome() function is running directly after importing side module in main script and output get printed twice one from direct execution of module and another from calling of function after importing module.
![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/51c29591d43b7ef38334668f064a292911f3c2b8/images/day20(before%20using%20of%20name==main%20idom).png)
### After using **__name__=="__main__"** welcome() function is not executed direclty.
![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/dcc57ae4b1f1bc69e4ccb430621ee6d75f31227f/images/day20(after%20using%20name==main%20idom).png)
So the main use of ```__name__=="__main__"``` is to import any module without running it functions directly.
   
   
# Day21
### Lambda Function 
This funcion is also known as anonymous function in python because it does have any name like function but behaves like function
syntax:
```lambda_expression= lamda (parameter list)=expression```
For e.g:
```python
f= lambda a:a*a
print(f(5))
```
Above lamda function is used to find square

# Day22
### Webscrapping 
Web scraping refers to the extraction of data from a website. This information is collected and then exported into a format that is more useful for the user.

* first we will install request library by using requests library, we can fetch the content from the URL given
```python
pip install requests
```
* Also we will install beautiful soup that helps to parse(change format) data and fetch the details the way we want. You can use a beautiful soup library to fetch data using Html tag, class, id, css selector and many more ways.
```python
pip install beautifulsoup4
```
I am going to show you a sample of scrapping method and final results of it in excel file 
* Scrapped website [Link](https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets)
* Code that has done scrapping is given below :
    
![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/dd706441cafaa4e1374d620215a33d6134d467f7/images/day22.png) 
    
* beautiful data after scrapping:
    
![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/0937bf6d6fde35fd2c7c0965845035a08dfd9a86/images/day22(scrapped%20data).png)

You can learn more on HTTP and requests [from here](https://github.com/Utshav-paudel/100Daysofcode/blob/46d4893b6d0336ee3b33359efd3e99db92595aa3/jupyternotebook/Requests_HTTP.ipynb)
    
# Day23
Today we are applying our learning and scrapping data from website of tata ipl auction 2022
* Here is the sample code that does all our scrapping:
  
![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/35ba7e062a60e3cca244f7831414672860a23ef3/images/day23.png)
    
* Data obtained after scrapping:
![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/35ba7e062a60e3cca244f7831414672860a23ef3/images/day23(scrapped%20data).png)
# Day24
### Map,reduce and filters function in python.
In python map,reduce and filters are built in function that allows you to apply a function to the sequence of element and returns a new sequence.These functions are called higher order function because they takes functions as arguments.
```Note:we can use lamda fucntion to make it more easier and efficient```
lets learn each of them .
* <strong>Map function</strong>
Map function simply performs the function on the given iterable sequence and return a whole new sequence of data.
 syntax:
 ```python
 map(function,iterable)
 ```
 ![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/692398c8ed0bfccf5fdccb0b4807542fbe595553/images/day24(map).png)
 
 * <strong>Filter</strong>
 Filter simply filter the sequential data according to our defined predicates(i.e function) and give us selected data that passes condition after filtering.
 syntax:
 ```python
 filter(predicate_function,iterable)
 ```
 ![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/692398c8ed0bfccf5fdccb0b4807542fbe595553/images/day24(filter).png)
 * <strong>Reduce</strong>
 ```python
 from functools import reduce
 reduce(function,iterable)
 ```
 Return is also similar higher oder function but it returns a single value output not  a list or sequence of data and ```it needs to be imported from functools.
    
   
 ![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/692398c8ed0bfccf5fdccb0b4807542fbe595553/images/day24(reduce).png)
 # Day25 
 Today I created a project using python which is coffe machine.
 [Click here for its code](https://github.com/Utshav-paudel/100Daysofcode/blob/ca68172d64863eb80a029d209471cde284b7fb24/code/day25/main.py)
 
 # Day26
 ### Importing packages reading its documentation and using it
 Python has lots of library to use we can simply use it by installing it ,importing it and reading documentataion to use it.
 Here is the sample of me using ```PrettyTable``` library by installing it,importing it.
 
 ![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/0bfb546b7ef1bdab706db6577c289aa31a91d0a2/images/day26.png)
 
 # Day27
 #### OOP is the main usecase of python and many other programming languages that solves realworld problems.
 In Day16 We have discussed basic of object and class . Today we are going to discuss about different concepts of OOP in python like:
 * #### The ```__init__()``` function
 This function is always initiated when the class is being iniated . It passes values to object properties, or other operations that are necessary to do when the object is being created.
 ![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/3e4c59900ab511763c3cf1a6d52b7930084ffc2b/images/day27(the__inti__function).png)
 
* #### The ```__str__()``` function
The __str__() function controls what should be returned when the class object is represented as a string.
![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/a22df59805b9fae296b85010c70f6ced44729672/images/day27(__str__()fucntion).png)
    
#### Objects method
Objects method is the function in objects. Let create a sample object method 
![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/f1773e78980e3265bfb41864e25425d422bfd38f/images/day27%20object%20method.png)

# Day28
### Turtle graphics and using it to make arts :
Before learning about turtle graphics let us see about importing ways once.
* from import_module import class_or_function 
![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/f0dca120c71e4bdab1aa5a80bc1f1426d54f4cae/images/day28(import%20).png)
* from import_module import*
![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/f0dca120c71e4bdab1aa5a80bc1f1426d54f4cae/images/day28%20import%20everything.png)
    
 Always remember to break down your poblem,write pseudo code and start coding .
 Here is a sample solution of problem that I created ,You can understand problem and solution by reading code and comments.
 ![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/3288dd683cf5cf459ada2cdc25257dded1fa2d9a/images/day28%20problem.png)
    
 Output:
    
 ![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/3288dd683cf5cf459ada2cdc25257dded1fa2d9a/images/day28%20solving%20problem%20output.png)
 
 # Day29
 ### Problem: Create a random walk with random color
 * solution:
 ![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/0a77accbd3ae73c6875ff21a04b9300f22838f95/images/day29randomwalkcode.png)
 * output:
    
 ![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/0a77accbd3ae73c6875ff21a04b9300f22838f95/images/day29random%20walk.png)
 
 ### Creating spirograph 
 * code:
    
 ![spirograph code](https://github.com/Utshav-paudel/100Daysofcode/blob/9eaa626c9feb758282143e25e363f47a9cfd301a/images/day29%20spirograph.png)
   
* Output:
    
 ![spirograph output](https://github.com/Utshav-paudel/100Daysofcode/blob/9eaa626c9feb758282143e25e363f47a9cfd301a/images/day29%20creating%20spirograph.png)
 
 # Day30
 Today I learned to create hirst painting which is sold in millon dollars in muesum using python.
 This learning is helping me to build strong problem solving and programming logic .
 * **Hirst painting** : We have to create similar painting
 
 ![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/07b647d65d941915f02ffc28316f4ed7cfe67e18/images/day30%20objective.png)
 
 * **Code**: My code is as follow
 
 ![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/07b647d65d941915f02ffc28316f4ed7cfe67e18/images/day30%20code.png)
 
 * **Output** : Here is final result
 
 ![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/07b647d65d941915f02ffc28316f4ed7cfe67e18/images/day30.png)
 
 # Day31
 ### Working with turtle graphics 
 #### Creating drawing app
 Using turlte I created a screen where user can draw and erase by themself
#### CODE
 ![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/f27f65a5ba91f9fc9cf937e0aa573df4a47358b0/images/day31.png)
#### Output
 ![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/f27f65a5ba91f9fc9cf937e0aa573df4a47358b0/images/day31%20drawing%20output.png)
# Day32 
## Turtle Betting race game
I have created a very fun project where six different color turtle are racing , you can bet on any color of turtle and at last winner turtle will be declared,If winner is similar to bet you will won .
This projects has been very fun it uses many concepts of python like loop,list,modules.
Here is a code for this project hope you get some insight
# Code
![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/cbda82c04134fe491e03e3feb42abfcd912c43d9/images/day32%20code.png)
# Input prompt
![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/cbda82c04134fe491e03e3feb42abfcd912c43d9/images/day32%20bet.png)
# Output
![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/b47727bec31d5cf6320b86733522330877a9265a/images/day31%20output.png)

![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/cbda82c04134fe491e03e3feb42abfcd912c43d9/images/day32%20final%20output.png)
# Day33
Today I started to create snake game and it challenge my logic to core mainly to create the movement of segment it was challenging.
### Task completed so far:
* screen
* snake body
* segment movement , snake movement
Here is a code which will be completed tomorrow for full game
![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/0f882e0afff37ca7bd0939b10db86f1ef29f1029/images/day33%20snake%20code.png)
    
# Day34
Today I continued snake game and made snake to move according to botton,created food,made snake to eat food .
It is still incomplete
### Task completed so far:
* movement of snake
* food
* consuming food by snake
You can check the code of till data [here](https://github.com/Utshav-paudel/100Daysofcode/tree/Utshav-paudel/code/day34)

# Day35
Today I completed the snake game and in total it was awesome and very fun projects . 
Here is sample of how game looks like
![snake game ](https://github.com/Utshav-paudel/100Daysofcode/blob/76b67320225331b9a7b0cabf6d23d6536129fad9/images/day35.png)

You can check this game by 
* first run this on terminal
```pip install turtle```
* And download [this](https://github.com/Utshav-paudel/100Daysofcode/tree/Utshav-paudel/code/day35) and run 

# Day36
Today I continued my learning on webscraping and scraped a website .
* **note**: find_all create list  
Here is a sample code that find joblist from timejobs website.  
![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/833ceaf26e7f591ab934d5c0d6952ed4c83cb277/images/day36%20.png)

# Day37
Today I scrapped tesla revenue where I learned about how to select specific table from many tables in website.
* use find_all to find all table and use indexing of table you want to retrieve , because find_all create list.
* scrapped website [url](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm)
* <strong>Code</strong>  
![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/a02202b8edf731a4940535a0b1f4301f868a9fe1/images/day37.png)  
* csv file  
 [click](https://github.com/Utshav-paudel/100Daysofcode/blob/a02202b8edf731a4940535a0b1f4301f868a9fe1/code/day37/tesla_revenue.csv)
# Day38
Today I learned about how to createa and work on virtual environment.  
Started to learn about streamlit which is a Interactive Data Visualization Web Application .  
Here is a sample code to create webapp using streamlit.
![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/bb00b96d8504f87422f8e9fb8ac454d0ddaccd4c/images/day38.png)
# Day38
Today I learned about list comphrension using it we can really reduce the line of codes.  
## :heavy_check_mark: list comphrension:  
List comprehension is a concise way to create lists in Python. It is a syntactic construct that allows you to create a new list by specifying an expression and an iterable, along with optional filters and conditions. Here's the general syntax:  
```python
new_list = [expression for item in iterable if condition]
```  

Here is a sample program without using list comphrension vs with using list comphrension:  
![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/d15c6f2f75ef60d01a6a1a84cfeedd838dcdd68b/images/day39%20without%20list%20comphrension.png)  
Using list comphrension:  
![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/d15c6f2f75ef60d01a6a1a84cfeedd838dcdd68b/images/day39%20using%20list%20comphrension.png)

# Day40
Today I learned about dictionary comphrension , looping in pandas dataframe and solved some problem related to it.
## :heavy_check_mark: Dictionary comphrension:  
syntax:  
```python  
new_dict ={new_key:new_value for item in list }  
```
we can also create a new dictionary from existing dictionary :  
syntax:  
```python
new_dict ={new_key:new_value for (key,value) in dict.items() }
```  
also we can use conditional statement as we did in list comphrension  
syntax:  
```python  
new_dict ={new_key:new_value for (key,value) in dict.items() if condition}
```  
Here is a sample program for dictionary comphrension :   
![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/cd1280e040a0de5f53edd3b17d239a6728be34aa/images/day40%20dict_comphrension.png)  
Here is a sample program for looping in pandas dataframe:  
![alt](https://github.com/Utshav-paudel/100Daysofcode/blob/cd1280e040a0de5f53edd3b17d239a6728be34aa/images/day40%20pandasdf_loop.png)

## Word to nato phonetic code :  
* The NATO phonetic alphabet is a standardized spelling alphabet used by NATO militaries and other organizations to communicate information over radio or telephone in a clear and unambiguous way. It uses a set of 26 code words, each representing one letter of the English alphabet, to avoid confusion between similar-sounding letters.   
Here is a code for this nato phonetic code generator.
![image](https://github.com/Utshav-paudel/100Daysofcode/blob/45bf05e456dc87ffc80b0ef8785315847d3ea2f2/images/day40natocode.png)

# Day41
Today I learned about *args and **kwargs.  
* ## (*args)  
*args is used to pass a variable number of non-keyword arguments to a function. It allows you to pass any number of arguments to a function, which are then packed into a tuple. Here's an example:  
```python
def my_func(*args):
    for arg in args:
        print(arg)

my_func(1, 2, 3)
# Output: 1 2 3
```  
* ## (**kwargs)  
**kwargs is used to pass a variable number of keyword arguments to a function. It allows you to pass any number of keyword arguments to a function, which are then packed into a dictionary. Here's an example:  
```python
def my_func(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

my_func(name="John", age=30, city="New York")
# Output: name: John, age: 30, city: New York
```
### Tkinter miles to km converter app :  
![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/8b08d3d3ad67acb014f2b230d91678d779526fb3/images/day41%20miles%20to%20km%20converter.png)
# Day42 
Today I learned about strong typing and dynamic typing and built pomodoro app using python library tkinter.
Python is strongly, dynamically typed.  
* Strong typing means that the type of a value doesn't change in unexpected ways. A string containing only digits doesn't magically become a number, as may happen in Perl. Every change of type requires an explicit conversion.  
* Dynamic typing means that runtime objects (values) have a type, as opposed to static typing where variables have a type.
for e.g:  
```python
a = 5 #int
a= "ram" # string
```  
In above program a is firstly integer and later assigning string chages it to string this is called dynamic typing.  
## Pomdoro app some glimpse  
You can check full code [here](https://github.com/Utshav-paudel/100Daysofcode/tree/20324106cb5b59bb1e05a0b9f63fd7e5054b4a50/code/day42)
![alt](https://github.com/Utshav-paudel/100Daysofcode/blob/20324106cb5b59bb1e05a0b9f63fd7e5054b4a50/images/day42%20.png)

# Day43
Today I made password mananger app using tkinter it save your details in file.txt using file handling and also can generate your password.  
It is safer to save local than online .
click [here](https://github.com/Utshav-paudel/100Daysofcode/tree/dbba964e915e0f32bd3585298c936859a8add30c/code/day43) for full code.
![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/dbba964e915e0f32bd3585298c936859a8add30c/images/day43%20password%20manager.png)
 # Day44
 Today I updated some features in my password manager by using json.load() , json.dump() , json.update() technique. some details of updates are:  
 * data that user entered will be saved in json format .
 * user can search their saved email and password .
 * handle all exception that can crash program like if file doesnot exist it will be created using try and except.
 
 Final app look like this :  
 ![image](https://github.com/Utshav-paudel/100Daysofcode/blob/9cd60b43b5c46041cc51c7214f07da84a82b1fc0/images/day44%20password%20manager%20updated.png)
 
 [click](https://github.com/Utshav-paudel/100Daysofcode/tree/46b484454a143cb12d2c7d1abdf19d555dce373a/code/day44) here for final app code
 
# Day45
Today I made flash card app using tkinter , In this app you will be shown french word first and after 3 seconds you will be given it english translation . If you know answer and click tick button the word will not be shown again but if you didnot know answer and click cross button the word will be shown again.  
<strong>Highlights of app</strong>
* You will select ✓(If you know) and ❌(if you dont know)  
* The word you know will not be repeated
* The translation of french to english will be shown after 3 seconds.

some glimpse of app:  
![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/79bb2667f4412f3d7c6e6a479202e08ed73da6b0/images/day45%20flash%20card%20app.png)
After 3 seconds it will show translation
![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/79bb2667f4412f3d7c6e6a479202e08ed73da6b0/images/day45%20flash%20card%20result.png)  
[click](https://github.com/Utshav-paudel/100Daysofcode/tree/79bb2667f4412f3d7c6e6a479202e08ed73da6b0/code/day45) here for full code.

# Day46
Today I learned about API and built some project using api  
<strong> API</strong>  
An api a set of commands,functions,protocols and object that programmer can use to create software or interact with an external system.  
* API endpoints : API endpoints are the specific digital location where requests for information are sent by one program to retrieve the digital resource that exists there  
* API requests : A request includes the URL of the API endpoint and an HTTP request method. The method indicates the action you want the API to perform. Here are some of the most common methods:

GET retrieves data from an API.
POST sends new data to an API.
PATCH and PUT update existing data.
DELETE removes existing data.

Also I learned about HTTP Status code  
* 1xx : Informational
* 2xx : Success
* 3xx : Redirection
* 4xx : Client error
* 5xx : Server error
## Kanye west quote generator app
I also built kanye west quote generator app using  kanye.rest API  
[**Kanye West Quote generator app**](https://github.com/Utshav-paudel/100Daysofcode/tree/77b5e9617d3ed22c680d3afb3f6cfe4d1d23eaef/code/day46/kanye%20west%20quote%20app)  
![alt](https://github.com/Utshav-paudel/100Daysofcode/blob/f9df2f1953f08224bf7508a75b2f686c741318f4/images/day46%20kanye%20west%20quote%20generator.png)

## ISS checker
This program check ISS satellite if it is overhead you and its night then it will send email to your mail and tell you that iss is overhead.  
[**Iss satellite checker**](https://github.com/Utshav-paudel/100Daysofcode/tree/77b5e9617d3ed22c680d3afb3f6cfe4d1d23eaef/code/day46/iss%20overhead)  
Here is a sample of code :  
![alt](https://github.com/Utshav-paudel/100Daysofcode/blob/77b5e9617d3ed22c680d3afb3f6cfe4d1d23eaef/images/day46%20iss%20checker.png)

# Day47
Today I revised my knowledge on intermediate Html before getting started with webscrapping and selenium . 
* I got to know that tags under meta are very important thing for seo optimization. 
* we should prefer ```<strong>``` in place of ```<bold>``` tag , also ```<em>``` in place of ```<i>``` tag because they help you to highlight expressions that you think are important, and which represents a web page's interest.  
Here is sample website I build today as part of learning using Html only.  
![alt image](https://github.com/Utshav-paudel/100Daysofcode/blob/d9820184d4760985873c751437f340ca55c86038/images/day47.png)

# Day48
Today I revised my knowledge about css before getting started with webscrapping in python.  
<strong>CSS selector</strong>
* element selector  
Directly selects Html element for styling
```css
img
{
}
```
* class selector  
Select element on the basis of it class name , One page can used same class name in different items.  
```css
.class_name
{}
```  
* id selector  
The id of an element is unique within a page, so the id selector is used to select one unique element!  
```css
#id_name
{}
```  
Here is a sample css written that give you basic idea.  
![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/cbcebbfc228fd5dcf98eaa44196e50fced54ebeb/images/day48.png)
# Day49
Today I learned more about intermediate css like display properties,css positioning,font-styling.  
## Display property in css  
The display property is used to control how an HTML element is displayed on a webpage.  
There are several possible values for the display property, including:  
* block: Makes the element a block-level element and takes up the full width of its parent container.
* inline: Makes the element an inline-level element and takes up only as much width as necessary.
* inline-block: Makes the element an inline-level block container, meaning it behaves like an inline element but can have a width and height set.
* none: Hides the element from the page entirely, effectively removing it from the document flow.
* flex: Turns the element into a flex container, allowing for flexible layouts with child elements.
* grid: Turns the element into a grid container, allowing for grid-based layouts with child elements.  
## Css positioning  
There are four main types of CSS positioning: static, relative, absolute, and fixed.  
* Static positioning is the default position of elements on a webpage and they flow in the order they appear in the HTML document.  
* Relative positioning allows elements to be positioned relative to their original position, with the use of the top, bottom, left, and right properties.  
* Absolute positioning positions elements relative to their nearest positioned ancestor, or the document body if no ancestor is found.  
* Fixed positioning positions elements relative to the browser window and the element stays in the same position even when the page is scrolled.

# Day50
  Today I revised by concepts on webscrapping and learn how to scrapped any website using css selector and also with html using beautifulsoup.  
### Here is a sample program that extracta all news and its details like link,upvote and atlast it display news with highest upvote.  
  ![image](https://github.com/Utshav-paudel/100Daysofcode/blob/03fe26307fdcec41d1d1ec3900bb110c5527a6c9/images/day50%20updated.png)
    
 ### Here is the snippet of output 
  ![image](https://github.com/Utshav-paudel/100Daysofcode/blob/03fe26307fdcec41d1d1ec3900bb110c5527a6c9/images/day50%20final%20output.png)
  
# Day51
Todat I completed a project in webscrapping where user inputs the date and get top 100 music of that date.  
Here is a code snippet for the above program:  
![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/5717ca0621c5f2e426c4820d63a6d0e0125ffab9/images/day51%20final.png)  
Output looks like:  
![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/5717ca0621c5f2e426c4820d63a6d0e0125ffab9/images/day51%20output.png)  

# Day52
Todat I created a program that scrape amazon webiste and send the price of product you selected to your email.
In this project I learned following things
* to scrape website like amazon you have to pass header which you can generate from www.myhttpheader.com 
* also learned about smtplib library used to send email in python.  
![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/8f07bc0f2db89057fd9b4fefd6d781f8e26ef2fd/images/day52.png)

# Day53
 Today I learned about selenium,Selenium is an open-source tool that automates web browsers.  
 Using selenium I created a program that automatically scrapped the require data from a website and store it json format.  
 ![alt image](https://github.com/Utshav-paudel/100Daysofcode/blob/9e0ba608d6510bb8f434183bf7cf22bd73f95d36/images/day53.png)
 
 # Day54
 Today I created bot using selenium that play web game called cookie clicker and upgrade item in enough points.  
 ![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/d26a98393eb5ef8421ec9f61ca4ca272541cff41/images/day54.png)
 
 # Day55
Today I get started with flask which is a framework in python. I learned about decorator,some basic of shell commands.Here is a snapshot of what I learned.  
 * Decorator
 Python decorators is a technique for changing the behavior of an existing function without changing actual code inside the function.  
   
here is a sample of decorator and how it works  
![decorator](https://github.com/Utshav-paudel/100Daysofcode/blob/46bc09edfd96362a177003bf0515ba09b382e6f7/images/day55.1.png)

Here is a simplest way to create flask app:  
![flask app](https://github.com/Utshav-paudel/100Daysofcode/blob/46bc09edfd96362a177003bf0515ba09b382e6f7/images/day55.2.png)
# Day56
Today I learned about debugg mode,working with flask url,and more about advnaced decorators.Below is some explanation and snapshot of what I learned today.  
* Debugg mode:   
When debug mode is on it allows automatic reload. 
```python
if __name__ == "__main__"
    app.run(debug = True)
```  
 * Working with flask url:  
You can modify flask url to work like you want here is sample  
```python
@app.route("/<name>/<int:number>")
def greet(name, number):
    return (f"Hello {name}! You are {number} years old")
```  
* rendering html elements with flask
* advanced decorators.  
Here is a decorator that I created that check authenication of login
![creating decorators](https://github.com/Utshav-paudel/100Daysofcode/blob/2d1ab1a3eb7bef5360210140c561f21686857948/images/day56%20advanced%20decorator.png)  
Here is snapshot all concept I used in sample flask app.  
![image of sample flask app](https://github.com/Utshav-paudel/100Daysofcode/blob/2d1ab1a3eb7bef5360210140c561f21686857948/images/day56.png)


# Day57
## Jinja:  
Provide flask template for creating website with simple and organized file structure.

<strong>we can use python functionalities in html file using '{{ }}' double braces. Its python file should be implemented in .py</strong>  
Note: Template should be inside `templates` file which is index.html file generally  
  
here is sample code that use jinja methods to import python functionalities in website  
[day57  code](https://github.com/Utshav-paudel/100Daysofcode/tree/8129174a158d1cf5f86d19747710208a83925c6a/code/day57)  

![image of day57](https://github.com/Utshav-paudel/100Daysofcode/blob/2485973db90d2bdd2fcef7697bfd5f914465c454/images/day57.png)
# Day58
Today I learned about using multiline template and generating url  in jinja and applied them on my server.  
you can check full implementation on this [day 58 code](https://github.com/Utshav-paudel/100Daysofcode/tree/59d4e61c2b638427dbaceb2519794ca18f60da56/code/day58)
* Multiline is  usef for thing like using for loop , if else condition inside html file  
```html
<h1>{% for i in range(5): %} </h1>
<h2>{{ hello }}</h2>
{%endfor%}
```
![](https://github.com/Utshav-paudel/100Daysofcode/blob/389b056dbfeef1a8644250ba6afb98c682d3a172/images/day58%20.png)  

* URL building with flask
```html
<a href="{{ url_for('function_name',other parameter)}}">press</a>

```   
![](https://github.com/Utshav-paudel/100Daysofcode/blob/59d4e61c2b638427dbaceb2519794ca18f60da56/images/day58%20URL%20linking.png)

# Day59
Today, I learned about using Bootstrap to build responsive websites. Bootstrap is a popular front-end development framework that provides pre-built components and styles to help developers create beautiful, responsive websites quickly and easily.

To start building a website with Bootstrap, it's important to first create a mockup or wireframe of your website design. This can help you plan out the layout and structure of your website, and ensure that it meets your requirements and goals.

I also learned about some of the key features of Bootstrap that make it easy to create responsive websites. These include:

Grid system: Bootstrap's grid system is based on a 12-column layout, which can be easily customized to fit the needs of your website.
Responsive breakpoints: Bootstrap includes responsive breakpoints that allow you to adjust the layout of your website based on the size of the user's screen.
Pre-built components: Bootstrap provides a variety of pre-built components, such as navigation menus, forms, and modals, that can be easily customized to fit your website's design.
Overall, I found today's lesson on Bootstrap and mockups to be very helpful, and I'm excited to start building my own responsive websites using this framework. Tomorrow, I plan to dive deeper into the grid system and explore how to use it to create complex layouts.  
    Here is a sample of website that I built today.
![](https://github.com/Utshav-paudel/100Daysofcode/blob/49c027f555570956d34af2b565b319e5c9f91307/images/day59.png)

# Day60
Today, I created a falsk app that is used for iris flower classification based Decision tree algorithm and deployed it in flask server to make it user interactive.  
    Here is demo of project :   
    ![](https://github.com/Utshav-paudel/100Daysofcode/blob/ade073258e305b7168a9ac046cbae3bc97520fdd/images/project%20demo.png)
    * [Iris flower classificaiton webapp](https://github.com/Utshav-paudel/Iris-flower-calssification-webapp)
# Day61
* Today I learned about super() method in python which is used incase of multiple inheritance it allow us to call any method or function from parent class in base class.
Here is a sample hope you get some insights
![python-super](https://github.com/Utshav-paudel/100Daysofcode/blob/1cfbc464ffcfe3adb806ed3fbfa53bc9f486290e/images/day61%20super.png)
# Day62
* Today I learned more on webscrapping especially dealing with loading more pages , I have scrapped around 1.1k articles from kathmandu post for a project using beautiful soup. You can deal with pagination using json file available in network developer tool. Since the kathmandu post didnot have proper json showing changes in pages I use selinum to automate the load more option and scrapped all data using beautiful soup.
# Day63 
* Today I started learning FastAPI and learn about FastAPI request methods , also worked on simple student register system where I added functionality for adding student, searching student a, searching course , updating passed student and displaying results using python and learned about some method of regex to manage desire input , used datetime module to check various condition of update status like if student has date of later than today or if the date is not correct format.
* Implemented logging in python which keep tracks of the exception or any failure in code which makes debugging a lot more easier as failure are easier to find by logging
# Day 64
* As a part of learning fast API today I built a webapp that accept image and using deep learning to model to classify it.
