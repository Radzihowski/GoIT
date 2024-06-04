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
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
    print("Coding complet? Let's try tests!")

