import random

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

    def receive_attack(self, damage):
        self.__health -= damage
        if self.__health <= 0:
            print(f"{self.get_name()} has died!")

    def attack(self, target):
        damage = random.randint(self.get_level() * 2, self.get_level() * 4)
        target.receive_attack(damage)
        print(
            f"{self.get_name()} attacked {target.get_name()} and caused {damage} damage!"
        )


class Hero(Character):
    def __init__(self, name, health, level, hability):
        super().__init__(name, health, level)
        self.__hability = hability

    def get_hability(self):
        return self.__hability

    def display_details(self):
        return f"{super().display_details()}\n Hability: {self.get_hability()}\n"

    def special_attack(self, target):
        damage = random.randint(self.get_level() * 5, self.get_level() * 8)
        target.receive_attack(damage)
        print(
            f"{self.get_name()} used {self.get_hability()} and attacked {target.get_name()} and caused {damage} damage!"
        )


class Enemy(Character):
    def __init__(self, name, health, level, type):
        super().__init__(name, health, level)
        self.__type = type

    def get_type(self):
        return self.__type

    def display_details(self):
        return f"{super().display_details()}\n Type: {self.get_type()}\n"


class Game:
    """Class Orchestrator of the game"""

    def __init__(self) -> None:
        self.hero = Hero(name="Lucas", health=100, level=5, hability="Super Power")
        self.enemy = Enemy(name="Bat", health=80, level=5, type="Flying")

    def start_game(self):
        print("Starting Game...")
        while self.hero.get_health() > 0 and self.enemy.get_health() > 0:
            print("\n Characters Details:")
            print(self.hero.display_details())
            print(self.enemy.display_details())

            input("Tap Enter to attack")
            choice = input("Choose (1 - Normal Attack, 2 - Special Attack):")

            if choice == "1":
                self.hero.attack(self.enemy)
            elif choice == "2":
                self.hero.special_attack(self.enemy)
            else:
                print("Invalid choice")

            if self.enemy.get_health() > 0:
                self.enemy.attack(self.hero)

        if self.hero.get_health() > 0:
            print("Congratulations, you won!")
        else:
            print("Game Over, you lost!")


# Game instance and start battle
game = Game()
game.start_game()
