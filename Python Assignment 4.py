##qs1##

person_dic = {"firstname": "ateeq", "lastname": "mughal", "age": 20, "city": "karachi"}
for i in list(person_dic.keys()):
    print(person_dic[i])
person_dic["qual"] = "matric"
print(person_dic["qual"])
person_dic.update(qual="university")
print(person_dic["qual"])
del person_dic["qual"]

####qs2###

d1 = {"country": "pakistan", "population": 1000, "fact": "cityoflights"}
d2 = {"country": "England", "population": 100000, "fact": "londonbridge"}
cities = {"karachi": d1, "london": d2}
for info in list(cities.keys()):
    city = cities[info]
    print("The country is", city["country"], "population is", city["population"], "the fact is ", city["fact"])

###qs3####

person = int(input("enter .."))
for x in range(person):
    #  age should be positive# 
    age = int(input("enter age.."))
    if age < 3:
        print("the ticket  is free")
    elif 3 <= age <= 12:
        print("$10")
    else:
        print("$15")


####qs4###

def favorite_book(title):
    print("my favorite book is ", title)


favorite_book("40 rules of love")

###qs5##

import random

number = random.randint(1, 30)
for chances in range(3):
    guess = int(input("guess the number......."))
    if guess == number:
        print("you have guessed correct number!!!")
        break
    elif number > guess:
        print("number is larger and u have guessed smaller")
    elif number < guess:
        print("number is smaller and u have guessed larger")
