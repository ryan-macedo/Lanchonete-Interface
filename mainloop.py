from lanchonete import *

if __name__=="__main__":
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


        # Encerra o programa
        elif escolha1 == "0":
            print("sair")
            continuar_menu = "n"