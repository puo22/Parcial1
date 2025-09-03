def ADFP1(cadena: str) -> bool:

    estado = "q0"
    for simbolo in cadena:
        if estado == "q0":
            if simbolo == "a":
                estado = "q0"
            elif simbolo == "b":
                estado = "q1"
            elif simbolo == "c":
                estado = "q2"
            else:
                return False
        elif estado == "q1":
            if simbolo == "b":
                estado = "q1"
            elif simbolo == "c":
                estado = "q2"
            else:
                return False
        elif estado == "q2":
            if simbolo == "c":
                estado = "q2"
            else:
                return False
    return True

#pruebas
pruebas = ["", "aaa", "bbb", "ccc", "aaabbbccc", "aabb", "bc", "aba", "cac", "cab"]

for cad in pruebas:
    print(f"{cad!r:10} -> {ADFP1(cad)}")

