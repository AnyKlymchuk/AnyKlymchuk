'''Task2. Create a class Human, everyone has a name, create a method in the
class that displays a welcome message to each person. Create a class method
in the class that returns information that it is a species of "Homosapiens". And
in the class create a static method that returns an arbitrary message.'''
class Human:
    species = "Homosapiens"  # Class attribute for the species

    def __init__(self, name):
        self.name = name

    def welcome_message(self):
        print(f"Welcome, {self.name}!")

    @classmethod
    def get_species(cls):
        return cls.species

    @staticmethod
    def arbitrary_message():
        return "This is a static message."

# Create instances of the Human class
person1 = Human("Alice")
person2 = Human("Bob")

# Call the welcome_message method for each person
person1.welcome_message()
person2.welcome_message()

# Call the class method to get the species
print(f"Species: {Human.get_species()}")

# Call the static method to get an arbitrary message
print(Human.arbitrary_message())
