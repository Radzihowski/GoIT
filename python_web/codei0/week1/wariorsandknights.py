class Warrior:
    def __init__(self, health=50, attack=5):
        self.health = health
        self.attack = attack
    @property
    def is_alive(self):
        return self.health > 0
    def hit(self, unit):
        unit.loose(self.attack)
    def loose(self, attack):
        self.health -= self.damage(attack)
    def damage(self, attack):
        return attack


class Knight(Warrior):
    def __init__(self, health=50, attack=7):
        super().__init__(health, attack)

class Defender(Warrior):
    def __init__(self, health=60, attack=3, defence=2):
        super().__init__(health, attack)
        self.defence = defence

    def damage(self, attack):
        if self.defence < attack
            return max(0, attack - self.defence)

    def loose(self, attack):
        if attack > self.defence:
            self.health -= attack - self.defence

class Vampire(Warrior):
    def __init__(self, health=40, attack=4, vampirism=50):
        super.__init__(health, attack)
        self.vampirism = vampirism
    def hit(self, unit):
        super().hit(unit)


class Army:
    def __init__(self):
        self.units = []

    def add_units(self, unit_type, quantity):
        self.units += [unit_type() for i in range(quantity)]

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
        unit1.hit(unit2)
        if not unit2.is_alive:
            break
        unit2.hit(unit1)
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
    # army_1 = Army()
    # army_2 = Army()
    # army_1.add_units(Warrior, 20)
    # army_2.add_units(Warrior, 21)
    # battle = Battle()
    # battle.fight(army_1, army_2)
    # battle tests
    # my_army = Army()
    # my_army.add_units(Knight, 3)
    # enemy_army = Army()
    # enemy_army.add_units(Warrior, 3)
    my_army = Army()
    my_army.add_units(Defender, 1)
    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    army3 = Army()
    army3.add_units(Warrior, 1)
    army3.add_units(Defender, 1)
    army4 = Army()
    army4.add_units(Warrior, 2)
    battle = Battle()
    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army3, army4) == True

    print("Coding complet? Let's try tests!")

