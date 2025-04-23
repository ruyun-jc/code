pizzas=['Margherita','Pepperoni','Hawaiian']
for pizza in pizzas:
    print('I like '+pizza+' pizza!')
print('I really love pizza!\n')

pets=['dog','cat','bird']
for pet in pets:
    print('A '+pet+' would make a great pet.')
print('Any of these animals would make a great pet.\n')

number=list(range(1,21))
print(number)
money=[]
for value in range(1,1000001):
    money.append(value)
print(min(money))
print(max(money))
print(sum(money))
number1=[]
for value in range(3,31,3):
    number1.append(value)
print(number1)
number2=[]
for value in range(1,11):
    number2.append(value**3)
print(number2)
number3=[value**3 for value in range(1,11)]
print(number3)

my_list=['apple','banana','kiwi','orange','grape']
print('\nThe first three items in the list are:')
print(my_list[0:3])
print('Three items from the middle of the list are:')
print(my_list[1:4])
print('The last three items in the list are:')
print(my_list[-3:])

my_pizzas=pizzas
friend_pizzas=my_pizzas[:]
my_pizzas.append('vegetarian')
friend_pizzas.append('saussage')
print('\nMy favourit pizzas are:')
for my_pizza in my_pizzas:
    print(my_pizza)
print("My friend's favourite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)

menus=('fish','crab','shrimp','beef','soup')
print('\nMenu:')
for menu in menus:
    print(menu)
menus=('fish','crab','shrimp','egg','vegetable')
print('New menu:')
for menu in menus:
    print(menu)
