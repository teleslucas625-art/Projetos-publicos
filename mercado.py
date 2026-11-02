import bd_mercado

carrinho = []

def adicionar_produto():
    
    print("      ADICIONAR PRODUTO\n")
    while True:
        produto = input("Digite o nome do produto: ")
        if produto.strip() == "":
            print("ERRO: NAO DEIXE OS CAMPOS VAZIOS")
            continue
        break

    while True:
        try:
            valor_produto = float(input("Digite o valor do produto: R$ "))
            quant_produto = int(input("Digite a quantidade em estoque: "))
            break
        except ValueError:
            print("ERRO: DIGITE APENAS NUMEROS!")
            continue
        

    try:
        conn = bd_mercado.bd_mercado()
        if conn is None:
            print("Sem conexao com o banco de dados!")
            return

        cursor = conn.cursor()
        query = "INSERT INTO produtos (produto, valor, quantidade) VALUES (%s, %s, %s)"
        cursor.execute(query, (produto, valor_produto, quant_produto))
        conn.commit()
        cursor.close()
        conn.close()

        print("\nPRODUTO ADICIONADO!")
        print("--------------------------------------------\n")

    except Exception as e:
      print(f"Erro ao salvar no banco: {e}")

def lista_de_produtos():

    try:
        conn = bd_mercado.bd_mercado()
        if conn is None:
            print("Sem conexao com o banco de dados!")
            return
        cursor = conn.cursor()
        cursor.execute("SELECT produto, valor, quantidade FROM produtos")
        produtos = cursor.fetchall()

        if not produtos:
            print("Nenhum produto em estoque!")
            cursor.close()
            conn.close()
            print("--------------------------------------------\n")
            return
        
        print("      LISTA DE PRODUTOS")

        for item in produtos:
            nome = item[0]
            valor = item[1]
            quantidade = item[2]
            print(f"\nProduto: {nome}\nValor: R$ {valor:.2f}\nEstoque: {quantidade}")

        cursor.close()
        conn.close()    
        print("\n--------------------------------------------\n")
    except Exception as e:
        print(f"Erro ao listar os produtos: {e}")

def alterar():
    try:
        conn = bd_mercado.bd_mercado()
        if conn is None:
            print("Sem conexao com o banco de dados!")
            return
        cursor = conn.cursor()
        cursor.execute("SELECT produto, valor, quantidade FROM produtos")
        produtos = cursor.fetchall()
    
        if not produtos:
            print("Nenhum produto em estoque!")
            cursor.close()
            conn.close()
            print("--------------------------------------------\n")
            return

        while True:

            cursor.execute("SELECT produto, valor, quantidade FROM produtos")
            produtos = cursor.fetchall()

            print("      LISTA DE PRODUTOS EM ESTOQUE")
        
            for item in produtos:
                nome = item[0]
                valor = item[1]
                quantidade = item[2]
                print(f"\nProduto: {nome}\nValor: R$ {valor:.2f}\nEstoque: {quantidade}")

            produto_alterar = input("\nDigite o nome do produto que deseja alterar: ")
            encontrado = False

            produto_selecionado = None

            for item in produtos:
                nome = item[0]
                if produto_alterar == nome.strip().lower():
                    encontrado = True
                    produto_selecionado = item
                    break

            if not encontrado:
                print("\nPRODUTO NÃO ENCONTRADO!\n")
                continue

            nome_alterar = produto_selecionado[0]
            valor_alterar = produto_selecionado[1]
            quantidade_alterar = produto_selecionado[2]
    
            print("\nProduto a ser alterado: ")
            print(f"\nProduto: {nome_alterar}\nValor: R$ {valor_alterar}\nEstoque: {quantidade_alterar}\n")

            confirmar3 = input("Deseja alterar esse produto? (S/N): ").strip().lower()
            if confirmar3 != "s":
                print("\nSelecione outro produto!")
                continue

            valor_novo = float(input("\nDigite o novo valor do produto: R$ "))
            quantidade_nova = int(input("Digite a nova quantidade em estoque: "))

            cursor.execute("""
                UPDATE produtos
                SET valor = %s , quantidade = %s
                WHERE produto = %s
                """,(valor_novo,quantidade_nova,nome))
            conn.commit()

            print("\nProduto alterado com sucesso!")

            continuar4 = input("Deseja alterar outro produto? (S/N): ")
            if continuar4 != "s":
                break

        cursor.close()
        conn.close()    
        print("\n--------------------------------------------\n")

    except Exception as e:
        print(f"Erro ao listar os produtos: {e}")

    

def relatorio_estoque():

    try:
        conn = bd_mercado.bd_mercado()
        if conn is None:
            print("Sem conexao com o banco de dados!")
            return
        cursor = conn.cursor()
        cursor.execute("SELECT produto, valor, quantidade FROM produtos")
        produtos = cursor.fetchall()

        if not produtos:
            print("Nenhum produto em estoque!")
            cursor.close()
            conn.close()
            print("\n--------------------------------------------\n")
            return

        print("      PRODUTOS EM BAIXO ESTOQUE!\n")
        tem_baixo_estoque = False

        for item in produtos:
            nome = item[0]
            valor = item[1]
            quantidade = item[2]
            if quantidade < 5:
                tem_baixo_estoque = True
                print(f"Produto: {nome}\nValor: R$ {valor:.2f}\nEstoque: {quantidade}")
                
        if not tem_baixo_estoque:
            print("NENHUM PRODUTO EM BAIXO ESTOQUE!")

        cursor.close()
        conn.close()
        print("\n--------------------------------------------\n")

    except Exception as e:
        print(f"Erro ao listar os produtos em baixo estoque: {e}")
        print("--------------------------------------------\n")

