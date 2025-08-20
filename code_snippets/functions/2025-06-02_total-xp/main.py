def total_xp(level, xp_to_add):
    current_xp = level * 100 # Current XP player has based on level
    players_total_xp = current_xp + xp_to_add # Players current XP and XP gained
    return players_total_xp # Players new XP total
