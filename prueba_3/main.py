# Reto 3
# Respuestas:
# 18 dias habra 1784 peces
# 80  dias habra 380612 peces
# 256 dias habra 12230304 peces
# Paul Vazquez

import time


def calcular_temporizadores(temporizadores_iniciales, dias):
    temporizadores = temporizadores_iniciales.copy()
    total_peces = len(temporizadores)
    nuevos_peces = []

    for dia in range(1, dias+1):
        # print(f"Día {dia}: {temporizadores}")
        for i in range(len(temporizadores)):
            temporizadores[i] -= 1
            if temporizadores[i] == -1:
                if dia >= 2:
                    nuevos_peces.append(8)
                temporizadores[i] = 6

        total_peces += len(nuevos_peces)
        temporizadores.extend(nuevos_peces)
        nuevos_peces = []

    return temporizadores, total_peces


if __name__ == "__main__":
    # Ejemplo de uso
    temporizadores_iniciales = [3,1,4,2,1,1,1,1,1,1,1,4,1,4,1,2,1,1,2,1,3,4,5,1,1,4,1,3,3,1,1,1,1,3,3,1,3,3,1,5, 5,1,1,3,1,1,2,1,1,1,3,1,4,3,2,1,4,3,3,1,1,1,1,5,1,4,1,1,1,4,1,4,4,1,5,1,1,4,5,1, 1,2,1,1,1,4,1,2,1,1,1,1,1,1,5,1,3,1,1,4,4,1,1,5,1,2,1,1,1,1,5,1,3,1,1,1,2,2,1,4, 1,3,1,4,1,2,1,1,1,1,1,3,2,5,4,4,1,3,2,1,4,1,3,1,1,1,2,1,1,5,1,2,1,1,1,2,1,4,3,1, 1,1,4,1,1,1,1,1,2,2,1,1,5,1,1,3,1,2,5,5,1,4,1,1,1,1,1,2,1,1,1,1,4,5,1,1,1,1,1,1, 1,1,1,3,4,4,1,1,4,1,3,4,1,5,4,2,5,1,2,1,1,1,1,1,1,4,3,2,1,1,3,2,5,2,5,5,1,3,1,2, 1,1,1,1,1,1,1,1,1,3,1,1,1,3,1,4,1,4,2,1,3,4,1,1,1,2,3,1,1,1,4,1,2,5,1,2,1,5,1,1, 2,1,2,1,1,1,1,4,3,4,1,5,5,4,1,1,5,2,1,3]
    dias_prueba_1 = 18
    dias_prueba_2 = 80
    # dias_prueba_3 = 256

    start_time = time.time()
    resultado_temporizadores, resultado_total_peces = calcular_temporizadores(temporizadores_iniciales, dias_prueba_1)
    # print("Temporizadores:", resultado_temporizadores)
    print("Total de peces:", resultado_total_peces)
    print("Tiempo de ejecución: %s segundos" % (time.time() - start_time))

    resultado_temporizadores, resultado_total_peces = calcular_temporizadores(temporizadores_iniciales, dias_prueba_2)
    # print("Temporizadores:", resultado_temporizadores)
    print("Total de peces:", resultado_total_peces)
    print("Tiempo de ejecución: %s segundos" % (time.time() - start_time))

    # resultado_temporizadores, resultado_total_peces = calcular_temporizadores(temporizadores_iniciales, dias_prueba_3)
    # print("Temporizadores:", resultado_temporizadores)
    # print("Total de peces:", resultado_total_peces)
