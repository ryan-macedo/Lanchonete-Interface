# Listas globais
continuar_menu = "s"
cod = []             # Lista para armazenar os códigos dos produtos
prod = []            # Lista para armazenar os nomes dos produtos
val = []             # Lista para armazenar os valores dos produtos
cod_alterar = []     # Lista auxiliar para armazenar os códigos válidos para alteração
pedido = []          # Lista usada para armazenar pedidos (não utilizada nesse trecho)
nomes = []           # Lista não utilizada nesse trecho
temp = []            # Lista temporária para análise de códigos
temp_cod = []        # Lista temporária para códigos faltantes
arquivo = open('produtos.txt', 'a+', encoding='utf-8')  # Abre o arquivo de produtos para leitura e escrita

# Função que exibe o menu principal e valida a escolha do usuário
def menu():
    print("\n\n--- MENU ---\n")
    print("1- Administrador\n2- Operador\n0- Sair")

    escolha = input("\nEscolha uma opção:\n")

    # Validação de entrada
    while(escolha == "" or (escolha != "1" and escolha != "2" and escolha != "0")):
        print("\nOpção inválida!")
        escolha = input("\nEscolha uma opção:\n")
    
    return escolha

# Função que exibe o menu do administrador e valida a escolha
def menu_adm():
    print("\n\n--- MENU ADMINISTRADOR ---\n")
    print("1- Cadastrar produto\n2- Listar produto\n3- Alterar produto\n4- Apagar produto\n0- Voltar")

    escolha = input("\nEscolha uma opção:\n")

    # Validação da entrada
    while(escolha == "" or (escolha not in ["1", "2", "3", "4", "0"])):
        print("\nOpção inválida!")
        escolha = input("\nEscolha uma opção:\n")

    return escolha

# Função que busca o próximo código disponível para cadastro
def busca_cod():
    codigo = 0
    
    arquivo = open('produtos.txt', 'r', encoding='utf-8')
    dados = arquivo.readlines()
    arquivo.close()

    if dados == []:
        # Nenhum produto cadastrado, começa com código 100
        codigo = "100"
    else:
        # Extração dos códigos existentes
        for i in range(len(dados)):
            dados[i] = dados[i].strip('\n')
            dados[i] = dados[i].split('|')
            temp.append(dados[i][0])

        # Conversão para inteiros e verificação de códigos faltantes
        for i in range(len(temp)):
            temp[i] = int(temp[i])

        numeros = set(temp)
        esperado = set(range(100, max(numeros) + 1))
        faltantes = sorted(esperado - set(numeros))

        if faltantes == []:
            codigo = str(max(numeros) + 1)
        else:
            # Usa o primeiro código faltante
            for numero in faltantes:
                temp_cod.append(numero)
            codigo = str(temp_cod[0])
            return codigo

    return codigo

# Atualiza as listas globais com os dados atuais do arquivo
def atualizar():
    cod.clear()
    prod.clear()
    val.clear()

    arquivo = open('produtos.txt', 'r', encoding='utf-8')
    linhas = arquivo.readlines()
    arquivo.close()

    # Processa cada linha do arquivo e separa os dados em listas
    for linha in linhas:
        if linha.strip() != "":
            partes = linha.strip().split(" | ")
            if len(partes) == 3:
                cod.append(partes[0])
                prod.append(partes[1])
                val.append(partes[2])

# Função para cadastrar um novo produto
def cadastro():
    codigo = busca_cod()  # Gera novo código
    print("\n\n--- CADASTRO ---\n")

    arquivo = open('produtos.txt', 'a+', encoding='utf-8')

    print(f"\nO código gerado para o novo produto é: {codigo}")
    produto = input("\nDigite o nome do produto:\n")
    while (produto == ""):
        print("Opção inválida!\n")
        produto = input("\nDigite o nome do produto:\n")

    valor = input("\nDigite o valor do produto (R$):\n")
    while (valor == "" or valor.isalpha()):
        print("Opção inválida!\n")
        valor = (input("\nDigite o valor do produto (R$):\n"))

    # Grava o novo produto no arquivo
    arquivo.write(f"{codigo} | {produto} | {valor}\n")
    arquivo.close()

# Função para listar os produtos cadastrados
def listar():
    arquivo = open('produtos.txt', 'r', encoding='utf-8')
    itens = arquivo.read()
    arquivo.close()
    
    print("\n\n--- LISTA DE PRODUTOS ---\n")
    print("CÓDIGO | PRODUTO | VALOR (R$)\n")

    if len(itens) == 0:
        print("Não há nenhum produto cadastrado.")
    else:
        print(itens)

