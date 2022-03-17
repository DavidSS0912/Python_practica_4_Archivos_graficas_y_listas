# -- Uso de ventanas
from tkinter import *
# -- Ventanas para mostrar mensajes emergentes
from tkinter import messagebox
from typing import ForwardRef, List, Sized
# -- Uso de Gráficas
from matplotlib import pyplot as plt
from numpy import poly1d

ARCHIVO = "data.text"


# ------ Función para encontrar las raices de la función x^2 -12x -9 y guardar las iteraciones en un archivo
def biseccion(xi: float, xs: float, error: float):

    global raiz
    signo = ""
    limite = ""
    xa = (xi + xs)/2.0
    i = 0

    file = open(ARCHIVO, "w")
    file.write('{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^1}'.format(
        'i', 'xi', 'xs', 'xa', 'signo', 'limite', 'error', '\n'))

    while abs(funPolinomica(xa)) > error:
        file.write('{:^10}{:^10.4f}{:^10.4f}{:^10.4f}{:^10}{:^10}{:^10.4f}{:1}'.format(
            i, xi, xs, xa, signo, limite, float(funPolinomica(xa)), '\n'))
        xa = (xi + xs)/2.0
        i = i+1
        if funPolinomica(xi) * funPolinomica(xa) < 0:
            xs = xa
            signo = "Negativo"
            limite = "Superior"
        else:
            xi = xa
            signo = "Positivo"
            limite = "Inferior"

    raiz = xa
    file.write("La raíz es: " + str(raiz))
    file.close()

    messagebox.showinfo(
        message="El programa terminó exitosamente", title=" Resultado")
    graficarFuncion()


# ------ Función polinomica que regresa el valor en y(x)
def funPolinomica(x):
    y = pow(x, 2) - (3*x) - 4
    return (y)


# ------ Función para graficar los datos obtenidos del archivo.
def graficarFuncion():

    # --- Variables tipo list para guardar los datos del archivo
    xXI = []
    xXS = []
    yXI = []
    yXS = []
    arrayFun = []
    arrayX = []
    aux: List

    file = open(ARCHIVO, "r")

    for linea in file:  # --- Se lé una línea completa y se guarda en [linea]
        # --- En [aux] se guarda la línea con los espacios en blanco eliminados y separada por colum
        aux = linea.strip().split()
        if aux[0].isdecimal() and int(aux[0]) > 0:
            xXI.append(aux[1])
            xXS.append(aux[2])

    file.close()

    for i in range(0, len(xXI)):
        yXI.append(funPolinomica(float(xXI[i])))
        arrayX.append(xXI[i])

    xXS.reverse()

    for i in range(0, len(xXI)):
        yXS.append(funPolinomica(float(xXS[i])))
        arrayX.append(xXS[i])

    for i in range(0, len(xXI)):
        arrayFun.append(funPolinomica(float(xXI[i])))

    for i in range(0, len(xXS)):
        arrayFun.append(funPolinomica(float(xXS[i])))

    plt.plot(xXI, yXI, marker="o", color="g")
    plt.plot(xXS, yXS, marker="o", color="r")
    plt.plot(arrayX, arrayFun, marker="_", color="y")
    plt.ylim(-.5, .5)
    plt.title("Metodo biseccion de la funcion y =x^2-3x-4")
    plt.ylabel("Eje Y")
    plt.xlabel("Eje X")
    plt.grid()
    plt.show()


# ------ Función principal
def run():
    # ------ Interface gráfica para solicitar xi, xs y error al usuario
    ventanaBiseccion = Tk()
    ventanaBiseccion.title(
        " Practica 4 Python | Metodo de Bisección y guardar archivo")
    ventanaBiseccion.iconbitmap("logo_py.ico")
    ventanaBiseccion.resizable(0, 0)

    frameBiseccion = Frame(
        ventanaBiseccion, width=600, height=600, bg="white")
    frameBiseccion.pack()

    Label(frameBiseccion, text="Introduce xi: ",
          font=12, bg="white").grid(row=0, column=0, sticky="e", padx=10)

    xiAux = Entry(frameBiseccion, width=50)
    xiAux.grid(row=0, column=1, padx=10, pady=20)

    Label(frameBiseccion, text="Introduce xs: ",
          font=12, bg="white").grid(row=2, column=0, sticky="e", padx=10)

    xsAux = Entry(frameBiseccion, width=50)
    xsAux.grid(row=2, column=1, padx=10, pady=20)

    Label(frameBiseccion, text="Introduce el error: ",
          font=12, bg="white").grid(row=3, column=0, sticky="e", padx=10)

    errorAux = Entry(frameBiseccion, width=50)
    errorAux.grid(row=3, column=1, padx=10, pady=20)

    Button(frameBiseccion, width=20, text="Calcular raices",
           command=lambda: biseccion(float(xiAux.get()), float(xsAux.get()), float(errorAux.get()))).grid(row=4, columnspan=2, padx=10, pady=20)

    ventanaBiseccion.mainloop()


if __name__ == "__main__":
    run()
