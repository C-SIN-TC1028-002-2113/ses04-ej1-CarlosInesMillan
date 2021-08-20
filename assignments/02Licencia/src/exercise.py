def main():
    #escribe tu código abajo de esta línea
    num = int(input("Ingresa tu edad: "))
    if 0<num<18:
        print("No cumples requisitos")
    elif num<=0:
        print("Respuesta incorrecta")
    else:
        lic = input("¿Tienes identificación oficial? (s/n): ")
        if lic == "s":
            print("Trámite de licencia concedido")
        elif lic =="n":
            print("No cumples requisitos")
        else:
            print("Respuesta incorrecta")
            


if __name__ == '__main__':
    main()