# Função para alterar um produto existente
def alterar():
    atualizar()  # Atualiza as listas com os dados do arquivo

    if len(cod) == 0:
        print("Não há produtos cadastrados para alterar.")
        return

    listar()  # Mostra os produtos disponíveis

    print("\n--- ALTERAR PRODUTOS ---\n")

    cod_alterar.clear()
    for i in range(len(cod)):
        cod_alterar.append(cod[i])

    op_alterar = input("Escolha o código do produto que você deseja alterar:\n")

    # Validação da escolha
    while op_alterar not in cod_alterar:
        op_alterar = input("Escolha um código válido:\n")

    codigo_alterar = cod_alterar.index(op_alterar)

    # Solicita nova descrição
    print(f"\nA descrição atual do produto é: {prod[codigo_alterar]}\n")
    nova_desc = input("Digite a nova descrição do produto:\n")
    while nova_desc == "":
        print("Insira uma descrição válida!\n")
        nova_desc = input("Digite a nova descrição do produto:\n")

    # Solicita novo valor
    print(f"O valor atual do produto é: {val[codigo_alterar]}\n")
    novo_valor = input("Digite o novo valor para o produto: R$\n")
    while novo_valor == "" or novo_valor.isalpha():
        print("Insira um valor válido\n")
        novo_valor = input("Digite o novo valor para o produto: R$\n")

    # Atualiza as listas com os novos dados
    print(f"\nNova descrição do produto cujo o código é {cod_alterar[codigo_alterar]}: {nova_desc}")
    print(f"Novo valor do produto: R${novo_valor}")

    prod[codigo_alterar] = nova_desc
    val[codigo_alterar] = novo_valor

    # Reescreve o arquivo com os dados atualizados
    arquivo = open("produtos.txt", 'w', encoding='utf-8')
    for i in range(len(cod)):
        arquivo.write(cod[i] + " | " + prod[i] + " | " + val[i] + "\n")
    arquivo.close()

# Apagar prod
def apagar():
    
    # Atualiza os dados
    atualizar()
    print("--- APAGAR PRODUTO ---\n")

    # Verifica se há produtos cadastrados
    if len(cod) == 0:
        print("Não há produtos cadastrados.")

        return

    # Mostra os produtos cadastrados
    for i in range(len(cod)):
        print(f"{cod[i]} | {prod[i]} | {val[i]}\n")

    # Solicita o código do produto que o usuário deseja remover
    remover = input("\nDigite o código do produto que deseja remover:\n")

    # Verifica se o produto está na lista de código
    if remover in cod:
        i = cod.index(remover)  # Encontra o índice do produto

        # Remove o código, produto e valor das listas
        cod.pop(i)
        prod.pop(i)
        val.pop(i)

        # Atualiza o arquivo: "produtos.txt"
        arquivo = open("produtos.txt", 'w', encoding="utf-8")
        for j in range(len(cod)):
            arquivo.write(f"{cod[j]} | {prod[j]} | {val[j]}\n")

        print("\nProduto removido com sucesso\n")
    else:
        print("\nCódigo não encontrado\n")


