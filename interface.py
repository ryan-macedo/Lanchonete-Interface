# Importa CustomTkinter
import customtkinter as ctk

# Importa Pillow para imagens/ícones
from PIL import Image

# Importa o menu do código da lanchonete
from lanchonete_app import cadastro, listar, alterar, apagar, pedido_operador, busca_cod, cod, prod, val, atualizar, lista_carrinho, calcular_total

# Imagens
carrinho_icon = ctk.CTkImage(Image.open('icons/carrinho.png'), size=(25, 25))
adicionar_icon = ctk.CTkImage(Image.open('icons/adicionar.png'), size=(25, 25))



# Funções
def foco_janela(janela):
    janela.lift()                       # Traz para frente
    janela.focus_force()                # Foco de teclado
    janela.attributes('-topmost', True) # Fica por cima
    janela.after(100, lambda: janela.attributes('-topmost', False))  # Depois volta ao normal

def abrir_adm():
    adm = ctk.CTkToplevel(root)
    adm.title("Administrador")
    adm.geometry('300x300')

    foco_janela(adm)

    # Label
    label_adm = ctk.CTkLabel(adm, text="ESCOLHA UMA OPÇÃO", font=('Arial', 14, 'bold'))
    label_adm.pack(pady=10)

    # Button
    cadastrar_p = ctk.CTkButton(adm, text="Cadastrar produto", command=abrir_cadastro)
    cadastrar_p.pack(pady=10)

    listar_p = ctk.CTkButton(adm, text="Listar produtos", command=abrir_listar)
    listar_p.pack(pady=10)

    alterar_p = ctk.CTkButton(adm, text="Alterar produto", command=abrir_alterar)
    alterar_p.pack(pady=10)

    apagar_p = ctk.CTkButton(adm, text="Apagar produto", command=abrir_apagar)
    apagar_p.pack(pady=10)

def abrir_cadastro():
    atualizar()

    # Cria uma nova janela
    janela_cad = ctk.CTkToplevel()
    janela_cad.title("Cadastro de produtos")
    janela_cad.geometry('400x550')

    # Mantém a janela em foco
    foco_janela(janela_cad)

    # Chama a função busca_cod()
    codigo = busca_cod()

    # Label
    label_cadastrar = ctk.CTkLabel(janela_cad, text='CADASTRAR PRODUTO', font=('Arial', 14, 'bold'))
    label_cadastrar.pack(pady=10)

    label_cod = ctk.CTkLabel(janela_cad, text=f'O código gerado para o novo produto é:', font=('Arial', 14))
    label_cod.pack(pady=10)

    label_cod = ctk.CTkLabel(janela_cad, text=codigo, font=('Arial', 28, "bold"))
    label_cod.pack(pady=30)

    label_nomeprod = ctk.CTkLabel(janela_cad, text='Digite o nome do produto')
    label_nomeprod.pack(pady=10)

    # Entry
    entry_produto = ctk.CTkEntry(janela_cad, placeholder_text='Produto')
    entry_produto.pack(pady=10)

    # Label
    label_valorprod = ctk.CTkLabel(janela_cad, text='Digite o valor do produto (R$)')
    label_valorprod.pack(pady=10)

    # Entry
    entry_valor = ctk.CTkEntry(janela_cad, placeholder_text='Valor')
    entry_valor.pack(pady=10)

    resultado_cadastro = ctk.CTkLabel(janela_cad, text='')
    resultado_cadastro.pack(pady=10)

    def confirmar_pedido():
        produto = entry_produto.get().strip()
        valor = entry_valor.get().strip()        

        if not produto:
            resultado_cadastro.configure(text='Preencha todos os campos corretamente!', text_color='red')

        elif not valor:
            resultado_cadastro.configure(text='Preencha todos os campos corretamente!', text_color='red')

        elif produto in prod:
            resultado_cadastro.configure(text='Já existe um produto com esse nome!', text_color='red')

        else:
            cadastro(produto, valor)    # Registra o produto no arquivo

            resultado_cadastro.configure(text='Produto cadastrado com sucesso!', text_color='#90EE90')
            
            novo_codigo = busca_cod()
            label_cod.configure(text=novo_codigo, font=('Arial', 28, 'bold'))

            entry_produto.delete(0, 'end')
            entry_valor.delete(0, 'end')

            cod.append(novo_codigo)
            prod.append(produto)
            val.append(valor)

    # Button
    button_confirma = ctk.CTkButton(janela_cad, text='Confirmar Cadastro', command=confirmar_pedido,
        fg_color="#4CAF50",
        hover_color="#337736",
        text_color='white')
    button_confirma.pack(pady=10)

