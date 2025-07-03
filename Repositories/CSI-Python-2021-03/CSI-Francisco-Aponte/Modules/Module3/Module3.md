<div style="text-align:center">
        <img    src="https://files.realpython.com/media/Basic-Data-Types-in-Python_Watermarked.49e17138407b.jpg"
                title="Python" 
                width="60%" 
                height="60%" />
</div>
<br>


# Module 3: Data Types and Variables
## Data type
A data type is a category for values. The most commons data types in Python are `integer`, `float`, `strings`, and `boolean`. 

<br>

### Integer
In Python, whole numbers are called `integers`. Programmers usually count using integers. 
>Example: -2, -1, 0, 1, 2, 14, 2019

<br>

### Float
In coding, numbers with a decimal point are known as `floats`. It's Full name is <u>Decimal Floating Point Number</u>. A `double`'s full name is <u>Double Precision Decimal Floating Point Number</u>(float64).  
>Example: -1.25, -1.0, 0.5, 1.0, 1.33

<br>

### String
Programmers use the word strings to refer to blocks of text or any data made up of a sequence of characters. Strings are a single data object; They are surrounded by single quote (') or double quote (") characters. 
>Example: "a", "aa", 'Hello!', '101 Dalmatians'

<br>

### Boolean
A Boolean is a value that is represented by a single bit. This means that it is either true or false. Booleans are used as a part of logic. Various operators may determine whether a statement is true or false such as equals(`==`) or greater than(`>`).
>Example:
>
>i = 10
>
>(i < 15) is True

<br>

### Object
You may define your own data type. In <u>object oriented languages</u> such as Java or C#, everything is an object.

<br>

### Null
A null or None type represents the absence of a value. This differs from, say 0, in that 0 is present value. 

<br>

### List
An list is a list, or collection, of a certain data type. An list is treated as its own data type since it acts like a container.

<br>

## Data Types

| Data Type | Syntax | 
|-----------|--------|
| Integer | `i = 42` <br> `i:int = 42` <br> `i = int("3")` <br> converts a string with int characters into a number |
| Float | `d = float(5)` <br> is equal to 5.0 <br> `d = 5.3` |
| String | `s = "Hello World!"` <br> `s = str(42)` <br> is equal to "42" |
| Boolean | True, False, >, <, ==, >=, <=, 1, 0, and, or, not |
| Object | `o = Object()` |
| Void/Null | `o = None` |
| List | `myList = ["someValue","otherValue"]` <br> `myList[0]="updatedFirstValue"` <br> `myList.append("Third Value")` <br> `myList.extend(["combine","multiple","lists"])` |

<br>

## Variables

A variable can store a value.  In Python, programmers assign variables by using the equals sign "`=`". 

Example: 

```python
age = 21
print(age)

age:int = 22
print(type(age))
```
>21

<br>

## Class Discussion
## Answer the questions on the Markdown file located within your <u>`Module3`</u> directory (Module3.md) - `(10pts)`

<!-- Welcome! These are your questions. -->
<!-- Answer using full sentences to receive all points. -->
<!-- 

What is the difference between "42" and 42.

 - Answer: The difference between "42" and 42, is that the "" in "42" make it into a string, or a sequence of data for the program. for example in the project wehre we had to rpint our name, the letters were in between "" making those letters a string aswell. THe 42 without "" is simply just an integer.

Define the boolean operators: >, <, ==, >=, <=

 - Answer: Boolean operators are used to define operations as true or false, the operators used in these booleans are: <, which means less than, >, which means more than, ==, which means equal to, >= which means more than or equal to, and <, which means less than or equal to.

How do you address an index in an list? Write a python code that assigns 34 to a new variable by accessing the value stored in:  
        arr = [4, 3, -1, 4, 34]

 - Answer: 
 arr = [4, 3, -1, 4, 34]
print (arr[4])
brr = arr[4]
print (brr)



What is the first index of a list? Why?

 - Answer: the first index of a list is 0 for a couple of reasons. The first one is that the language of code had always been this way, while there are still other types of code that do not start at zero, hte largest ones like java and python do. Also, it makes it more clear for the program to reach a index in a list from its memory. For example in: 1, 2, 3, 4, 5.(1=0). The logic behind it is how far the numbers are from the beggining (therefore the 1 is 0 numbers from the begining. Finally, you can represent 10 different values with only 1 digit.)

Provide an original example of a null value. It must prove your understanding of the concept.

 - Answer: The difference between 0 and a null values is that a null value is simply unknown. For example, if teh problem we are facing is "how many classrooms does Colegio san ignacio have that an english teacher has given a class in?" that would be a null value becuase we do not know. The question does not have to be that specific or unknown to everyone, for example if we ask how many glasses of water did jose drink today, that would also be a null value even though jose knows how many he drank today..

Type down any class notes below this sentence:

Profesor como no fui al colegio, no pude prenguntarte como hacer la 3, busque en el internet para ver si podia aprender y aprendi como update integers de una lista y todo lo basico de una lista. Corri el codigo que puse como respuesta pero me salia: error, brr is not defined. no se como definirlo. Ya no lo estoy definiendo poniendo que brr = arr[4]?

Y lo arregle

Lackluster responses may result in point deductions.
-->

<br>

## [Next Module ->](/../../tree/main/Modules/Module4/Module4.md)