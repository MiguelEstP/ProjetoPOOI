class Cardapio:
    def __init__(self):
        self.pratos = [
            Prato("Bruschetta", ["tomate", "manjericão", "azeite_oliva"], "entrada", 15.00, 10),
            Prato("Salada Caprese", ["mussarela", "tomate", "manjericão"], "entrada", 18.00, 12),
            Prato("Spaghetti ao molho de tomate", ["massa_fresca", "molho_tomate", "manjericão"], "prato principal", 30.00, 20),
            Prato("Lasanha à bolonhesa", ["massa_fresca", "molho_tomate", "queijo_parmesao"], "prato principal", 35.00, 25),
            Prato("Pizza Margherita", ["massa_fresca", "molho_tomate", "queijo_mussarela", "manjericão"], "prato principal", 40.00, 18),
            Prato("Pizza Parma com rúcula", ["massa_fresca", "presunto_parma", "rúcula"], "prato principal", 45.00, 22),
            Prato("Gnocchi ao molho pesto", ["massa_fresca", "pesto"], "prato principal", 32.00, 20),
            Prato("Risoto de tomate seco", ["arroz", "tomate_seco", "queijo_parmesao"], "prato principal", 38.00, 28),
            Prato("Massa com azeite e alho", ["massa_fresca", "azeite_oliva", "alho"], "prato principal", 28.00, 15),
            Prato("Carpaccio de linguiça italiana", ["linguiça_italiana", "rúcula"], "entrada", 20.00, 10)
        ]
        '''self.bebidas = [] - cpa vamos usar'''

class Produto:
   def __init__(self, ingredientes, tipo, preco, tempo):
       self.ingredientes = ingredientes
       self.tipo = tipo
       self.preco = preco
       self.tempo = tempo

class Prato(Produto):
    def __init__(self, nome, ingredientes, tipo, preco, tempo):
        self.nome = nome
        super().__init__(ingredientes, tipo, preco, tempo)

class Bebida(Produto):
    def __init__(self, ingredientes, tipo, preco, tempo):
        super().__init__(ingredientes, tipo, preco, tempo)


class Inventario:
    def __init__(self, dinheiro, x, y, z):
        self.caixa = dinheiro
        self.mesas = {'dois_lugares': x, 'quatro_lugares': y, 'oito_lugares': z}
        self.estoque = {
            "massa_fresca": 30,       # Quantidade de pacotes ou porções
            "molho_tomate": 50,       # Quantidade em unidades
            "azeite_oliva": 20,       # Quantidade em garrafas
            "manjericão": 15,         # Quantidade em maços
            "queijo_parmesao": 10,    # Quantidade em peças ou blocos
            "queijo_mussarela": 25,   # Quantidade em peças ou pacotes
            "presunto_parma": 10,     # Quantidade em pacotes
            "linguiça_italiana": 12,  # Quantidade em pacotes
            "pesto": 8,               # Quantidade em potes
            "farinha_trigo": 20,      # Quantidade em sacos
            "tomate_seco": 18,        # Quantidade em potes
            "vinho_tinto": 15,        # Quantidade em garrafas
            "vinho_branco": 12,       # Quantidade em garrafas
            "alho": 30,               # Quantidade em cabeças
            "rúcula": 10,             # Quantidade em maços
            "azeitonas_pretas": 12,   # Quantidade em unidades
            "azeitonas_verdes": 14,   # Quantidade em unidades
            }
        self.pedidos = []
    
class Pessoa(Inventario):
    def __init__(self, nome, cpf, salario=1412.00):
        self.nome = nome
        self.__cpf = cpf
        self.salario = salario
    
    def verificar_estoque(self):
        print(self.estoque)
    
    def verificar_cpf(self):
        return self.__cpf
    
class Cozinheiro(Pessoa):
    def __init__(self, nome, cpf, salario= 1412, estagiario= True):
        super().__init__(nome, cpf, salario)
        self.estagiario = estagiario
    
    def cozinhar(self, prato, ingredientes):
        for c in self.estoque.keys():
            for j in ingredientes:
                if j == c and c > 0:
                    c -= 1
                else:
                    print('erro')
        print(f'Mamma Mia!! O prato {prato} foi feito com sucesso! HMMMMMM!!!!')
    
    def verificar_estoque(self):
        return super().verificar_estoque()
    
    def verificar_pedidos(self):
        print(self.pedidos)
    
class Garcom(Pessoa):
    def __init__(self, nome, cpf, salario=1412):
        super().__init__(nome, cpf, salario)

    def enviar_pedidos(self, ingredientes, tipo, preco, tempo):
        prato = Prato(ingredientes, tipo, preco, tempo)
        self.pedidos.append(prato)

    def verificar_estoque(self):
        return super().verificar_estoque()
    
class Gerencia(Pessoa):
    def __init__(self, nome, cpf, salario=1412):
        super().__init__(nome, cpf, salario)

    def verificar_estoque(self):
        return super().verificar_estoque()
    
    def controle_de_mesas(self):
        print(self.mesas)
        menu = int(input('''1 - Reduzir mesas de 2 pessoas
              2 - Reduzir mesas de 4
              3 - Reduzir mesas de 8
              4 - Adicionar mesas de 2
              5 - Adicionar mesas de 4
              6 - Adicionar mesas de 8
              7 - Alocar clientes'''))
        if menu == 1:
            self.mesas['dois_lugares'] -= 1
        elif menu == 2:
            self.mesas['quatro_lugares'] -= 1
        elif menu == 3:
            self.mesas['oito_lugares'] -= 1
        elif menu == 4:
            self.mesas['dois_lugares'] += 1
        elif menu == 5:
            self.mesas['quatro_lugares'] += 1
        elif menu == 6:
            self.mesas['oito_lugares'] += 1
        elif menu == 7:
            valor = input('Quantos clientes? ')
            while valor > 0:
                if valor >= 8:
                    self.mesas['oito_lugares'] -= 1
                elif valor >=4:
                    self.mesas['quatro_lugares'] -= 1
                elif valor >=2:
                    self.mesas['dois_lugares'] -= 1
                else:
                    print('error')
        else:
            print('error')
    
    def controle_de_estoque(self):
        print(self.estoque)
        item, valor = input('Digite o item e o novo valor dele: ').split()
        self.estoque[item] = int(valor)
        
class Estatisticas:
    def __init__(self):
        self.cozinheiros = []
        self.garcons = []
        self.gerencia = []
        self.funcionarios = [self.cozinheiros, self.garcons, self.gerencia]
        self.vendas = []

    def registrar_cozinheiro(self):
        nome, cpf, salario, estagiario = input('Digite as informações base: ').split()
        cozinheiro = Cozinheiro(nome, int(cpf), float(salario), estagiario)
        self.cozinheiros.append(cozinheiro)
    
    def registrar_garcom(self):
        nome, cpf, salario = input('Digite as informações base: ').split()
        garcom = Garcom(nome, int(cpf), float(salario))
        self.garcons.append(garcom)
        
    def registrar_gerencia(self):
        nome, cpf, salario = input('Digite as informações base: ').split()
        gerente = Gerencia(nome, int(cpf), float(salario))
        self.gerencia.append(gerente)
    
    def prato_mais_vendido(self):
        return True
    
    def ingrediente_mais_usado(self):
        return True
    
    def ticket_media(self):
        return True
    