def abrir_listar():
    atualizar()

    janela_lista = ctk.CTkToplevel()
    janela_lista.title("Lista de Produtos")
    janela_lista.geometry('400x300')

    # Mantém a janela em foco
    foco_janela(janela_lista)

    # Label
    label_lista = ctk.CTkLabel(janela_lista, text='LISTA DE PRODUTOS', font=('Arial', 14, 'bold'))
    label_lista.pack(pady=10)

    # Frame tabela
    frame_listar = ctk.CTkScrollableFrame(janela_lista, width=350, height=200)
    frame_listar.pack()

    # Listagem de produtos
    listar(frame_listar)

def abrir_alterar():
    atualizar()

    janela_alterar = ctk.CTkToplevel()
    janela_alterar.title("Alterar Produtos")
    janela_alterar.geometry('400x500')

    # Mantém a janela em foco
    foco_janela(janela_alterar)

    # Label
    ctk.CTkLabel(janela_alterar, text='ALTERAÇÃO DE PRODUTOS', font=('Arial', 14, 'bold')).pack(pady=10)

    # Frames
    frame_alterar = ctk.CTkScrollableFrame(janela_alterar,
        width=350,
        height=100,
        label_text='LISTA DE PRODUTOS'
        )
    frame_alterar.pack()
    
    # Listagem de produtos
    listar(frame_alterar)

    # Label
    label_alterar = ctk.CTkLabel(janela_alterar, text='Digite o código do produto que deseja alterar')
    label_alterar.pack(pady=10)

    # Entry
    entry_alterar = ctk.CTkEntry(janela_alterar, placeholder_text='Código')
    entry_alterar.pack(pady=10)
    
    # Resultado alteração
    resultado_alteracao = ctk.CTkLabel(janela_alterar, text='')
    resultado_alteracao.pack(pady=10)

    def confirmar_alterar():
        codigo = entry_alterar.get().strip()

        if codigo not in cod:
            resultado_alteracao.configure(text='Código não encontrado!', text_color='red')
            return
        
        resultado_alteracao.configure(text='')

        janela_alterar2 = ctk.CTkToplevel()
        janela_alterar2.title("Alterar produtos")
        janela_alterar2.geometry('400x400')

        foco_janela(janela_alterar2)

        # Scrollable Frame
        janela_alterar2 = ctk.CTkScrollableFrame(janela_alterar2,
                orientation='vertical',
                width=300,
                height=400,
                label_text='ALTERAÇÃO DE PRODUTOS',
                corner_radius=10
                )
        
        janela_alterar2.pack(pady=40)

        indice = cod.index(codigo)
        ctk.CTkLabel(janela_alterar2, text=f'Digite a nova descrição do produto:').grid(row=0, column=0, pady=5)
        ctk.CTkLabel(janela_alterar2, text=f'{codigo} - {prod[indice]}', text_color='#FFD700', font=('Arial', 14, 'bold')).grid(row=1, column=0)

        entry_nova_desc = ctk.CTkEntry(janela_alterar2, placeholder_text='Produto')
        entry_nova_desc.grid(row=2, column=0, pady=10)

        ctk.CTkLabel(janela_alterar2, text='Digite o novo valor do produto').grid(row=3, column=0, pady=1)
        entry_novo_valor = ctk.CTkEntry(janela_alterar2, placeholder_text='Valor')
        entry_novo_valor.grid(row=4, column=0, pady=5)

        resultado_alteracao1 = ctk.CTkLabel(janela_alterar2, text='')
        resultado_alteracao1.grid(row=6, column=0, pady=5)

        label_nova_desc = ctk.CTkLabel(janela_alterar2, text='')
        label_nova_desc.grid(row=7, column=0, pady=3)

        resultado_nova_desc = ctk.CTkLabel(janela_alterar2, text='')
        resultado_nova_desc.grid(row=8, column=0, pady=5)

        label_novo_valor = ctk.CTkLabel(janela_alterar2, text='')
        label_novo_valor.grid(row=10, column=0, pady=3)

        resultado_novo_valor = ctk.CTkLabel(janela_alterar2, text='')
        resultado_novo_valor.grid(row=11, column=0, pady=5)

        janela_alterar2.grid_columnconfigure(0, weight=1)

        def aplicar_alteracao():
            nova_desc = entry_nova_desc.get().strip()
            novo_valor = entry_novo_valor.get().strip()

            if not nova_desc or not novo_valor:
                resultado_alteracao1.configure(text='Preencha todos os campos corretamente!', text_color='red')
                return

            else:
                alterar(codigo, nova_desc, novo_valor)
                listar(frame_alterar)

            resultado_alteracao1.configure(text='Produto alterado com sucesso!', text_color='#90EE90')

            label_nova_desc.configure(text=f'Nova descrição do produto cujo código é {codigo}:')
            resultado_nova_desc.configure(text=nova_desc, text_color="#FFD700", font=('Arial', 14, 'bold'))

            label_novo_valor.configure(text=f'O valor atual do produto é:')
            resultado_novo_valor.configure(text=f'R$ {novo_valor}', text_color="#FFD700", font=('Arial', 14, 'bold'))
            
    
        # Botão para confirmar a alteração do produto
        ctk.CTkButton(janela_alterar2, text='Alterar produto', command=aplicar_alteracao,
            fg_color="#2196F3",
            hover_color="#1976D2",
            text_color='white').grid(row=5, column=0, pady=10,)

    # Button
    button_alterar = ctk.CTkButton(janela_alterar, text='Confirmar', command=confirmar_alterar)
    button_alterar.pack(pady=10)
    
