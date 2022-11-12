class Character:
    """Defines a game character"""
    def __init__(self, name: str, attackPower: int, life: int) -> None:
        """Creates an instace of `Character`"""
        self.name = name
        self.attackPower = attackPower
        self.life = life

    def __repr__(self) -> str:
        return "<class `Character`>"
    
    def __str__(self) -> str:
        return f"Name: {self.name}, AttachPower: {self.attackPower}, Life:{self.life}"
    
villain1 = Character("Thanos", 400, 1500)
# Using key value pair
villain2 = Character(attackPower=300, life=800, name="Redskull")

hero1 = Character(name="Ironman", attackPower=250, life=1000)
hero2 = Character(name="Blackwidow", attackPower=180, life=800)

print(villain1)
print(villain2)

print(hero1)
print(hero2)

