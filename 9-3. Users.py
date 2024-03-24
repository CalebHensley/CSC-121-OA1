class User:
    def __init__(self, first_name, last_name, age, location, career):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.career = career

    def describe_user(self):
        print(f"User: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location}")
        print(f"Career: {self.career}")

    def greet_user(self):
        print(f"Hello, {self.first_name}!")

user1 = User("Steve", "Harvey", 67, "Atlanta", "Comedian")
user2 = User("Bill", "Gates", 69, "Seattle", "Philanthropist")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()