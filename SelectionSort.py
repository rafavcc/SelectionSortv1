# Algoritmos de Selection Sort
import numpy as np

def insertion_sort(lista: list):
    size = len(lista)

def bubble_sort(lista: list):
    size = len(lista)
    for j in range(size-1):
        for i in range(size-1-j):
            if lista[i] > lista[i+1]:
                aux = lista[i+1]
                lista[i+1] = lista[i]
                lista[i] = aux
    return lista

def selection_sort(lista: list):
    size = len(lista) 
    for j in (range(size-1)):
        idx_min = j
        for i in range(j, size):
            if lista[i] < lista[idx_min]:
                idx_min = i
                
        aux = lista[j]
        lista[j] = lista[idx_min]
        lista[idx_min] = aux
        #print(f'Array ordenado após iteração {j+1}: {lista}')
    return lista
   

if __name__ == "__main__":
    # Testes
    list_1 = [ 7, 5, 6, 4, 3, 2, 1]
    lista_final = bubble_sort(list_1)
    print(f'Lista : {lista_final}')