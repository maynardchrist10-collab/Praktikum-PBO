import random
class hero():
    def __init__(self, name, health, attack,armor, mana=50):
        self.name = name
        self._health = health
        self.attack = attack
        self.armor = armor
        self.mana = mana

    def __str__(self):
        return f'nama hero {self.name}'

    def __str__(self):
        return f'nama hero {self.name}'

    def diserang(self, jumlah):
        self._health = max(self._health - jumlah, 0)

    def serang(self, target):
        damage = max(self.attack - target.armor, 0)
        target.diserang(damage)
        print(f'{self.name} menyerang {target.name} dengan damage {damage}')

class marksman(hero):
    def __init__(self, name, health, attack,armor, mana=50, misschance=50):
        super().__init__(name, health, attack,armor, mana=50)
        self.misschance = misschance

    def serang(self, target):
        if random.randint(1, 100) <= self.misschance:
            print(f'{self.name} menyerang {target.name} tetapi meleset!')
        else:
            super().serang(target)

class energymarksman(marksman):
    def __init__(self, name, health, attack,armor, mana=50, misschance=50, energy=100):
        super().__init__(name, health, attack,armor, mana=50, misschance=50)
        self.energy = energy

    def serang(self, target):
        if self.energy >= 20:
            self.energy -= 20
            damage = max(self.attack * 2 - target.armor, 0)
            target.diserang(damage)
            print(f'{self.name} menyerang {target.name} dengan damage {damage},sisa energy {self.energy}')
        else:
            super().serang(target)

class healing():
    def heal(self, target):
        target._health += 20
        print(f'{self.name} menyembuhkan {target.name} sebesar 20 health')

class support(marksman, healing):
    pass

class fighter(hero):
    pass

balmond = hero ('balmond',100,15,4)
layla = marksman('layla', 80, 20, 4, 30)
nana = support('nana', 70, 10, 4, 50, 10)
energymarksman = energymarksman('energymarksman', 80, 20, 4, 30, 50, 100)

# for i in range(8):
#     layla.serang(balmond)
# print(layla.__dict__)
# layla.serang(balmond)
# balmond.serang(layla)
# # print(balmond)
# kimmy = energymarksman('kimmy', 100, 10, 4, 50, 10, 100)
# print(layla.__dict__)
# print(isinstance(layla, marksman))