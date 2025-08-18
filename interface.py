# Importa CustomTkinter
import customtkinter as ctk
# Importa o menu do código da lanchonete
from lanchonete import cadastro, alterar, apagar, pedido_op, busca_cod, cod, prod, val, atualizar

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
    label_adm = ctk.CTkLabel(adm, text="ESCOLHA UMA OPÇÃO", font=fonte_titulo)
    label_adm.pack(pady=10)

    # Button
    cadastrar_p = ctk.CTkButton(adm, text="Cadastrar produto", command=abrir_cadastro)
    cadastrar_p.pack(pady=10)

    listar_p = ctk.CTkButton(adm, text="Listar produtos", command=abrir_listar)
    listar_p.pack(pady=10)

    alterar_p = ctk.CTkButton(adm, text="Alterar produto", command=abrir_alterar)
    alterar_p.pack(pady=10)

    apagar_p = ctk.CTkButton(adm, text="Apagar produto", command=apagar)
    apagar_p.pack(pady=10)

def abrir_cadastro():
    # Cria uma nova janela
    cad = ctk.CTkToplevel()
    cad.title("Cadastro de produtos")
    cad.geometry('400x550')

    # Mantém a janela em foco
    foco_janela(cad)

    # Chama a função busca_cod()
    codigo = busca_cod()

    # Label
    label_cadastrar = ctk.CTkLabel(cad, text='CADASTRAR PRODUTO', font=fonte_titulo)
    label_cadastrar.pack(pady=10)

    label_cod = ctk.CTkLabel(cad, text=f'O código gerado para o novo produto é:', font=('Arial', 14))
    label_cod.pack(pady=10)

    label_cod = ctk.CTkLabel(cad, text=codigo, font=('Arial', 28, "bold"))
    label_cod.pack(pady=30)

    label_nomeprod = ctk.CTkLabel(cad, text='Digite o nome do produto')
    label_nomeprod.pack(pady=10)

    # Entry
    entry_produto = ctk.CTkEntry(cad, placeholder_text='Produto')
    entry_produto.pack(pady=10)

    # Label
    label_valorprod = ctk.CTkLabel(cad, text='Digite o valor do produto (R$)')
    label_valorprod.pack(pady=10)

    # Entry
    entry_valor = ctk.CTkEntry(cad, placeholder_text='Valor')
    entry_valor.pack(pady=10)

    resultado_cadastro = ctk.CTkLabel(cad, text='')
    resultado_cadastro.pack(pady=10)

    def confirmar_pedido():
        produto = entry_produto.get().strip()
        valor = entry_valor.get().strip()        

        if not produto:
            resultado_cadastro.configure(text='Preencha todos os campos corretamente!', text_color='red')

        elif not valor:
            resultado_cadastro.configure(text='Preencha todos os campos corretamente!', text_color='red')

        else:
            cadastro(produto, valor)    # Registra o produto no arquivo

            resultado_cadastro.configure(text='Produto cadastrado com sucesso!', text_color='green')
            
            novo_codigo = busca_cod()
            label_cod.configure(text=novo_codigo, font=('Arial', 28, 'bold'))

            entry_produto.delete(0, 'end')
            entry_valor.delete(0, 'end')

            cod.append(novo_codigo)
            prod.append(produto)
            val.append(valor)

    # Button
    button_confirma = ctk.CTkButton(cad, text='Confirmar Cadastro', command=confirmar_pedido)
    button_confirma.pack(pady=10)

