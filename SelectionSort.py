# Algoritmos de Selection Sort
import numpy as np

def list_order(lista: list):
    size = len(lista) 
    for j in (range(size-1)):
        idx_min = j
        for i in range(j, size):
            if lista[i] < lista[idx_min]:
                idx_min = i
                
        aux = lista[j]
        lista[j] = lista[idx_min]
        lista[idx_min] = aux
        print(f'Array ordenado após iteração {j+1}: {lista}')
   

if __name__ == "__main__":
    # Testes
    random_list = np.random.randint(0,4200, size = 30).tolist()
    list_7to1 = [ 7, 5, 6, 4, 3, 2, 1]
    list_order(random_list)
    list_order(list_7to1)