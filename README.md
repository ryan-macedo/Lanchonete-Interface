# Lanchonete
## 📌 Sobre o projeto
Este projeto foi desenvolvido durante o 1º Semestre de Engenharia de Software na **UMC - Universidade de Mogi das Cruzes** e tem como objetivo simular um sistema de gerenciamento de lanchonete, 
permitindo que o usuário acesse a parte do Administrador e do Operador.

## 💻 Tecnologias utilizadas
- `Python 3`
- `Manipulação de arquivos '.txt'`
- `Estruturas de dados básicas (listas, loops, funções e condicionais)`



## ⚙️ Funcionalidades
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
   * Solicita o código do produto que será alterado
   * Solicita a nova descrição do produto
   * Solicita o novo valor do produto
   * Atualiza o arquivo `'produtos.txt'`
     
***4. Apagar produto***
   * Exibe os produtos cadastrados
   * Solicita o código do produto que será removido
   * Apaga o produto do arquivo `'produtos.txt'`

---

### 🛒 Operador:

***1. Realizar pedido***
* Questiona se o usuário deseja realizar um pedido
* Solicita o nome do cliente que está fazendo o pedido
* Exibe os produtos cadastrados no arquivo
* Solicita o código do produto desejado
* Solicita a quantidade
* Questiona se o usuário deseja adicionar mais algum produto
* Exibe um resumo do pedido

## ▶️ Como executar o projeto
1. Instale o [Python 3](https://www.python.org/downloads/)
2. Clone este repositório:
```
git clone https://github.com/ryan-macedo/Lanchonete.git
```