def abrir_apagar():
    atualizar()

    # Criação da janela
    janela_apagar = ctk.CTkToplevel()
    janela_apagar.title("Apagar Produtos")
    janela_apagar.geometry('400x500')

    foco_janela(janela_apagar)

    ctk.CTkLabel(janela_apagar, text='APAGAR PRODUTOS', font=('Arial', 14, 'bold')).pack(pady=10)

    # Frames
    frame_apagar = ctk.CTkScrollableFrame(janela_apagar,
        width=350,
        height=100,
        label_text='LISTA DE PRODUTOS'
        )
    frame_apagar.pack()

    
    listar(frame_apagar)

    ctk.CTkLabel(janela_apagar, text='Digite o código do produto que deseja remover:').pack(pady=10)

    entry_apagar = ctk.CTkEntry(janela_apagar, placeholder_text='Código')
    entry_apagar.pack(pady=10)

    resultado_alteracao = ctk.CTkLabel(janela_apagar, text='')
    resultado_alteracao.pack(pady=10)

    def confirmar_apagar():
        # Pega o código do produto que o usuário deseja remover
        cod_remover_prod = entry_apagar.get().strip()
        
        if cod_remover_prod not in cod:
            resultado_alteracao.configure(text='Código não encontrado!', text_color='red')
            return
        
        else:
            apagar(cod_remover_prod)
            listar(frame_apagar)

            resultado_alteracao.configure(text='Produto apagado com sucesso!', text_color='#90EE90')
    
    button_apagar = ctk.CTkButton(janela_apagar, text='Apagar Produto', command=confirmar_apagar,
        fg_color="#F44336",
        hover_color="#D32F2F",
        text_color='white')
    button_apagar.pack(pady=10)