def abrir_listar():
    atualizar()

    lista = ctk.CTkToplevel()
    lista.title("Lista de Produtos")
    lista.geometry('400x300')

    # Mantém a janela em foco
    foco_janela(lista)

    # Label
    label_lista = ctk.CTkLabel(lista, text='LISTA DE PRODUTOS', font=fonte_titulo)
    label_lista.pack(pady=10)

    # Frames
    frame1 = ctk.CTkScrollableFrame(lista, width=350, height=200)
    frame1.pack()

    # Label tabela
    label_codigo = ctk.CTkLabel(frame1, text='CÓDIGO', font=fonte_titulo)
    label_codigo.grid(column=0, row=0, padx=30, pady=5)

    label_produto = ctk.CTkLabel(frame1, text='PRODUTO', font=fonte_titulo)
    label_produto.grid(column=1, row=0, padx=30, pady=5)

    label_preco = ctk.CTkLabel(frame1, text='VALOR', font=fonte_titulo)
    label_preco.grid(column=2, row=0, padx=30, pady=5)

    
    # Listagem de produtos
    if len(cod) == 0:
        ctk.CTkLabel(frame1, text='Não há produtos cadastrados.', font=('Arial', 18, 'underline')).pack()

    else:
        for i in range(len(cod)):
            ctk.CTkLabel(frame1, text=cod[i], font=('Arial', 14, 'bold')).grid(column=0, row=i + 1, padx=40, pady=5)
            ctk.CTkLabel(frame1, text=prod[i], font=('Arial', 14, 'underline')).grid(column=1, row=i + 1, padx=40, pady=5)
            ctk.CTkLabel(frame1, text=f'R$ {val[i]}',font=('Arial', 14, 'bold')).grid(column=2, row=i + 1, padx=40, pady=5)

