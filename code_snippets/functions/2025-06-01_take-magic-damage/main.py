def take_magic_damage(health, resist, amp, spell_power):
    total_damage = spell_power * amp 
    damage_taken = max(0, total_damage - resist)
    return health - damage_taken
