from random import *

aList = ["Jada", "James", "John", "Jusstin", "Jaden", "You suck", "Hah", "No one likes you"]

aRandomIndex = randint(0, len(aList)-1)
print(aList[aRandomIndex])

Sides = ["Fries", "rice", "corn", "dressing"]
Main = ["Vege bowl", "bbq chicken", "ribs", "salad"]

bRandomIndex = randint(0, len(Sides)-1)
print(Sides[bRandomIndex])
cRandomIndex=randint(0, len(Main)-1)
print(Main[cRandomIndex])
