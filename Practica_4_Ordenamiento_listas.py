import random

# ------ Función para ordenar con el metodo de la burbuja


def burbuja(list: list):

    for i in range(len(list)-1, 0, -1):
        for j in range(i):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp

    print(list)


# ------ Función principal
def run():

    list = []
    # --- Llenado de la lista con 15 números aleatorios
    for _ in range(15):
        list.append(random.randrange(0, 15, 1))

    print(list)
    burbuja(list)


if __name__ == "__main__":
    run()
