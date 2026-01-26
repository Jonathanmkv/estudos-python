def calcular_expressao():
    # Solicitar ao usuário que insira uma expressão matématica
    expressao = input("digite uma expressão matemática: ")

    try:
        #avaliar a expressão usando eval
        resultado = eval(expressao)
        print("O resultado da expressão é: ", resultado)
    except Exception as e:
        print("Erro ao avaliar a expressão", e)

# Chamar a função
calcular_expressao()