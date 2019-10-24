'''
Text Based game created by Rafael Cenzano
https://repl.it/@RAFAELCENZANO/text-based-game
'''

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
