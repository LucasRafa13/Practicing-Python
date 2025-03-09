# Character: Mother Class
# Hero: Controlled by the User
# Enemy: User's opponent


class Character:

    def __init__(self, name, health, level) -> None:
        self.__name = name
        self.__health = health
        self.__level = level

    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def get_level(self):
        return self.__level

    def display_details(self):
        return f"Name: {self.get_name()}\n Health: {self.get_health()}\n Level: {self.get_level()}\n"


class Hero(Character):
    def __init__(self, name, health, level, hability):
        super().__init__(name, health, level)
        self.__hability = hability

    def get_hability(self):
        return self.__hability

    def display_details(self):
        return f"{super().display_details()}\n Hability: {self.get_hability()}\n"


class Enemy(Character):
    def __init__(self, name, health, level, type):
        super().__init__(name, health, level)
        self.__type = type

    def get_type(self):
        return self.__type

    def display_details(self):
        return f"{super().display_details()}\n Type: {self.get_type()}\n"


# Example usage

hero = Hero(name="Lucas", health=100, level=15, hability="Super Power")
enemy = Enemy(name="Bat", health=50, level=3, type="Flying")
print(hero.display_details())
print(enemy.display_details())
