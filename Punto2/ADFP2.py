def ADFP2(cadena: str) -> bool:
    letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digitos = "0123456789"

    if not cadena:  
        return False 

    if cadena[0] not in letras:
        return False

    for simbolo in cadena[1:]:
        if simbolo not in letras + digitos:
            return False

    return True


#Pruebas

pruebas=["hola", "X9y8", "Id123", "9start", "ab-cd"]
for cad in pruebas:
    if ADFP2(cad):
        print(f"{cad!r:10} -> ACEPTA")
    else:
        print(f"{cad!r:10} -> NO ACEPTA")
