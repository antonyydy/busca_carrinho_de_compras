import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def conversor_real(valor):
    return locale.currency(valor, grouping=True, symbol=None)

opcao = 0
carrinho = []
resultado_global = []

def busca_carrinho():
    with open('produtos - produtos.csv', 'r', encoding='utf8') as produtos:
        next(produtos)
        lista_linhas = produtos.readlines()

    print("===========================================")
    print("Digite sua chave de busca:")
    busca = input("> ").lower()
    print("===========================================")
    print("Resultados:")
    print("Código | Produto | Categoria | Preço")
    
    resultados = []

    for linha in lista_linhas:
        nome, categoria, preco, quantidade, codigo = linha.strip().split(',')
        nome = nome.lower()
        categoria = categoria.lower()

        if busca in nome or busca in categoria or busca == codigo.lower():
            resultados.append((codigo, nome, quantidade, categoria, float(preco)))

    resultados = resultados[:5]

    for produto in resultados:
        preco_formatado = conversor_real(produto[4])
        print(f"{produto[0]} | {produto[1]} | {produto[3]} | {preco_formatado}")
    
    return resultados

def menu_carrinho():
    print("===========================================")
    print('Escolha uma opção:\n 1- Fazer nova busca. \n 2- Adicionar item no carrinho. \n 3- Visualizar os itens no carrinho. \n 4- Finalizar compra.')


def adicionar_carrinho():
    print("Qual produto deseja adicionar: ")
    resultado_selecionado = input()
    print("===========================================")
    for produto in resultado_global:
        if resultado_selecionado == produto[0]:
            carrinho.append(produto)
            print("Produto adicionado com sucesso!")
            

def finalizar_compra():
    print("Carrinho:")
    visualizar_carrinho()
    print("Compra finalizada. Obrigado por comprar conosco!")
    exit()


def visualizar_carrinho():
    print("Itens no carrinho:")
    total = 0
    quant = 0
    print("Código | Produto | Categoria | Preço")
    for prod in carrinho:
        preco_formatado = conversor_real(prod[4])
        print(f"{prod[0]} | {prod[1]} | {prod[3]} | {preco_formatado}")
        total += prod[4]
        quant += 1
          
    print(f"Quantidade de itens: {quant}") 
    print(f"Total do carrinho: {conversor_real(total)}")
        

def finalizar_compra():
    print("Compra finalizada. Obrigado por comprar conosco!")


while opcao != 4:
  menu_carrinho()
  opcao = int(input('Escolha uma opção: '))
  if opcao == 1:
    print("===========================================")
    resultado_global = busca_carrinho()
  elif opcao == 2:
    print("===========================================")
    adicionar_carrinho()
  elif opcao == 3:
    print("===========================================")
    visualizar_carrinho()
  elif opcao == 4:
    print("===========================================")
    finalizar_compra()
  else:
    print("Opção inválida. Por favor, escolha uma opção válida.")
    menu_carrinho()


























