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

if age < 5:
    print('your age is too little,' + str(age))
elif age > 60:
    print('your age is too old,' + str(age))
else:
    print('your age is suitable,' + str(age))

age = 17
if age < 5:
    print('your age is too little,' + str(age))
elif age < 18:
    print('sorry,your age have not enough,' + str(age))
elif age > 60:
    print('your age is too old,' + str(age))
else:
    print('your age is suitable,' + str(age))

if my_car in cars:
    print('my car have exist' + my_car)
if my_car not in cars:
    print('my car not exist ' + my_car)

empty_cars = cars[:]
empty_cars.clear()
# 确定列表是不是空的
if empty_cars:
    print('not empty:' + str(empty_cars))
if not empty_cars:
    print('empty:' + str(empty_cars))
for empty_car in empty_cars:
    print(empty_car)

