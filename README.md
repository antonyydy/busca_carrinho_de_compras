  <h1 align="center"> Busca e Carrinho de Produtos </h1>
  
  
  <p align="center">
    <a href="#-tecnologias">Tecnologias</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
    <a href="#-projeto">Projeto</a>&nbsp;&nbsp;&nbsp;
  
  
  ## 💻 Projeto

  Neste trabalho, você deverá criar um programa que possibilite o usuário de fazer buscas por um catálogo de produtos. O usuário deve conseguir montar um carrinho e ao sinalizar que terminou de buscar por produtos, seu programa deve mostrar quais produtos estão no carrinho e o total das compras realizadas por ele.

Para ajudar a resolver o trabalho, seguem algumas orientações e passo a passos:

1. Aqui, em anexo, existe um arquivo .CSV que deverá servir como base de dados para o seu programa. Isso quer dizer que as buscas realizadas pelo usuário devem sempre procurar as informações dos produtos nesse arquivo e exibir na tela de acordo com o que está registrado no arquivo. O formato que as informações serão exibidas na tela é indiferente, contanto que as informações sejam exatamente as mesmas do arquivo de base de dados e sempre seja exibido o código, nome e preço do produto.
2. A primeira coisa a se fazer é implementar a busca, onde o usuário do seu programa poderá digitar na barra de busca o nome do produto OU o código do produto OU a categoria do produto. O resultado da busca deverá ser uma lista com no máximo 5 produtos correspondentes à busca do usuário, não tem problema se essa lista de correspondência tiver menos itens do que 5. Abaixo, um exemplo de como essa busca deve ser exibida para o usuário:
------------------------------------------------
Digite sua chave de busca: <br>
> jeans <br>
Resultados: <br>
Código | Produto | Preço <br>
PROD100005   Jaqueta Jeans Feminina   161.01 <br>
PROD100025   Jaqueta Jeans Feminina   80.34 <br>
PROD100035   Jaqueta Jeans Feminina   92.32
--------------------------------------------------
3. Ao final de cada busca, o usuário deve poder escolher entre: Fazer uma nova busca; Adicionar item no carrinho; Visualizar os itens no carrinho; Finalizar a compra. Essas opções só podem ser exibidas ao usuário depois que ele tiver inserido pelo menos um item no carrinho, se não houver itens no carrinho, as únicas opções disponíveis devem ser: Fazer uma nova busca, Adicionar item no carrinho e Finalizar a compra.
4. Para adicionar um item no carrinho, o usuário deverá fornecer o código do produto apenas e baseado nesse código, todas as outras informações devem ser acrescentadas ao carrinho, abaixo um exemplo de como deve ocorrer essa operação
-------------------------------------------------
Digite o código do produto que deseja adicionar ao carrinho:
> PROD100025
Produto adicionado ao carrinho!
-------------------------------------------------
5. Ao selecionar a opção de visualizar o carrinho, deve ser exibido para o usuário todos os produtos que ele já adicionou ao carrinho anteriormente com as informações de código do produto, nome, categoria e preço. Ao final da exibição de todos os elementos deve ser exibida a quantidade total de produtos e o preço total dos itens, como no exemplo abaixo:
--------------------------------------------------------------
Carrinho: <br>
Código | Produto | Preço  <br>
PROD100005   Jaqueta Jeans Feminina   34.00  <br>
PROD100025   Blusa Feminina   10.43  <br>
PROD100035   Calça Jeans Feminina   56.00  <br>
Quantidade de itens: 3  <br>
Total do carrinho: 100.43  <br>

--------------------------------------------------------------

6. Ao selecionar a opção de finalizar a compra, o carrinho deve ser exibido para o usuário e o programa deverá finalizar.

Informações importantes:
- O arquivo .csv não pode ser alterado em momento algum, o arquivo utilizada para a correção do trabalho será diferente deste, seguindo apenas o mesmo formato e estrutura.
- O usuário pode adicionar o mesmo produto no carrinho mais de uma vez sem problemas, você podem exibir da forma que acharem melhor essa quantidade de produtos, podendo apenas repetir os itens na lista se quiserem.

EXTRA: Na exibição para a tela, mostrar todos os valores no formato de reais "R$ 00,00"<br>
EXTRA: Adicionar opção de remover do carrinho
  
  ## 🚀 Tecnologias
  
  Esse projeto foi desenvolvido com as seguintes tecnologias:
  
  - Python 
  - Git e Github
