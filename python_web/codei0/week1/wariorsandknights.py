class Warrior:
    def __init__(self, health=50, attack=5):
        self.health = health
        self.attack = attack

    @property
    def is_alive(self):
        return self.health > 0
class Knight(Warrior):
    def __init__(self, health=50, attack=7):
        super().__init__(health, attack)

class Army:
    def __init__(self):
        self.units = []

    def add_units(self, unit_type, quantity):
        self.units = [unit_type() for i in range(quantity)]

class Battle():
    def fight(self, army1, army2):
        while army1.units and army2.units:
            if fight(army1.units[0], army2.units[0]):
                army2.units.pop(0)
            else:
                army1.units.pop(0)
        return bool(army1.units)


def fight(unit1, unit2):
    while unit1.is_alive and unit2.is_alive:
        unit2.health -= unit1.attack
        if not unit2.is_alive:
            break
        unit1.health -= unit2.attack
    return unit1.is_alive

if __name__ == '__main__':
    chuck = Warrior()
    bruce = Warrior()
    carl = Warrior()
    dave = Warrior()
    mark = Warrior()
    assert fight(chuck, bruce) == True
    # assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    # assert dave.is_alive == False
    # assert fight(carl, mark) == False
    # assert carl.is_alive == False
    army_1 = Army()
    army_2 = Army()
    army_1.add_units(Warrior, 20)
    army_2.add_units(Warrior, 21)
    battle = Battle()
    battle.fight(army_1, army_2)
    # battle tests
    my_army = Army()
    my_army.add_units(Knight, 3)
    enemy_army = Army()
    enemy_army.add_units(Warrior, 3)

    print("Coding complet? Let's try tests!")

