def ler_quantidade(item):
#função para validar a entrada de números inteiros positivos"    
    while True:
        try: 
            entrada = int(input(f"Digite a quantidade de {item} desejados: "))
            if entrada < 0: 
                print("Por favor digite um número positivo")
            else: 
                return entrada
        except ValueError:
            print("Erro: Digite apenas números inteiros ex: 1,2,3")

#variável para acumular o valo total da conta
total_conta = 0.0

#preço unitário dos itens
hamburguer = 10.50
batata_frita = 4.00
refrigerante = 3.00


print("---BEM-VINDO AO RESTAURANTE---")

while True:
    #mostrar as opções do cardápio
    print("\nCARDÁPIO")
    print(f"1- HAMBÚRGUER (R$ {hamburguer: .2f})")
    print(f"2- BATATA FRITA (R$ {batata_frita: .2f})")
    print(f"3- REFRIGERANTE (R$ {refrigerante: .2f})")
    print("0- FECHAR A CONTA (SAIR)")

    #ler a escolha do usuario
    opcao = input("Digite o  número do item desejado: ")

    if opcao == "0":
        break

    elif opcao == "1":
        qtd = ler_quantidade("hambúrgueres")
        valor_item = qtd * hamburguer
        total_conta += valor_item
        print(f"> Adicionado: R$ {valor_item: .2f}")

    elif opcao == "2":
        qtd = ler_quantidade("batatas")
        valor_item = qtd * batata_frita
        total_conta += valor_item
        print(f"> Adicionado: R$ {valor_item: .2f}")

    elif opcao == "3":
        qtd = ler_quantidade("refrigerantes")
        valor_item = qtd * refrigerante
        total_conta += valor_item
        print(f"> Adicionado: R$ {valor_item: .2f}")

    else:
        print("Opção inválida! Escolha 1,2,3 ou 0.")

print("-" * 30)
print(f"PEDIDO FECHADO. Total a pagar: R$ {total_conta: .2f}")