# Pedido operador
def pedido_op():
    
    # Atualiza os dados
    atualizar()
    
    # Inicia um loop
    iniciar_pedido = "s"
    
    # Enquanto o loop estiver ativo, solicita o nome do cliente
    if iniciar_pedido == "s":
        nome_cliente = input("\nDigite o nome do cliente: \n")
        
        # Verifica se o nome do cliente é válido
        while nome_cliente == "" or nome_cliente.isnumeric():
            print("\nDigite o nome corretamente!\n")
            nome_cliente = input("\nDigite o nome do cliente: \n")

        # Adiciona o nome do cliente à lista
        nomes.append(nome_cliente)
        # Lista de itens do pedido
        itens_pedido = []
        # Total do pedido
        total = 0

        # Inicia outro loop
        continuar_pedido = "s"
        while continuar_pedido == "s":
            
            # Lista os produtos
            listar()
            
            # Solicita o código do produto
            pedido_cliente = input("Digite o código do produto desejado:\n")
            
            # Verifica se o código está na lista de códigos
            while pedido_cliente not in cod:
                print("\nDigite um código válido!")
                pedido_cliente = input("Digite o código do produto desejado:\n")

            # Solicita a quantidade
            quantidade = input("\nDigite a quantidade desejada:\n")
            
            # Validação da quantidade
            while quantidade.isalpha():
                print("\nInválido!")
                quantidade = input("\nDigite a quantidade desejada:\n")

            quantidade = int(quantidade) # Converte quantidade para inteiro
            
            # Coleta os dados do pedido
            produto_nome = prod[cod.index(pedido_cliente)]
            produto_valor = float(val[cod.index(pedido_cliente)])
            
            subtotal = quantidade * produto_valor   # Calcula o subtotal
            total += subtotal   # Soma ao total
            
            # Adiciona à lista de itens do pedido
            itens_pedido.append((produto_nome, quantidade, produto_valor, subtotal))

            # Pergunta se o usuário deseja adicionar mais algum produto ao pedido
            continuar_pedido = input("\nDeseja adicionar mais algum produto? s/n: \n").lower()
            
            # Verifica se a entrada do usuário em continuar_pedido é válida
            while continuar_pedido not in ["s", "n"]:
                print("Inválido! Digite uma opção válida")
                continuar_pedido = input("\nDeseja adicionar mais algum produto? s/n: \n").lower()

        # Exibe um resumo do pedido
        print("\n\n--- RESUMO ---\n")
        print(f"Cliente: {nome_cliente}")
        print("Produtos adicionados:")
        for item in itens_pedido:
            print(f"- {item[0]} | Quantidade: {item[1]} | Unitário: R${item[2]:.2f} | Subtotal: R${item[3]:.2f}")
        print(f"\nValor total: R${total:.2f}")

        # Confirmação so pagamento
        confirmar = input("Aperte 'Enter' para confirmar o pagamento ou digite 0 para voltar.\n")
        if confirmar == "":
            print(f"\nCompra concluída com sucesso!")
        else:
            print("\nCompra cancelada.")
            
    # Caso não deseje iniciar o pedido, o loop é encerrado
    else:
        continuar_pedido = "n"


# Loop principal
while(continuar_menu == "s"):
    escolha1 = menu()    # Mostra o menu principal


# Menu do administrador
    if escolha1 == "1":
        continuar_adm = "s"

        while(continuar_adm == "s"):
            escolha_adm = menu_adm()    # Exibe o menu do administrador


            # Cadastro dos produtos
            if escolha_adm == "1":
                continuar_cadastrar = "s"

                while(continuar_cadastrar == "s"):
                    cadastro()  # Entra na função de cadastro
                    
                    continuar_cadastrar = input("\nDeseja cadastrar mais algum produto? (s/n):\n").lower()

                    # Verifica se a entrada do uuário é válida
                    while(continuar_cadastrar not in ["s", "n"]):
                        print("\nInválido! Digite 's' para 'sim' ou 'n' para 'não'.")
                        continuar_cadastrar = input("\nDeseja cadastrar mais algum produto? (s/n):\n").lower()

            # Listar produtos
            elif escolha_adm == "2":
                continuar_listar = "s"

                while(continuar_listar == "s"):
                    listar()    # Entra na função listar produtos

                    voltar = input("Digite '0' para voltar:\n")

                    # Verifica a entrada do usuário
                    while(voltar != "0"):
                        print("\nInválido")
                        voltar = input("Digite '0' para voltar:\n")

                    continuar_listar = "n"
            
            # Alterar produtos 
            elif escolha_adm == "3":
                continuar_alterar = "s"

                while(continuar_alterar == "s"):
                    alterar()   # Entra na função de alterar produtos

                    voltar = input("Digite '0' para voltar:\n")

                    # Verifica a entrada do usuário
                    while(voltar != "0"):
                        print("\nInválido")
                        voltar = input("Digite '0' para voltar:\n")

                    continuar_alterar = "n"

            # Apagar produtos 
            elif escolha_adm == "4":
                continuar_apagar = "s"

                while(continuar_apagar == "s"):
                    apagar()    # Entra na função de apagar produtos

                    voltar = input("Digite '0' para voltar:\n")

                    # Verifica a entrada do usuário
                    while(voltar != "0"):
                        print("\nInválido")
                        voltar = input("Digite '0' para voltar:\n")

                    continuar_apagar = "n"    

            # Voltar ao menu principal
            elif escolha_adm == "0":
                continuar_adm = "n"

    
    # Menu do operador
    elif escolha1 == "2":
        continuar_op = "s"

        while(continuar_op == "s"):
            voltar = input("\nDeseja realizar um novo pedido? s/n \n").lower()
            
            # Verifica a entrada do usuário
            while(voltar not in ["s","n"]):
                print("\nInválido")
                voltar = input("\nDeseja realizar um novo pedido? s/n \n").lower()
                
            if voltar == "s":                
                pedido_op()     # Entra na função do pedido do operador se a entrada for 

            elif voltar == "n":
                continuar_op = "n"  # Se não encerra o loop do operador


    # Encerra o programa
    elif escolha1 == "0":
        print("sair")
        continuar_menu = "n"