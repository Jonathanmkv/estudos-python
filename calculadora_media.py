# Entrada de dados
nota1 = float(input("Digite a primeira nota: ")) 
nota2 = float(input("Digite a segunda nota: "))
#Validação dos dados de entrada
if (nota1 <0 or nota1 >10) or (nota2 <0 or nota2>10):
    print("Erro: As notas devem ser entre 0 a 10!")
else:
# Calculando a média
    media = (nota1 + nota2) / 2
    # Imprimindo o resultado 
    print("A média das notas é:", media)
    # Verificando se o aluno está aprovado
    if media <6:
        print("Aluno reprovado!")
    else: print("Aluno aprovado!")