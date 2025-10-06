can_create_guild = 0b1000 # 8
can_review_guild = 0b0100 # 4
can_delete_guild = 0b0010 # 2
can_edit_guild = 0b0001 # 1


def get_create_bits(user_permissions):
    return user_permissions & can_create_guild # Compares user nibble to can_create_guild nibble 

def get_review_bits(user_permissions):
    return user_permissions & can_review_guild



def get_delete_bits(user_permissions):
    return user_permissions & can_delete_guild



def get_edit_bits(user_permissions):
    return user_permissions & can_edit_guild