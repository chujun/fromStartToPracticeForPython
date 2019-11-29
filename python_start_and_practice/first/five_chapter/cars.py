# encoding = utf-8
cars = ['car', 'bmw', 'subaru', 'toyoa']
my_car = 'toyoa'
for car in cars:
    if car == my_car:
        print(car.upper())
    else:
        print(car)
    if car != 'bmw':
        print('welcome ' + car)
print(cars)

age = 18
if age >= 18:
    print("now , you can fly ," + str(age))
is_male = True
if age > 18 and is_male:
    print("come male")
age = 4
is_male = False
if age > 18 and not is_male:
    print("come female")
if age < 18 or age > 60:
    print("you need to be protected")
