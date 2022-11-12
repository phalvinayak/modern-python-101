"""
Decorators:
-----------
They are used to implement particular behavior for our classes.

Summary:
--------
1. property - Acts like a instance variable, no need to call like function.
2. static method - Directly called from the class.
3. class method - Returns a new instance of the class.
4. getter & setter - Used for `Data Encapsulation`.

Info:
-----
We can mark the class as `final` so that no other class can subclass it.

"""
from __future__ import annotations
from enum import Enum, auto
from datetime import datetime
from typing import final


class Role(Enum):
    """Roles for staff members"""

    ASSOCIATE = auto()
    SUPERVISOR = auto()
    MANAGER = auto()


# ------------------------------------------------------------------------------------------
class Person:
    def __init__(self, fname: str, lname: str) -> None:
        self.fname = fname
        self.lname = lname

    def __str__(self) -> str:
        return f"Person: {self.fname} {self.lname}"

    @property
    def fullName(self) -> str:
        return f"{self.fname} {self.lname}"


# ------------------------------------------------------------------------------------------


@final
class Staff(Person):
    def __init__(self, fname: str, lname: str, staffId: int, role: Role) -> None:
        # Initialize parent /super class
        super().__init__(fname, lname)
        self.role = role
        self.staffId = staffId
        self.isStaff = True
        # Private Member
        self._dateJoined = datetime.now()
        # Dynamically create and assign instance varialbe
        match role:
            case Role.ASSOCIATE:
                self.__salary: float = 15
            case Role.SUPERVISOR:
                self.__salary = 20
            case Role.MANAGER:
                self.__salary = 25

    def __str__(self) -> str:
        return f"Staff => Name: {self.fullName}, ID: {self.staffId}"

    @classmethod
    def new(cls, person: Person, staffId: int, role: Role) -> Staff:
        """
        Create a new `Staff` instance

        NOTE: It takes `class` as the first argument and return a instance
        of that class
        """
        return cls(person.fname, person.lname, staffId, role)

    @property
    def joinedOn(self) -> str:
        """Joining date of the staff number"""
        return f"{self._dateJoined.strftime('%B %d, %Y')}"

    @property
    def salary(self) -> float:
        """`GETTER` returns the salary"""
        return self.__salary

    @salary.setter
    def salary(self, amt: float) -> None:
        """`SETTER` sets the salary after validation"""
        if self.role == Role.ASSOCIATE and amt < 15:
            print("Error! Associate cannot have salary of less than $15/Hr")
        elif self.role == Role.SUPERVISOR and amt < 20:
            print("Error! Supervisor cannot have salary of less than $20/Hr")
        elif self.role == Role.MANAGER and amt < 25:
            print("Error! Manager cannot have salary of less than $25/Hr")
        else:
            self.__salary = amt
            print(f"{self.fullName} now has a salary of ${self.salary}")


# ------------------------------------------------------------------------------------------


p1 = Person("Louis", "Zappa")
print(p1)
print(p1.fullName)


s1 = Staff.new(p1, 1234, Role.SUPERVISOR)
print(s1)
print(s1.joinedOn)
print(s1.salary)

s1.salary = 17
s1.salary = 22

s2 = Staff("Chiko", "Jones", 3245, Role.MANAGER)
print(s2)
print(s2.joinedOn)
print(s2.salary)
# ------------------------------------------------------------------------------------------


# As Staff is decared as final we cannot inherit any more.
# class HR(Staff):
#     pass


# ------------------------------------------------------------------------------------------
