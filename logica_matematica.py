def transformador(valor):
    if valor == 1:
        return True
    else:
        return False


def transformador_bool(valor):
    if valor is True:
        return 1
    else:
        return -1


def negacion(valor):
    # - P
    transformador_bool(valor)  # el valor es boolean, por lo que lo vuelvo un numero
    return transformador(valor * -1)  # se multiplica por *-1 para despues volverlo bool de vuelta


def conjuncion(valor_a, valor_b):
    # P ^ Q
    if valor_b is valor_a is True:  # si A = B = v entonces es verdadero
        return True
    else:  # si no es verdadero entonves es falso
        return False


def disyuncion_inclusiva(valor_a, valor_b):
    # P v Q
    if (valor_a or valor_b) is True:  # si A o B son verdaderos, entonces es verdadero
        return True
    else:
        return False


def disyuncion_exclusiva(valor_a, valor_b):
    # P w Q
    # literalmente xor
    if (valor_a or valor_b) and not (valor_a and valor_b):
        # si A o B son verdaderos y no tienen el mismo valor son verdaderos
        return True
    else:
        return False


def condicional(valor_a, valor_b):
    # P -> Q
    if negacion(valor_a) or valor_b is True:  # si -A o B son verdaderos, entonces es verdadero
        # -AvB
        # tecnicamente se usa condicional simple
        return True
    else:
        return False


def bicondicional(valor_a, valor_b):
    # P <-> Q
    neg_a = negacion(valor_a)  # creo variables que son lo negativo de A y B
    neg_b = negacion(valor_b)
    if (neg_a or valor_b is True) and (valor_a or neg_b is True):
        # si -A o B son verdaderos y A o -B son verdaderos, entonces es verdadero
        # (-AvB)^(Av-B)
        return True
    else:
        return False
