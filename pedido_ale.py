# me deben 5mil por este programa, si no saben correr python busquen en google un simulador nomas (o googleen)
# cualquier duda del programa avisenme, es imposible que salgan errores a menos que hagan alguna macana
import hashlib


def encriptador(valor):  # el nucleo del programa
    # lo que me dio el chat gpt lol
    hash_obj = hashlib.sha256()
    hash_obj.update(valor.encode('utf-8'))
    return hash_obj.hexdigest()


# ejemplo para mostrar una sola cosa -> print(encriptador("ale gay"))

def bucle_lol():  # cree un bucle para facilitarles la vida, si borran esto les mato
    # lo de aca es todo lo que se muestra en la consola
    while True:
        value = input("Ingrese lo que desea encriptar:\n>>> ")  # registro el valor que escriben en la consola
        print(encriptador(value))  # se muestra el valor encriptado
        print("------")  # para que sea mas pulcro nomas


# si quieren que cuando corra no salga el bucle borren bucle_lol() nomas (lo de abajo, no sean bobos)
bucle_lol()
# ^^^^ LO DE ARRIBA , NO EL COSO QUE DICE DEF
