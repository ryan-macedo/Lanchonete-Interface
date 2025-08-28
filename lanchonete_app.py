import customtkinter as ctk


# Listas globais
continuar_menu = "s"
cod = []             # Lista para armazenar os códigos dos produtos
prod = []            # Lista para armazenar os nomes dos produtos
val = []             # Lista para armazenar os valores dos produtos
cod_alterar = []     # Lista auxiliar para armazenar os códigos válidos para alteração
pedido = [cod, prod, val]          # Lista usada para armazenar pedidos (não utilizada nesse trecho)
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
    print("1- Cadastrar produto\n2- Listar produtos\n3- Alterar produto\n4- Apagar produto\n0- Voltar")

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
            dados[i] = dados[i].split(';')
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
            partes = linha.strip().split(";")
            if len(partes) == 3:
                cod.append(partes[0])
                prod.append(partes[1])
                val.append(partes[2])

# Função para cadastrar um novo produto
def cadastro(produto, valor):
    codigo = busca_cod()  # Gera novo código

    arquivo = open('produtos.txt', 'a+', encoding='utf-8')

    # Grava o novo produto no arquivo
    arquivo.write(f"{codigo};{produto};{valor}\n")
    arquivo.close()

    return codigo

# Função para listar os produtos cadastrados
def listar(frame_destino):
    for widget in frame_destino.winfo_children():
        widget.destroy()

    atualizar()

    # Label tabela
    label_codigo = ctk.CTkLabel(frame_destino, text='CÓDIGO', font=('Arial', 14, 'bold'))
    label_codigo.grid(column=0, row=0, padx=30, pady=5)

    label_produto = ctk.CTkLabel(frame_destino, text='PRODUTO', font=('Arial', 14, 'bold'))
    label_produto.grid(column=1, row=0, padx=30, pady=5)

    label_preco = ctk.CTkLabel(frame_destino, text='VALOR', font=('Arial', 14, 'bold'))
    label_preco.grid(column=2, row=0, padx=30, pady=5)

    # Listagem de produtos
    if len(cod) == 0:
        ctk.CTkLabel(frame_destino, text='Não há produtos cadastrados.', text_color="#FFD700", font=('Arial', 14, 'underline')).grid(
            row=3, column=0, columnspan=3, pady=5
            )

    else:
        for i in range(len(cod)):
            ctk.CTkLabel(frame_destino, text=cod[i], font=('Arial', 14, 'bold')).grid(column=0, row=i + 1, pady=5, sticky='we')
            ctk.CTkLabel(frame_destino, text=prod[i], font=('Arial', 14, 'underline')).grid(column=1, row=i + 1, pady=5, sticky='we')
            ctk.CTkLabel(frame_destino, text=f'R$ {val[i]}',font=('Arial', 14, 'bold')).grid(column=2, row=i + 1, pady=5, sticky='we')

    

# Função para alterar um produto existente
def alterar(codigo, nova_desc, novo_valor):
    if codigo in cod:
        i = cod.index(codigo)
        prod[i] = nova_desc
        val[i] = novo_valor

    # Reescreve o arquivo com os dados atualizados
    arquivo = open("produtos.txt", 'w', encoding='utf-8')
    for i in range(len(cod)):
        arquivo.write(cod[i] + ";" + prod[i] + ";" + val[i] + "\n")
    arquivo.close()

    atualizar()

# Apagar prod
def apagar(entry_codigo):
    if entry_codigo in cod:
        i = cod.index(entry_codigo)
        cod.pop(i)
        prod.pop(i)
        val.pop(i)

        # Reescreve o arquivo já sem o item e garante flush/close
        with open("produtos.txt", "w", encoding="utf-8") as f:
            for j in range(len(cod)):
                f.write(f"{cod[j]};{prod[j]};{val[j]}\n")

        # Agora sim, recarrega a lista a partir do arquivo já salvo
        atualizar()

# Pedido operador
def pedido_operador(cliente, codigo, quantidade):
    
    # Atualiza os dados
    atualizar()

    # Adiciona o nome do cliente à lista
    nomes.append(cliente)
    # Lista de itens do pedido
    itens_pedido = []
    # Total do pedido
    total = 0

    # Coleta os dados do pedido
    produto_nome = prod[cod.index(codigo)]
    produto_valor = float(val[cod.index(codigo)])
    
    subtotal = quantidade * produto_valor   # Calcula o subtotal
    total += subtotal   # Soma ao total
    
    # Adiciona à lista de itens do pedido
    itens_pedido.append((produto_nome, quantidade, produto_valor, subtotal))
