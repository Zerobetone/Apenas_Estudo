#def is_perfect_square(num):
#    if num < 0:
#        return False
#    else:
#        sqrt = num ** 0.5
#        if int(sqrt + 0.5) ** 2 == num:
#            return True
#        else:
#            return False
#
# Exemplos de uso
#print(is_perfect_square(16))  # Deve retornar True
#print(is_perfect_square(25))  # Deve retornar True
#print(is_perfect_square(14))  # Deve retornar False


def is_perfect_square(num):
    if num < 0:
        return False

    sqrt = num ** 0.5
    return sqrt*sqrt ==num

# Exemplos de uso
print(is_perfect_square(16))  # Deve retornar True
print(is_perfect_square(25))  # Deve retornar True
print(is_perfect_square(14))  # Deve retornar False