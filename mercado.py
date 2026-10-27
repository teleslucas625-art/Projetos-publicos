
bd_produtos = []
carrinho = []

def adicionar_produto():
    
    print("--- ADICIONAR PRODUTO ---\n")
    while True:
        produtos = input("Digite o nome do produto: ")
        if produtos.strip() == "":
            print("ERRO: NAO DEIXE OS CAMPOS VAZIOS")
            continue
        break

    while True:
        try:
            valor_produto = int(input("Digite o valor do produto: "))
            quant_produto = int(input("Digite a quantidade em estoque: "))
            
        except ValueError:
            print("ERRO: NAO DEIXE OS CAMPOS VAZIOS")
            continue
        break

    produto = {
        "produto" : produtos,
        "valor" : valor_produto,
        "quantidade" : quant_produto
    }

    bd_produtos.append(produto)

    print("\nPRODUTO ADICIONADO!")
    print("--------------------------------------------\n")

def lista_de_produtos():

    if not bd_produtos:
        print("Nenhum produto em estoque!")

    print("--- LISTA DE PRODUTOS ---\n")

    for produto in bd_produtos:
        print(f"Produto: {produto["produto"]}\nValor: {produto["valor"]}\nEstoque: {produto["quantidade"]}\n")

    print("--------------------------------------------\n")

def relatorio_estoque():

    if not bd_produtos:
        print("Nenhum produto em estoque!")
        print("\n--------------------------------------------\n")
        return

    print("PRODUTOS EM BAIXO ESTOQUE!\n")

    for produto in bd_produtos:
        if int(produto["quantidade"]) < 5:
            print(f"Produto: {produto["produto"]}\nValor: {produto["valor"]}\nEstoque: {produto["quantidade"]}\n")
        

    print("--------------------------------------------\n")

def compras():
    print("--- BEM VINDO AO MERCADO ---\n")
    if not bd_produtos:
            print("Nenhum produto em estoque!\n")
            print("--------------------------------------------\n")
            return
    
    total = 0

    while True:

        print("Essa e a nossa lista de estoque!\n")
        
        for produto in bd_produtos:
            print(f"Produto: {produto["produto"]}\nValor: {produto["valor"]}\nEstoque: {produto["quantidade"]}\n")
        
        compra = input("\nDigite o nome do produto que deseja comprar: ").strip().lower()
        encontrado = False

        for produto in bd_produtos:

            if compra == produto["produto"].strip().lower():
                encontrado = True
                break

        if not encontrado:
            print("PRODUTO NÃO ENCONTRADO!")
            continue

        quantidade = int(input("Digite a quantidade que deseja comprar: "))

        if quantidade > produto["quantidade"] or quantidade < 1:
            print("\nVALOR INVALIDO OU MAIOR QUE O ESTOQUE!")
            continue

        produto["quantidade"] -= quantidade
        
        valor_produtos = int(produto["valor"]) * quantidade 
        print(f"\nPRODUTO: {produto["produto"]} | VALOR: {produto["valor"]} | QUANTIDADE: {quantidade}\n")

        total = total + valor_produtos
        print(f"VALOR TOTAL: {total}\n")

        produto_carrinho = {
            "produto" : compra,
            "valor" : (produto["valor"]),
            "quantidade" : quantidade
            }

        carrinho.append(produto_carrinho)

        continuar = input("Deseja continuar comprando? (S/N): ").strip().lower()

        if continuar != "s":
            break

    while True:

        print("--- SEU CARRINHO ---")
        for produto_carrinho in carrinho:
            print(f"\nPRODUTO: {produto_carrinho["produto"]} | VALOR: {produto["valor"]} | QUANTIDADE: {produto_carrinho["quantidade"]}")
        print(f"\nVALOR TOTAL DA COMPRA: {total}\n")

        print("Compras finalizadas !\n")
        print("--- PAGAMENTO ---")
        print("1 - Debito/Credito")
        print("2 - Pix")
        print("3 - Dinheiro")
        pagamento = input("\nDigite a forma de pagamento: ")

        if pagamento == "1":
            print("\nVenda debito/credito confirmada!")
            print("\n--------------------------------------------\n")
            return
        if pagamento == "2":
            print("\nVenda pix confirmada!")
            print("\n--------------------------------------------\n")
            return
        if pagamento == "3":
            valor_notas = int(input("Digite o valor total das notas: "))
            venda_dinheiro = valor_notas - total

            if venda_dinheiro < 0:
                print("\nDinheiro insuficiente selecione outra forma de pagamento!")
                continue

            elif venda_dinheiro > 0:
                print(f"\nValor troco devolvido: {venda_dinheiro}")
                print("\nVenda dinheiro confirmada!")
                print("\n--------------------------------------------\n")
                return
            else:
                print("\nVenda dinheiro confirmada!")
                print("\n--------------------------------------------\n")
        
while True:

    print("--- MENU MERCADO ---\n")

    print("1- Adicionar produto")
    print("2- Lista de produtos")
    print("3- Relatorio de estoque")
    print("4- Caixa (compras)")
    print("5- Sair\n")

    escolha = input("Digite o que deseja fazer: ")

    if escolha == "1":
        print("\n--------------------------------------------\n")
        adicionar_produto()

    elif escolha == "2":
        print("--------------------------------------------\n")
        lista_de_produtos()

    elif escolha == "3":
        print("--------------------------------------------\n")
        relatorio_estoque()

    elif escolha == "4":
        print("--------------------------------------------\n")
        compras()

    elif escolha == "5":
        print("Voce saiu!")
        break
    
    else:
        print("ERRO: DIGITE UM NUMERO DE 1 A 5!")
        continue