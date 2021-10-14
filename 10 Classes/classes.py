# A class is used for creating objects. An object has properties and methods (functions) associated with it.


# Creating a class
class User:
    # Constructor (is basically a function that runs when you instantiate an object from a class )
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    # Creating a method for the User class
    def display_name(self):
        return f'{self.name} is a Software Engineer at Maverick Edifice..'

    def display_phone(self):
        return f'His phone number is {self.phone}'


# Extending a class
class Admin(User):
    # Constructor (is basically a function that runs when you instantiate an object from a class )
    def __init__(self, name, email, phone, salary):
        self.name = name
        self.email = email
        self.phone = phone
        self.salary = salary



# Init or Initialize User object
majesty = User('Developer Majesty', 'developermajesty@gmail.com', '0544174142')


# Init or Initialize Admin object
admin = Admin('Solomon Aidoo Junior', 'developermajesty@gmail.com', '0544174142', 4500)

print(admin.display_name())
