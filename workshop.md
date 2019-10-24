# Python Text-Base Game

using an online [IDE](https://en.wikipedia.org/wiki/Integrated_development_environment) **[REPL.it](https://repl.it)**

## Python :snake:

#### Python info:

Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991. It is used for Machine Learning, Websites, Data Processing, and so much more! Python is an interperted language running directly from code written and doesn't require any pre compiling allowing for simple coding. Python has easy to remember and clean looking syntax and code. Python code is great for beginners and experts alike with its simple and advanced capabilities.

## Repl.it

Create a new repl and choose python. Make sure its specified as Python or Python 3. **Do Not Use Python 2**

![repl it image](https://github.com/lowell-dev-club/python-text-game/blob/master/replit.png?raw=true)

## Print Statment

The print statement is used to output messages.  
Code:
```python
print('Hello World!')
print('You enter a dark room.\nThe door creaks open.')
```
Output:  
> Hello World!  
> You enter a dark room.  
> The door creaks open.

The print statement has a format tool to allow for number and text(strings to be printed together).  
Code:
```python
print(f'Hello World! {5}')
```
Output:  
> Hello World! 5

## Variables

Variables hold data. Data can be numbers(integers, decimals) and text(strings) and much more!  
Code:
```python
variable = 404
anotherVariable = 'Hello There!'
print(f'{anotherVariable} {variable}.')
```
Output:  
> Hello There! 404.

**Make sure to come up with unique variable names**  

## User input

User input is a way to get input from users for your text game.  
Code:
```python
variable = input('What\'s your age? ')
print(f'Your age is {variable}')
```
Output:  
> What's your age? 16  
> 16

## If statments

Use if statments to check if something is true, for example, 5 == 5. Use this in conjunction with user input to determine what to do with user input. make the story go right, left, up all based off what the user inputs. You can use elif(else if) and else statments to run different code if the first if statment isn't true for example, 5 == 6 is False.
```python
var = input('Which way do you walk? ')
if var == 'right':
    print('You walk to the right.')
elif var == 'left':
    print('You walk to the left.')
else:
    print('You walk through the door.')
```
Output:
> Which way do you walk? left  
> You walk to the left.

## Example Game

Example game.  
Code:
```python
import random

print('It was a dark and stormy night.')
print('You are inside your house and you hear a knock on your door.')

whereToGo = input('Do you answer the knock? ')

# use .lower() next to a variable to make any text lowercase. ('HELLO').lower() = 'hello'
if whereToGo.lower() == 'yes':
    print('You open your door.')
    randNum = random.randint(1,2)
    if randNum == 1:
        print('You are killed by the Boogeyman.')
    else:
        print('John Wick kills a Boogeyman right in front of you saving you from death.')
else:
    print('You hear creaking in the attic above you.')
    randNum = random.randint(1,2)
    if randNum == 1:
        print('You are crushed by your roof.')
    else:
        print('Everything goes away the TV turns back on startiling you.')

```
View the code file [here](game.py)  
Test the game out [here](https://repl.it/@RAFAELCENZANO/text-based-game)
