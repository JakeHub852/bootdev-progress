def remove_duplicates(spells):
    seen_spells = set()
    unique_spells = []
    for spell in spells:
        if spell not in seen_spells:
            seen_spells.add(spell)
            unique_spells.append(spell)
    return unique_spells


def alt_remove_duplicates(spells):
    # Convert the list to a set - duplicates are removed here
    unique_spells_set = set(spells)
    # Convert the set back to a list
    unique_spells_list = list(unique_spells_set)
    return unique_spells_list


def alt_remove_duplicates_short(spells):
    return list(set(spells))  