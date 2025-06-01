health = 100
resist = 12
amp = 4 
spell_power= 25




def take_magic_damage(health, resist, amp, spell_power):
    total_damage = spell_power * amp 
    damage_taken = total_damage - resist
    return health - damage_taken
print(health)