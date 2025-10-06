class Wizard:
    # Initialize core attributes: store base stats; derive mana and health
    def __init__(self, name, stamina, intelligence):
        self.name = name
        self.__stamina = stamina
        self.__intelligence = intelligence
        self.mana = self.__intelligence * 10   # starting mana scales with intelligence
        self.health = self.__stamina * 100     # starting health scales with stamina
    
    # Cast a fireball at the target:
    # - raise if not enough mana
    # - otherwise spend mana and apply damage to target
    def cast_fireball(self, target, fireball_cost, fireball_damage):
        if fireball_cost <= 0:
            raise Exception("spell cost must be positive") # prevent free/negative-cost casts
        if self.mana < fireball_cost:
            raise Exception(f"{self.name} cannot cast fireball")  # not enough mana
        
        self.mana -= fireball_cost               # spend mana
        target.get_fireballed(fireball_damage)   # deal damage to target

    # A wizard is alive only if health > 0 (0 is dead)
    def is_alive(self):
        return self.health > 0

    # When hit by a fireball, stamina reduces incoming damage before health is reduced
    def get_fireballed(self, fireball_damage):
        fireball_damage -= self.__stamina   # damage mitigation from stamina
        if fireball_damage < 0:             # no healing from weaker hits
            fireball_damage = 0
        self.health -= fireball_damage      # apply remaining damage

    # Drinking a mana potion: potion amount scales with intelligence, then added to mana
    def drink_mana_potion(self, potion_mana):
        potion_mana += self.__intelligence   # smarter wizards get more from potions
        if potion_mana < 0:                  # no negative potions
            potion_mana = 0
        self.mana += potion_mana             # restore mana
