from random import randint


class Card:
    def __repr__(self):
        return str(self.__class__.__name__)

    def interaction(self, agent):
        raise NotImplementedError

    def destroy(self):
        raise NotImplementedError


class Agent(Card):
    hp = 12
    gold = 0 
    weapon = None

class Monster(Card):
    def __init__(self, hp=0, name=""):
        self.hp = hp if hp else randint(1, 10)
        self.name = name if name else "Monster"

    def interaction(self, agent):
        if agent.weapon:
            hp = self.hp
            self.hp -= agent.weapon.damage
            agent.weapon.damage -= hp
            agent.weapon = None if agent.weapon.damage <= 0 else agent.weapon
        hp = self.hp
        self.hp -= agent.hp
        agent.hp -= hp
        return [
            None if self.hp <= 0 else self,
            None if agent.hp <= 0 else agent
        ]
    

class Sword(Card):
    def __init__(self, damage=0):
        self.damage = damage if damage else randint(1, 10)

    def interaction(self, agent):
        if not agent.weapon:
            agent.weapon = self
        elif self.damage > agent.weapon.damage:
            agent.weapon = self
        return [None, agent]


class Elixir(Card):
    def __init__(self, hp=0, color=""):
        self.hp = hp if hp else randint(1, 10)
        self.color = color
    
    def interaction(self, agent):
        agent.hp += self.hp
        return [None, agent]


class Gold(Card):
    def __init__(self, value=0):
            self.value = value if value else randint(1, 5)

    def interaction(self, agent):
        agent.gold += self.value
        return [None, agent]