def abrir_alterar():
    atualizar()

    altera = ctk.CTkToplevel()
    altera.title("Alterar Produtos")
    altera.geometry('400x500')

    # Mantém a janela em foco
    foco_janela(altera)

    # Label
    label_lista = ctk.CTkLabel(altera, text='ALTERAÇÃO DE PRODUTOS', font=fonte_titulo)
    label_lista.pack(pady=10)

    # Frames
    frame1 = ctk.CTkScrollableFrame(altera,
        width=350,
        height=100,
        label_text='LISTA DE PRODUTOS'
        )
    frame1.pack()

    # Label tabela
    label_codigo = ctk.CTkLabel(frame1, text='CÓDIGO', font=fonte_titulo)
    label_codigo.grid(column=0, row=0, padx=30, pady=5)

    label_produto = ctk.CTkLabel(frame1, text='PRODUTO', font=fonte_titulo)
    label_produto.grid(column=1, row=0, padx=30, pady=5)

    label_preco = ctk.CTkLabel(frame1, text='VALOR', font=fonte_titulo)
    label_preco.grid(column=2, row=0, padx=30, pady=5)

    
    # Listagem de produtos
    if len(cod) == 0:
        ctk.CTkLabel(frame1, text='Não há produtos cadastrados.', font=('Arial', 18, 'underline')).pack()

    else:
        for i in range(len(cod)):
            ctk.CTkLabel(frame1, text=cod[i], font=('Arial', 14, 'bold')).grid(column=0, row=i + 1, padx=40, pady=5)
            ctk.CTkLabel(frame1, text=prod[i], font=('Arial', 14, 'underline')).grid(column=1, row=i + 1, padx=40, pady=5)
            ctk.CTkLabel(frame1, text=f'R$ {val[i]}',font=('Arial', 14, 'bold')).grid(column=2, row=i + 1, padx=40, pady=5)


        # Label
        label_alterar = ctk.CTkLabel(altera, text='Digite o código do produto que deseja alterar')
        label_alterar.pack(pady=10)

        # Entry
        entry_alterar = ctk.CTkEntry(altera, placeholder_text='Código')
        entry_alterar.pack(pady=10)
        
        # Resultado alteração
        resultado_alteracao = ctk.CTkLabel(altera, text='')
        resultado_alteracao.pack(pady=10)

        def confirmar_alterar():
            codigo = entry_alterar.get().strip()

            if codigo not in cod:
                resultado_alteracao.configure(text='Digite um código válido!', text_color='red')
                return
            
            resultado_alteracao.configure(text='')

            janela_alterar2 = ctk.CTkToplevel()
            janela_alterar2.title("Alterar produtos")
            janela_alterar2.geometry('400x400')

            foco_janela(janela_alterar2)

            # Scrollable Frame
            scroll_janela2 = ctk.CTkScrollableFrame(janela_alterar2,
                 orientation='vertical',
                 width=300,
                 height=400,
                 label_text='ALTERAÇÃO DE PRODUTOS',
                 corner_radius=10
                 )
            
            scroll_janela2.pack(pady=40)

            ctk.CTkLabel(scroll_janela2, text=f'Digite a nova descrição do produto:\n{codigo}').grid(row=0, column=0, pady=5)

            entry_nova_desc = ctk.CTkEntry(scroll_janela2, placeholder_text='Produto')
            entry_nova_desc.grid(row=1, column=0, pady=10)

            ctk.CTkLabel(scroll_janela2, text='Digite o novo valor do produto').grid(row=2, column=0, pady=5)
            entry_novo_valor = ctk.CTkEntry(scroll_janela2, placeholder_text='Valor')
            entry_novo_valor.grid(row=3, column=0, pady=5)

            resultado_alteracao1 = ctk.CTkLabel(scroll_janela2, text='')
            resultado_alteracao1.grid(row=4, column=0, pady=5)

            label_nova_desc = ctk.CTkLabel(scroll_janela2, text='')
            label_nova_desc.grid(row=6, column=0, pady=3)

            resultado_nova_desc = ctk.CTkLabel(scroll_janela2, text='')
            resultado_nova_desc.grid(row=7, column=0, pady=5)

            label_novo_valor = ctk.CTkLabel(scroll_janela2, text='')
            label_novo_valor.grid(row=8, column=0, pady=3)

            resultado_novo_valor = ctk.CTkLabel(scroll_janela2, text='')
            resultado_novo_valor.grid(row=9, column=0, pady=5)

            scroll_janela2.grid_columnconfigure(0, weight=1)

            def aplicar_alteracao():
                nova_desc = entry_nova_desc.get().strip()
                novo_valor = entry_novo_valor.get().strip()



                if not nova_desc or not novo_valor:
                    resultado_alteracao1.configure(text='Preencha todos os campos corretamente!', text_color='red')
                    return

                else:
                    alterar(codigo, nova_desc, novo_valor)

                resultado_alteracao1.configure(text='Produto alterado com sucesso!', text_color='green')

                label_nova_desc.configure(text=f'Nova descrição do produto cujo código é {codigo}:')
                resultado_nova_desc.configure(text=nova_desc, text_color='yellow')

                label_novo_valor.configure(text=f'O valor atual do produto é:')
                resultado_novo_valor.configure(text=novo_valor, text_color='yellow')
                
        
            # Botão para confirmar a alteração do produto
            ctk.CTkButton(scroll_janela2, text='Alterar produto', command=aplicar_alteracao).grid(row=5, column=0, pady=10)

        # Button
        button_alterar = ctk.CTkButton(altera, text='Confirmar', command=confirmar_alterar)
        button_alterar.pack(pady=10)
        
        

def abrir_op():
    op = ctk.CTkToplevel(root)
    op.title("Operador")
    op.geometry('300x200')

    # Label
    label_op = ctk.CTkLabel(op, text='Deseja fazer um novo pedido?')
    label_op.pack(pady=10)

    # Button
    button_op = ctk.CTkButton(op, text='Sim')
    button_op.pack(pady=10)

    button_op = ctk.CTkButton(op, text='Não')
    button_op.pack(pady=10)

# Aparência da janela
ctk.set_appearance_mode('dark')

# Criação da janela
root = ctk.CTk()
root.title('Menu')
root.geometry('300x200')

# Fonte
fonte_titulo = ctk.CTkFont('Arial', 14, 'bold')


# Label
label_menu = ctk.CTkLabel(root, text='MENU', font=('Arial', 14, 'bold'))
label_menu.pack(pady=10)

# Button
button_adm = ctk.CTkButton(root, text='Administrador', command=abrir_adm)
button_adm.pack(pady=10)

button_op = ctk.CTkButton(root, text="Operador", command=abrir_op)
button_op.pack(pady=10)

root.mainloop()
