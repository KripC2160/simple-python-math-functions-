
#STILL WIP

# var = 762 
# if (var - n1) % 2 == 0:
#   return True
# else:
#   return false


def is_member(num, n1):
    if (num - n1) % 2 == 0:
        return (num -n1) % 2
    else: 
        return False

print(is_member(523, 431))