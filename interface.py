# Importa CustomTkinter
import customtkinter as ctk
# Importa o menu do código da lanchonete
from lanchonete import cadastro, listar, alterar, apagar, pedido_op, busca_cod, cod, prod, val, pedido

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

    alterar_p = ctk.CTkButton(adm, text="Alterar produto", command=alterar)
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

        if produto and valor:
            cadastro(produto, valor)    # Registra o produto no arquivo

            resultado_cadastro.configure(text='Produto cadastrado com sucesso!', text_color='green')
            
            novo_codigo = busca_cod()
            label_cod.configure(text=novo_codigo, font=('Arial', 28, 'bold'))

            entry_produto.delete(0, 'end')
            entry_valor.delete(0, 'end')

            cod.append(novo_codigo)
            prod.append(produto)
            val.append(valor)

        else:
            resultado_cadastro.configure(text='Preencha todos os campos corretamente!', text_color='red')

    # Button
    button_confirma = ctk.CTkButton(cad, text='Confirmar Cadastro', command=confirmar_pedido)
    button_confirma.pack(pady=10)

def abrir_listar():
    lista = ctk.CTkToplevel()
    lista.title("Lista de Produtos")
    lista.geometry('400x500')

    # Mantém a janela em foco
    foco_janela(lista)

    # Label
    label_lista = ctk.CTkLabel(lista, text='LISTA DE PRODUTOS', font=fonte_titulo)
    label_lista.pack(pady=10)

    # Frames
    frame1 = ctk.CTkFrame(lista, width=350, height=400)
    frame1.pack()

    frame2 = ctk.CTkFrame(lista, width=350, height=400)
    frame2.pack()

    # Label tabela
    label_codigo = ctk.CTkLabel(frame1, text='CÓDIGO', font=fonte_titulo)
    label_codigo.grid(column=0, row=0, padx=30, pady=5)

    label_produto = ctk.CTkLabel(frame1, text='PRODUTO', font=fonte_titulo)
    label_produto.grid(column=1, row=0, padx=30, pady=5)

    label_preco = ctk.CTkLabel(frame1, text='VALOR', font=fonte_titulo)
    label_preco.grid(column=2, row=0, padx=30, pady=5)

    
    # Listagem de produtos
    ctk.CTkLabel(frame2, text=cod[0]).grid(column=0, row=0, padx=30, pady=5)
    ctk.CTkLabel(frame2, text=prod[0]).grid(column=1, row=0, padx=30, pady=5)
    ctk.CTkLabel(frame2, text=val[0]).grid(column=2, row=0, padx=30, pady=5)




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
