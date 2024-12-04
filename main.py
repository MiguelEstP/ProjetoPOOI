# Importando as classes do arquivo restaurante.py
from restaurante import Cardapio, Inventario, Cozinheiro, Gerencia, Estatisticas

# Inicializando os objetos necessários
inventario = Inventario(1000, 5, 3, 2)
cardapio = Cardapio()
estatisticas = Estatisticas(inventario)
gerencia = Gerencia("Gerente", "00000000000")
cozinheiro = Cozinheiro("Chef", "11111111111")

# Funções do sistema de interação
def menu_principal():
    print("\n=== Bem-vindo ao Sistema do Restaurante ===")
    print("1. Gerenciar Estoque")
    print("2. Registrar Funcionários")
    print("3. Realizar Pedido")
    print("4. Consultar Estatísticas")
    print("5. Sair")
    return input("Escolha uma opção: ")

def menu_estoque(gerencia):
    while True:
        print("\n=== Gerenciamento de Estoque ===")
        print("1. Verificar Estoque")
        print("2. Atualizar Estoque")
        print("3. Voltar")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            gerencia.verificar_estoque(inventario.mesas)
        elif opcao == "2":
            gerencia.controle_de_estoque(inventario.estoque)
        elif opcao == "3":
            break
        else:
            print("Opção inválida.")

def menu_registrar(estatisticas):
    while True:
        print("\n=== Registro de Funcionários ===")
        print("1. Registrar Cozinheiro")
        print("2. Registrar Garçom")
        print("3. Registrar Gerente")
        print("4. Voltar")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            estatisticas.registrar_cozinheiro()
        elif opcao == "2":
            estatisticas.registrar_garcom()
        elif opcao == "3":
            estatisticas.registrar_gerencia()
        elif opcao == "4":
            break
        else:
            print("Opção inválida.")

def menu_pedidos(cozinheiro, cardapio, inventario):
    while True:
        print("\n=== Realizar Pedido ===")
        print("1. Ver Menu")
        print("2. Fazer Pedido")
        print("3. Voltar")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            print("\nMenu do Restaurante:")
            for i, prato in enumerate(cardapio.pratos, start=1):
                print(f"{i}. {prato.nome} - R$ {prato.preco:.2f}")
        elif opcao == "2":
            numero = int(input("Digite o número do prato desejado: ")) - 1
            if 0 <= numero < len(cardapio.pratos):
                prato = cardapio.pratos[numero]
                cozinheiro.cozinhar(prato, inventario.estoque, inventario.uso_ingredientes, inventario.vendas)
            else:
                print("Número inválido.")
        elif opcao == "3":
            break
        else:
            print("Opção inválida.")

def menu_estatisticas(estatisticas):
    while True:
        print("\n=== Estatísticas ===")
        print("1. Prato Mais Vendido")
        print("2. Ingrediente Mais Usado")
        print("3. Ticket Médio")
        print("4. Voltar")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            estatisticas.prato_mais_vendido()
        elif opcao == "2":
            estatisticas.ingrediente_mais_usado()
        elif opcao == "3":
            estatisticas.ticket_medio(cardapio)  # Passando o objeto cardápio
        elif opcao == "4":
            break
        else:
            print("Opção inválida.")

# Loop principal do sistema
while True:
    opcao = menu_principal()
    if opcao == "1":
        menu_estoque(gerencia)
    elif opcao == "2":
        menu_registrar(estatisticas)
    elif opcao == "3":
        menu_pedidos(cozinheiro, cardapio, inventario)
    elif opcao == "4":
        menu_estatisticas(estatisticas)
    elif opcao == "5":
        print("Saindo do sistema. Até logo!")
        break
    else:
        print("Opção inválida.")
