import time

def bucle_calculo():
    resultado = 0
    limite=1000000

    print("Calculando con un bucle simple en Python...")

    inicio=time.time()

    for i in range(limite):
        resultado+=i

    fin=time.time()
    
    print(f"Resultado: {resultado}")
    print(f"Tiempo de ejecucion: {(fin-inicio) *1000:.4f}ms")

bucle_calculo()