def abrir_operador():
    janela_operador = ctk.CTkToplevel(root)
    janela_operador.title("Operador")
    janela_operador.geometry('300x200')

    # Foco na janela
    foco_janela(janela_operador)

    # Label
    label_op = ctk.CTkLabel(janela_operador, text='Deseja fazer um novo pedido?')
    label_op.pack(pady=10)


    def escolha_sim():
        janela_pedido = ctk.CTkToplevel()
        janela_pedido.title("Pedido")
        janela_pedido.geometry("740x500")

        # Foco janela
        foco_janela(janela_pedido)

        janela_pedido.grid_columnconfigure(0, weight=1)
        janela_pedido.grid_columnconfigure(1, weight=1)
        janela_pedido.grid_rowconfigure(0, weight=1)

        # Frame da tabela de produtos (lado esquerdo)
        frame_lista = ctk.CTkScrollableFrame(janela_pedido,
            width=350,
            height=250,
            label_text='MENU'
        )
        frame_lista.grid(row=0, column=0, pady=10, padx=10, sticky="nsew")

        listar(frame_lista)


        # Frame do cliente (lado direito)
        frame_cliente = ctk.CTkFrame(janela_pedido)
        frame_cliente.grid(row=0, column=1, pady=10, padx=10, sticky="nsew")


        ctk.CTkLabel(frame_cliente, text='CLIENTE:', font=('Arial', 14, 'bold')).grid(row=0, column=2, padx=5, pady=10, sticky='w')

        ctk.CTkLabel(frame_cliente, text='Nome do cliente:', font=('Arial', 14)).grid(row=1, column=1, padx=5, pady=5, sticky='we')

        entry_cliente = ctk.CTkEntry(frame_cliente, placeholder_text='Cliente')
        entry_cliente.grid(row=1, column=2, padx=20, pady=5, sticky='w')

        ctk.CTkLabel(frame_cliente, text='PEDIDO:', font=('Arial', 14, 'bold')).grid(row=2, column=2, padx=5, pady=30, sticky='w')

        ctk.CTkLabel(frame_cliente, text='Código do produto:', font=('Arial', 14)).grid(row=3, column=1, padx=5, pady=5, sticky='we')

        entry_codigo = ctk.CTkEntry(frame_cliente, placeholder_text='Código')
        entry_codigo.grid(row=3, column=2, padx=20, pady=5, sticky='w')

        ctk.CTkLabel(frame_cliente, text='Quantidade:', font=('Arial', 14)).grid(row=4, column=1, padx=5, pady=5, sticky='we')

        entry_qtd = ctk.CTkEntry(frame_cliente, placeholder_text='Quantidade')
        entry_qtd.grid(row=4, column=2, padx=20, pady=5, sticky='w')

        resultado_gravar_pedido = ctk.CTkLabel(frame_cliente, text='')
        resultado_gravar_pedido.grid(row=5, column=1, columnspan=2, padx=5, pady=30)

        ctk.CTkLabel(frame_cliente, text='').grid(row=10, column=0)

        def gravar_pedido():
            cliente = entry_cliente.get().strip().upper()
            codigo = entry_codigo.get().strip()
            quantidade = entry_qtd.get().strip()

            if not cliente or not codigo or not quantidade:
                resultado_gravar_pedido.configure(text='Preencha todos os campos corretamente!', text_color='red')
            
            elif codigo not in cod:
                resultado_gravar_pedido.configure(text='Código não encontrado!', text_color='red')

            else:
                try:
                    quantidade_int = int(quantidade)
                    resultado_gravar_pedido.configure(text='Produto adicionado ao carrinho!', text_color='#90EE90')
                    pedido_operador(cliente, codigo, quantidade_int)
                    
                except ValueError:
                    resultado_gravar_pedido.configure(text="'Quantidade' deve ser um número!", text_color='red')
                
        def carrinho():
            janela_carrinho = ctk.CTkToplevel()
            janela_carrinho.title("Seu Carrinho")
            janela_carrinho.geometry("500x500")
            
            # Foco na janela
            foco_janela(janela_carrinho)

            # Scrollable Frame
            frame_pedido = ctk.CTkScrollableFrame(janela_carrinho,
                label_text='PEDIDO',
                width=450
                )
            frame_pedido.grid(row=0, column=0, padx=15)

            lista_carrinho(frame_pedido)

            frame_pedido2 = ctk.CTkFrame(janela_carrinho)
            frame_pedido2.grid(row=1, column=0, pady=5, padx=20)
            
            label_valor_total = ctk.CTkLabel(frame_pedido2, text=f'Total: R$ {calcular_total()}', font=('Arial', 18, 'underline'))
            label_valor_total.pack()

        ctk.CTkButton(
            frame_cliente, 
            command=gravar_pedido,
            text='Adicionar à lista de pedidos', 
            image=adicionar_icon,
            fg_color="#000000",
            hover_color="#3D3D3D", 
            text_color='white'
        ).grid(row=6, column=1, columnspan=2, padx=5, pady=5, sticky='nsew')

        # Botão do carrinho
        carrinho = ctk.CTkButton(frame_cliente, 
            command=carrinho,
            text='Seu carrinho', 
            image=carrinho_icon,
            fg_color="transparent",
            hover_color="#3D3D3D",
            text_color='white'
            )
        carrinho.grid(row=7, column=1, columnspan=2, padx=5, pady=5, sticky='nsew')

        finalizar_pedido = ctk.CTkButton(frame_cliente,
        text='Finalizar pedido',
        fg_color='#4CAF50',
        hover_color='#337736')
        finalizar_pedido.grid(row=8, column=1, columnspan=2, padx=10, pady=10, sticky='nsew')

    # Button
    button_op = ctk.CTkButton(janela_operador, text='Sim', command=escolha_sim)
    button_op.pack(pady=10)

    button_op = ctk.CTkButton(janela_operador, text='Não')
    button_op.pack(pady=10)



# Janela principal (root)
# Aparência da janela
ctk.set_appearance_mode('dark')

# Criação da janela
root = ctk.CTk()
root.title('Menu')
root.geometry('300x200')

# Label
label_menu = ctk.CTkLabel(root, text='MENU', font=('Arial', 14, 'bold'))
label_menu.pack(pady=10)

# Button
button_adm = ctk.CTkButton(root, text='Administrador', command=abrir_adm)
button_adm.pack(pady=10)

button_op = ctk.CTkButton(root, text="Operador", command=abrir_operador)
button_op.pack(pady=10)

root.mainloop()
