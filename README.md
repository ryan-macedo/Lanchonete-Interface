# Interface Gráfica - Lanchonete

> :construction: Projeto em construção :construction:

## 📌 Sobre o projeto
Este projeto foi desenvolvido durante o 1º Semestre de Engenharia de Software na **UMC - Universidade de Mogi das Cruzes** e tem como objetivo simular um sistema de gerenciamento de lanchonete, 
permitindo que o usuário acesse a parte do Administrador e do Operador.

## 💻 Tecnologias utilizadas
- `Python 3`
- `Manipulação de arquivos '.txt'`
- `Estruturas de dados básicas (listas, funções e condicionais)`
- `CustomTkinter (interface gráfica) – em desenvolvimento`

## ⚙️ Funcionalidades

<img src="https://github.com/user-attachments/assets/02563cca-88d0-4475-bd5a-8301e2feb29e" width=700 alt="Interface">

### 👨‍💼 Administrador:

***1. Cadastrar produto***  
  * Código do produto é gerado automaticamente
  * Solicitação do nome do produto
  * Solicitação do valor do produto em reais(R$)
  * Produto adicionado ao arquivo `'produtos.txt'`

***2. Listar produto***
   * Lê o arquivo `'produtos.txt'`
   * Lista todos os produtos que estiverem cadastrados  
     
***3. Alterar produto***
   * Exibe os produtos cadastrados
   * Solicita código, nova descrição e novo valor do produto
   * Atualiza o arquivo `'produtos.txt'`
     
***4. Apagar produto***
   * Exibe os produtos cadastrados
   * Solicita o código do produto que será removido
   * Apaga o produto do arquivo `'produtos.txt'`

---

### 🛒 Operador:

***1. Realizar pedido***
* Solicita o nome do cliente que está fazendo o pedido
* Exibe os produtos cadastrados no arquivo
* Solicita o código do produto desejado e a quantidade
* Permite adicionar vários produtos
* Exibe um resumo do pedido

## ▶️ Como executar o projeto
1. Instale o [Python 3](https://www.python.org/downloads/)
2. Instale a biblioteca [CustomTKinter](https://customtkinter.tomschimansky.com/documentation/) utilizando o seguinte comando no terminal:
```
pip install customtkinter
```
3. Clone este repositório:
```
git clone https://github.com/ryan-macedo/Lanchonete.git
```
4. Execute o arquivo principal:
```
python interface.py
```
