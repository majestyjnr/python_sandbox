# A class is used for creating objects. An object has properties and methods (functions) associated with it.

# Creating a class
class User:
    # Constructor (is basically a function that runs when you instantiate an object from a class )
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    # Creating a method for the User class
    def displayInfo(self):
        return f'{self.name} is a Software Engineer at Maverick Edifice. His phone number is {self.phone}.'




# Extending a class
class Admin(User):
    # Constructor (is basically a function that runs when you instantiate an object from a class )
    def __init__(self, name, email, phone, salary):
        self.name = name
        self.email = email
        self.phone = phone
        self.salary = 4500


    def setSalary(self):
        self.salary = salary
    




# Init or Initialize User object
majesty = User('Developer Majesty', 'developermajesty@gmail.com', '0544174142')

# Init or Initialize Admin object
admin = Customer('Solomon Aidoo Junior', 'developermajesty@gmail.com', '0544174142', 4500)

admin.setSalary()

print(majesty.displayInfo())
