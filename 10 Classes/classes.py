# A class is used for creating objects. An object has properties and methods (functions) associated with it.

# Creating a class
class User:
    # Constructor (is basically a function that runs when you instantiate an object from a class )
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

# Init or Initialize User object
majesty = User('Developer Majesty', 'developermajesty@gmail.com', '0544174142')

print(majesty.phone)