def compras():

    try:
        conn = bd_mercado.bd_mercado()
        if conn is None:
            print("Sem conexao com o banco de dados!")
            return

        cursor = conn.cursor()
        cursor.execute("SELECT produto, valor, quantidade FROM produtos")
        produtos = cursor.fetchall()
        
        print("      BEM VINDO AO MERCADO\n")
        if not produtos:
                print("Nenhum produto em estoque!\n")
                print("--------------------------------------------\n")
                return

        total = 0

        while True:
            cursor.execute("SELECT produto, valor, quantidade FROM produtos")
            produtos = cursor.fetchall()

            print("Essa e a nossa lista de estoque!\n")

            for item in produtos:
                nome_estoque = item[0]
                valor_estoque = item[1]
                quantidade_estoque = item[2]
                print(f"Produto: {nome_estoque}\nValor: R$ {valor_estoque}\nEstoque: {quantidade_estoque}\n")
            
            compra = input("\nDigite o nome do produto que deseja comprar: ").strip().lower()
            encontrado = False

            produto_selecionado = None

            for item in produtos:
                nome_estoque = item[0]
                if compra == nome_estoque.strip().lower():
                    encontrado = True
                    produto_selecionado = item
                    break

            if not encontrado:
                print("\nPRODUTO NÃO ENCONTRADO!\n")
                continue

            quantidade_produto = int(input("Digite a quantidade que deseja comprar: "))

            estoque_validar = produto_selecionado[2]

            if quantidade_produto > estoque_validar or quantidade_produto < 1:
                print("\nVALOR INVALIDO OU MAIOR QUE O ESTOQUE!\n")
                continuar2 = input("Deseja continuar comprando? (S/N): ").strip().lower()
                print(" ")
                if continuar2 != "s":
                    break

                continue

            nome = produto_selecionado[0]
            valor = produto_selecionado[1]
                 
            cursor.execute("""
            UPDATE produtos
            SET quantidade = quantidade - %s
            WHERE produto = %s
            """,(quantidade_produto,nome))
            conn.commit()
            
            valor_produtos = valor * quantidade_produto 
            print(f"\nPRODUTO: {nome} | VALOR: R$ {valor} | QUANTIDADE: {quantidade_produto}\n")

            total = total + valor_produtos
            print(f"VALOR TOTAL: {total}\n")

            produto_comprado = {
                "nome_comprado" : nome,
                "valor_comprado" :  valor,
                "quantidade_comprada" : quantidade_produto
            }
            carrinho.append(produto_comprado)

            continuar = input("Deseja continuar comprando? (S/N): ").strip().lower()

            if continuar != "s":
                break

        while True: 

            if total == 0:
                print("O valor de sua compras e 0!")
                print("Volte sempre!")
                print("\n--------------------------------------------\n")
                break

            print("\n      SEU CARRINHO")
            for produto_comprado in carrinho:
                print(f"\nPRODUTO: {produto_comprado["nome_comprado"]} | VALOR: {produto_comprado["valor_comprado"]} | QUANTIDADE: {produto_comprado["quantidade_comprada"]}")

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
                break
            elif pagamento == "2":
                print("\nVenda pix confirmada!")
                print("\n--------------------------------------------\n")
                break
            
            elif pagamento == "3":
                valor_notas = int(input("Digite o valor total das notas: "))
                venda_dinheiro = valor_notas - total

                if venda_dinheiro < 0:
                    print("\nDinheiro insuficiente selecione outra forma de pagamento!")
                    continue

                elif venda_dinheiro > 0:
                    print(f"\nValor troco devolvido: {venda_dinheiro}")
                    print("\nVenda dinheiro confirmada!")
                    print("\n--------------------------------------------\n")
                    break
                
                else:
                    print("\nVenda dinheiro confirmada!")
                    print("\n--------------------------------------------\n")
                    break
            else:
                print("ERRO: DIGITE UM NUMERO DE 1 A 3!")
                continue

        cursor.close()
        conn.close()

    except Exception as e:
        print(f"Erro ao listar os produtos em baixo estoque: {e}")
        print("--------------------------------------------\n")

while True:

    print("      MENU MERCADO\n")

    print("1- Adicionar produto")
    print("2- Lista de produtos")
    print("3- Alterar valor/estoque")
    print("4- Relatorio de estoque")
    print("5- Caixa (compras)")
    print("6- Sair\n")

    escolha = input("Digite o que deseja fazer: ")

    if escolha == "1":
        print("\n--------------------------------------------\n")
        adicionar_produto()

    elif escolha == "2":
        print("--------------------------------------------\n")
        lista_de_produtos()

    elif escolha == "3":
        print("--------------------------------------------\n")
        alterar()

    elif escolha == "4":
        print("--------------------------------------------\n")
        relatorio_estoque()

    elif escolha == "5":
        print("--------------------------------------------\n")
        compras()

    elif escolha == "6":
        print("Voce saiu!")
        break
    
    else:
        print("ERRO: DIGITE UM NUMERO DE 1 A 5!")
        continue