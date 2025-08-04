# Importa CustomTkinter
import customtkinter as ctk
# Importa o menu do código da lanchonete
from lanchonete import cadastro, listar, alterar, apagar, pedido_op, busca_cod



# Funções
def foco_janela(janela):
    janela.lift()                       # Traz para frente
    janela.focus_force()                # Foco de teclado
    janela.attributes('-topmost', True) # Fica por cima
    janela.after(100, lambda: janela.attributes('-topmost', False))  # Depois volta ao normal

def abrir_adm():
    adm = ctk.CTkToplevel(app)
    adm.title("Administrador")
    adm.geometry('300x300')

    foco_janela(adm)

    # Label
    label_adm = ctk.CTkLabel(adm, text="ESCOLHA UMA OPÇÃO")
    label_adm.pack(pady=10)

    # Button
    cadastrar_p = ctk.CTkButton(adm, text="Cadastrar produto", command=abrir_cadastro)
    cadastrar_p.pack(pady=10)

    listar_p = ctk.CTkButton(adm, text="Listar produtos", command=listar)
    listar_p.pack(pady=10)

    alterar_p = ctk.CTkButton(adm, text="Alterar produto", command=alterar)
    alterar_p.pack(pady=10)

    apagar_p = ctk.CTkButton(adm, text="Apagar produto", command=apagar)
    apagar_p.pack(pady=10)

def abrir_cadastro():
    # Cria uma nova janela
    cad = ctk.CTkToplevel()
    cad.title("Cadastro de produtos")
    cad.geometry('400x500')

    # Mantém a janela em foco
    foco_janela(cad)

    # Chama a função busca_cod()
    codigo = busca_cod()

    # Label
    label_cadastrar = ctk.CTkLabel(cad, text='CADASTRAR PRODUTO')
    label_cadastrar.pack(pady=10)

    label_cod = ctk.CTkLabel(cad, text=f'O código gerado para o novo produto é:\n\n{codigo}')
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
            label_cod.configure(text=f'O código gerado para o novo produto é:\n\n{novo_codigo}')

            entry_produto.delete(0, 'end')
            entry_valor.delete(0, 'end')

            

        else:
            resultado_cadastro.configure(text='Preencha todos os campos corretamente!', text_color='red')

    # Button
    button_confirma = ctk.CTkButton(cad, text='Confirmar Cadastro', command=confirmar_pedido)
    button_confirma.pack(pady=10)


def abrir_op():
    op = ctk.CTkToplevel(app)
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
app = ctk.CTk()
app.title('MENU')
app.geometry('300x200')


# Label
label_menu = ctk.CTkLabel(app, text='MENU')
label_menu.pack(pady=10)

# Button
button_adm = ctk.CTkButton(app, text='Administrador', command=abrir_adm)
button_adm.pack(pady=10)

button_op = ctk.CTkButton(app, text="Operador", command=abrir_op)
button_op.pack(pady=10)

app.mainloop()
