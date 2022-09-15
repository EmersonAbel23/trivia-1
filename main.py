import time  #importes para el tiempo

iniciar_trivia = True
intento = 0
while iniciar_trivia == True:
    intento += 1
    puntaje = 0
    print(
        "\n BIENVENIDOS A TRIVIA , PONDREMOS A PRUEBA TUS CONOCIMIENTOS. TIENES ",
        f'\033[32m{puntaje} de puntaje\033[39m\n')

    print(f"Intento numero:  {intento}")
    print("Embreve continuamos... ")
    time.sleep(1)
    print("\n '' RESPONDE LAS PREGUNTAS CORECTAS '' \n")
    nombre = str(input("Diguite su nombre: "))
    print(
        f"\n{nombre} Recuerda que cada pregunta vale 10 puntos y cada pregunta incorrecta te restaremos 10 puntos "
    )
    print("Empezemos.")
    time.sleep(1)
    print("\n1)¿Quien es el creador de facebook?")
    print("a)Mark zuckerberg "
          "b)Alan Turing "
          "c)Bill Gates "
          "d)Dennis Ritchie \n")
    validacion = str(input(nombre + " Diguite la respuesta correcta:").lower())
    while validacion not in ("a", "b", "c", "d", "X"):
        validacion = str(
            input("\n " + nombre + " Debes ingresar A, B, C, D\n "
                  "Diguite nuevamente la respuesta correcta: "))
#condiconales de la primera pregunta
    if validacion == "a":
        puntaje += 10
        time.sleep(1)
        print(
            nombre,
            " ->RESPUESTA CORRECTA, EL CREADOR DE FACEBBOK ES MARK ZUCKERBERG<- ganaste",
            ' \033[32m 10 puntos\033[39m')
    elif validacion == "x":
        puntaje += 15
        time.sleep(1)
        print("\nMensaje secreto 🤫🤫 ganaste , \033[33m 15 puntos\033[39m\n")
    else:
        puntaje -= 10
        time.sleep(1)
        print("\nRESPUESTA INCORRECTA :( , SIGUE ESTUDIANDO.  Perdiste",
              '\033[31m 10 puntos\033[39m')
        time.sleep(1)

#pregunta numero 2
    print("\n2)¿Que lenguaje de programacion tiene un bajo nivel?")
    print("a)Python "
          "b)Java "
          "c)Php "
          "d)Elixir \n")

    validacion_2 = str(
        input(nombre + " Diguite la respuesta correcta:").lower())

    while validacion_2 not in ("a", "b", "c", "d", "x"):
        validacion_2 = str(
            input("\n " + nombre + " Debes ingresar A, B, C, D\n "
                  "Diguite nuevamente la respuesta correcta: "))

#condicionales de la segunda pregunta
    if validacion_2 == "a":
        puntaje -= 10
        time.sleep(1)
        print(
            "\nINCORRECTO! ", nombre,
            " Python es un lenguaje de programacion muy alto, SIGUE ESTUDIANDO , Perdiste \033[31m 10 puntos\033[39m\n"
        )
    elif validacion_2 == "b":
        puntaje -= 10
        time.sleep(1)
        print(
            "\nINCORRECTO! ", nombre,
            " JAVA es un lenguaje de programacion muy alto, SIGUE ESTUDIANDO, Perdiste \033[31m 10 puntos\033[39m\n"
        )
    elif validacion_2 == "c":
        puntaje -= 10
        time.sleep(1)
        print(
            "\nINCORRECTO! ", nombre,
            " PHP es un lenguaje de programacion muy alto, SIGUE ESTUDIANDO, Perdiste \033[31m 10 puntos\033[39m\n"
        )
    elif validacion_2 == "x":
        puntaje += 15
        time.sleep(1)
        print("\nMensaje secreto 🤫🤫 GANASTE \033[33m 15 puntos\033[39m ")
    else:
        puntaje += 10
        time.sleep(1)
        print(
            "\nCORRECTO! ", nombre,
            " Elixir es un lenguaje de programacion muy bajo. GANASTE\033[32m 10 puntos\033[39m "
        )

    if puntaje > 0:
        time.sleep(1)
        print("Gracias ", nombre, " por jugar mi trivia ganaste ",
              f'\033[32m {puntaje}\033[39m', " puntos, hasta luego . \n")
    else:
        time.sleep(1)
        print("Gracias ", nombre, " por jugar mi trivia perdiste ",
              f'\033[31m {puntaje}\033[39m', " puntos, hasta luego . \n")

    print("\n¿Deseas intentar la trivia nuevamente?")
    repetir_trivia = input(
        "Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower(
        )

    if repetir_trivia != "si":
        print(f"\nEspero {nombre} que lo hayas pasado bien, hasta pronto!")
        iniciar_trivia = False
