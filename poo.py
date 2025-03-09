# POO

# Exemple of Class


class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def introduce_self(self):
        return f"Olá. meu nome é {self.name} e eu tenho {self.age} anos."


# Objects

person1 = Person("Lucas", 30)
message = person1.introduce_self()
print(message)  # Output: Olá. meu nome é Lucas e eu tenho 30 anos.


person2 = Person(name="Alice", age=25)
message = person2.introduce_self()
print(message)  # Output: Olá. meu nome é Alice e eu tenho 25 anos.


# inheritance


print(f"\nExample of inheritance and polymorphism:\n")


class Animal:
    def __init__(self, name) -> None:
        self.name = name

        def walk(self):
            print(f"The animal {self.name} walked")
            return

        def emit_sound(self):
            pass


class Dog(Animal):
    def emit_sound(self):
        return "Woof Woof!"


class Cat(Animal):
    def emit_sound(self):
        return "Miawwwwww!"


dog = Dog(name="Rex")
cat = Cat(name="Felix")

animals = [dog, cat]

for animal in animals:
    print(f"{animal.name} do: {animal.emit_sound()}\n")

print("\n Exemple of encapsulating:\n")


class BankAccount:

    def __init__(self, balance) -> None:
        self.__balance = balance  # Atribute Private

    def deposit(self, value):
        if value > 0:
            self.__balance += value

    def withdraw(self, value):
        if value > 0 and value <= self.__balance:
            self.__balance -= value

    def get_balance(self):
        return self.__balance


account = BankAccount(balance=1000)

print(f"Initial Balance {account.get_balance()}")
account.deposit(500)
account.withdraw(200)

print(f"Current balance: {account.get_balance()}")  # Output: Current balance: 1300
