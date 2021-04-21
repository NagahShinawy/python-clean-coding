"""
created by Nagaj at 21/04/2021
"""
# readability
# python variables
from typing import List, Dict

IS_VALID = True

developers: List[Dict] = [
    {"name": "John", "title": "Java Developer", "team": "X001", "is_oncall": True},
    {"name": "James", "title": "Python Developer", "team": "A001", "is_oncall": False},
    {"name": "Leon", "title": "Java Developer", "team": "X001", "is_oncall": False},
    {"name": "Sara", "title": "Devops", "team": "Y001", "is_oncall": True},
]

oncall_developers = [developer for developer in developers if developer["is_oncall"]]

for oncall_developer in oncall_developers:
    print(oncall_developer)

# ###########  python control structure  #####################

cost = 100

if cost == 100:
    """DO Something"""
elif cost == 10:
    """ Do Something """
else:
    pass

# Ternary statement: is a statement is run in single line

speed = 50

warning = "Danger" if speed >= 100 else "Safe"

print(warning)


# ##################  Classes  #########################

class Vehicle:
    def __init__(self):
        """Base class constructor"""


class Car(Vehicle):

    def __init__(self):
        """class constructor"""
        super().__init__()

    def drive(self):
        """Drive the car"""


bmw = Car()
bmw.drive()
