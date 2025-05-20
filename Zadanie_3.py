class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def take_damage(self, amount):
        amount = int(amount)
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0
        print(f"{self.name} took {amount} damage. HP left: {self.hp}")

class Warrior(Character):
    def __init__(self, name, hp, strength):
        super().__init__(name, hp)
        self.strength = strength

    def attack(self, target):
        damage = self.strength * 1.5
        print(f"{self.name} attacks {target.name} for {int(damage)} damage!")
        target.take_damage(damage)

class Mage(Character):
    def __init__(self, name, hp, mana):
        super().__init__(name, hp)
        self.mana = mana

    def attack(self, target):
        if self.mana >= 10:
            print(f"{self.name} casts a spell on {target.name} for 25 damage!")
            target.take_damage(25)
            self.mana -= 10
            print(f"{self.name} has {self.mana} mana left.")
        else:
            print(f"{self.name} tried to cast a spell but has not enough mana!")


def simulate_battle():
    w = Warrior("Thorgal", 100, 10)
    m = Mage("Merlin", 60, 20)

    print("== BATTLE START ==")
    print(f"{w.name}: {w.hp} HP, {m.name}: {m.hp} HP")

    w.attack(m)
    m.attack(w)
    m.attack(w)
    m.attack(w)
    m.attack(w)  # ostatni atak – powinno być "Not enough mana"

    print("\n== BATTLE END ==")
    print(f"{w.name}: {w.hp} HP, {m.name}: {m.hp} HP")

simulate_battle()
