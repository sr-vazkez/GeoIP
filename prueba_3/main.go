package main

import (
	"fmt"
	"time"
)

func calcularTemporizadores(temporizadoresIniciales []int, dias int) (int) {
	temporizadores := make([]int, len(temporizadoresIniciales))
	copy(temporizadores, temporizadoresIniciales)
	totalPeces := len(temporizadores)
	nuevosPeces := []int{}

	for dia := 1; dia <= dias; dia++ {
		for i := 0; i < len(temporizadores); i++ {
			temporizadores[i]--
			if temporizadores[i] == -1 {
				if dia >= 2 {
					nuevosPeces = append(nuevosPeces, 8)
				}
				temporizadores[i] = 6
			}
		}

		totalPeces += len(nuevosPeces)
		temporizadores = append(temporizadores, nuevosPeces...)
		nuevosPeces = []int{}
	}

	return totalPeces
}

func main() {
	temporizadoresIniciales := []int{3,1,4,2,1,1,1,1,1,1,1,4,1,4,1,2,1,1,2,1,3,4,5,1,1,4,1,3,3,1,1,1,1,3,3,1,3,3,1,5, 5,1,1,3,1,1,2,1,1,1,3,1,4,3,2,1,4,3,3,1,1,1,1,5,1,4,1,1,1,4,1,4,4,1,5,1,1,4,5,1, 1,2,1,1,1,4,1,2,1,1,1,1,1,1,5,1,3,1,1,4,4,1,1,5,1,2,1,1,1,1,5,1,3,1,1,1,2,2,1,4, 1,3,1,4,1,2,1,1,1,1,1,3,2,5,4,4,1,3,2,1,4,1,3,1,1,1,2,1,1,5,1,2,1,1,1,2,1,4,3,1, 1,1,4,1,1,1,1,1,2,2,1,1,5,1,1,3,1,2,5,5,1,4,1,1,1,1,1,2,1,1,1,1,4,5,1,1,1,1,1,1, 1,1,1,3,4,4,1,1,4,1,3,4,1,5,4,2,5,1,2,1,1,1,1,1,1,4,3,2,1,1,3,2,5,2,5,5,1,3,1,2, 1,1,1,1,1,1,1,1,1,3,1,1,1,3,1,4,1,4,2,1,3,4,1,1,1,2,3,1,1,1,4,1,2,5,1,2,1,5,1,1, 2,1,2,1,1,1,1,4,3,4,1,5,5,4,1,1,5,2,1,3}
	diasPrueba3 := 256

	resultadoTotalPeces := calcularTemporizadores(temporizadoresIniciales, diasPrueba3)
	fmt.Println("Total de peces:", resultadoTotalPeces)

	startTime := time.Now()
	fmt.Printf("Tiempo de ejecución: %s segundos\n", time.Since(startTime))
}
