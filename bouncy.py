def bouncy(numero):
    crescente, decrescente = False, False
    direito = numero % 10
    numero = numero // 10

    while numero > 0:
        esquerdo = numero % 10
        if esquerdo < direito:
            crescente = True
        elif esquerdo > direito:
            decrescente = True
        direito = esquerdo
        numero = numero // 10
        if crescente and decrescente:
            return True
    return False

computo = 0
ultimo = 99
while computo < 0.99 * ultimo:
    ultimo = ultimo + 1
    if bouncy(ultimo):
        computo = computo + 1
        print("Bouncy = ", ultimo)