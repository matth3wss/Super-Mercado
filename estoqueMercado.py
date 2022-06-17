#criação da classe que define os atributos dos produtos
class mercadoria:
  nomeMercadoria=''
  precoMercadoria=0.0
  codigoMercadoria=0
  quantidadeEstoque=0

class compras:
  nomeProduto=''
  precoProduto=0.0
  codigoProduto=0
  quantidadeProduto=0
  total=0.0

#escolha das ações a serem realizadas pelo operador do caixa
def menu():
  print('Escolha o número da ação que deseja executar: ')
  print("(1) Cadastrar Novo Produto")
  print("(2) Atualizar Produto")
  print("(3) Realizar Compra")
  print("(4) Consultar Informações de um Produto")
  print("(5) Listar Produtos Cadastrados")
  print("(0) Sair do Programa")
  op=int(input())
  return op

#1º Cadastro de novos produtos no sistema do mercado
def cadastroMercadoria(codigoMercadoria):
  produto=mercadoria()
  produto.nomeMercadoria=input("Nome do Produto: ")
  produto.precoMercadoria=float(input("Preço do Produto: "))
  produto.codigoMercadoria=codigoMercadoria
  produto.quantidadeEstoque=int(input("Quantidade em Estoque: "))
  return produto

# 2º Atualizar Produto
def atualizarMercadoria(arrayEstoque):
  existe=0
  id=int(input("Digite o código do produto: "))
  for i in range(len(mercado)):
    if id == arrayEstoque[i].codigoMercadoria:
      existe = 1
      print("O que deseja atualizar?")
      print("(1) Quantidade em estoque.")
      print("(2) Preço do produto.")
      print("(-1) Sair.")
      op=int(input())
    
      if op == 1:
        print(f"Quantidade atual: {arrayEstoque[i].quantidadeEstoque}")
        arrayEstoque[i].quantidadeEstoque=int(input("Nova quantidade:"))
        break 

      elif op == 2:
        print(f"Preço atual: {arrayEstoque[i].precoMercadoria}")
        arrayEstoque[i].precoMercadoria=float(input("Novo preço:"))
        break
        
      elif op == -1:
        break
        
      else:
        print("Opção invalida")
        atualizarMercadoria(arrayEstoque)
        
  if existe == 0:
    print("Produto não cadastrado")

# 3 Compras
class caixa:
  # 3.1 Realiza a venda dos produtos e retorna o vetor que imprimira o recibo
  def realizarCompra(arrayEstoque, codigo):
    recibo=compras()
    for i in range(len(arrayEstoque)):
      if codigo==arrayEstoque[i].codigoMercadoria:
        print(f"Nome do produto:{arrayEstoque[i].nomeMercadoria}")
        
        quantidade=int(input("Quantidade de itens desejados: "))
        if quantidade > arrayEstoque[i].quantidadeEstoque:
          print("Quantia maior que o estoque.")
        else:
          arrayEstoque[i].quantidadeEstoque-=quantidade
          recibo.nomeProduto=arrayEstoque[i].nomeMercadoria
          recibo.precoProduto=arrayEstoque[i].precoMercadoria
          recibo.codigoProduto=arrayEstoque[i].codigoMercadoria
          recibo.quantidadeProduto=quantidade
          recibo.total=arrayEstoque[i].precoMercadoria*quantidade
          print("Item confirmado")
          return recibo
          
  # 3.2 Inicia o função que registra as vendas
  def iniciarCompra(arrayEstoque):
    recibo=[]
    print("Digite -1 no código do produto para finalizar a compra")

    while True:
      codigo=int(input("Código do Produto: "))
      if codigo!=-1:
        existe=0
        for i in range(len(arrayEstoque)):
          if codigo == arrayEstoque[i].codigoMercadoria:
            existe = 1
            novaCompra=caixa.realizarCompra(arrayEstoque, codigo)
            recibo.append(novaCompra)
            break
        if existe==0:
          print("Produto não Cadastrado!\n")
      else:
        print("Compra Finalizada!")
        break

    # 3.3 Realiza a impressão do recibo
    a=compras()
    total=0
    print("|  Código Produto  |  Nome do Produto  | Quantidade | Preço Unitário |  Total  |")
    print("|==============================================================================|") 
    for i in range(len(recibo)):
      a.codigoProduto=(str(recibo[i].codigoProduto)).center(18)
      a.nomeProduto=(recibo[i].nomeProduto).center(19)
      a.quantidadeProduto=(str(recibo[i].quantidadeProduto)).center(12)
      a.precoProduto=("R${:,.2f}".format(recibo[i].precoProduto).center(16))
      a.total=("R${:,.2f}".format(recibo[i].total).center(9))
      total+=(recibo[i].precoProduto*recibo[i].quantidadeProduto)

      print(f"|{a.codigoProduto}|{a.nomeProduto}|{a.quantidadeProduto}|{a.precoProduto}|{a.total}|")
    total=("R${:,.2f}".format(total)).center(8)
    print("|==============================================================================|")
    print(f"|                                                             Total  |{total} |")
    print("|==============================================================================|")  

# 4 listar as mercadorias cadastradas
class listarMercadoria:
  # 4.1 Lista as informações todas as mercadorias cadastradas no estoque
  def listar1(arrayEstoque):
    a=mercadoria()
    print("|  Nome do Produto  |  Preço  |  Código de Barras do Produto  |  Quantidade em Estoque  |")
    print("|=======================================================================================|")
    for i in range(len(arrayEstoque)):
      a.nomeMercadoria=arrayEstoque[i].nomeMercadoria.center(19)
      a.precoMercadoria=("R${:,.2f}".format((arrayEstoque[i].precoMercadoria)).center(9))
      a.codigoMercadoria=str(arrayEstoque[i].codigoMercadoria).center(31)
      a.quantidadeEstoque=str(arrayEstoque[i].quantidadeEstoque).center(25)
      print(f"|{a.nomeMercadoria}|{a.precoMercadoria}|{a.codigoMercadoria}|{a.quantidadeEstoque}|")
    print("|=======================================================================================|")

  def listar2(arrayEstoque):
    # 4.2 Lista as informações de um produto especificado pelo usuario
    existe=0
    a=mercadoria()
    codigoProduto=int(input("Digite o codigo do produto: "))
    for i in range(len(arrayEstoque)):                
      if codigoProduto==arrayEstoque[i].codigoMercadoria:
        existe= 1
        print("|  Nome do Produto  |  Preço  |  Código de Barras do Produto  |  Quantidade em Estoque  |")
        print("|=======================================================================================|")
        a.nomeMercadoria=arrayEstoque[i].nomeMercadoria.center(19)
        a.precoMercadoria=("R${:,.2f}".format((arrayEstoque[i].precoMercadoria)).center(9))
        a.codigoMercadoria=str(arrayEstoque[i].codigoMercadoria).center(31)
        a.quantidadeEstoque=str(arrayEstoque[i].quantidadeEstoque).center(25)
        print(f"|{a.nomeMercadoria}|{a.precoMercadoria}|{a.codigoMercadoria}|{a.quantidadeEstoque}|")

    if existe == 0:
      print("|=======================================================================================|")
      c=str("Produto não cadastrado").center(87)
      print(f"|{c}|")      
    print("|=======================================================================================|")

mercado=[]
codigoProduto=1

while True:
  op=menu()
  
  if op == 0:
    break
  
  if op == 1:
    novoProduto=cadastroMercadoria(codigoProduto)
    mercado.append(novoProduto)
    codigoProduto+=1
    continue
  
  if op == 2:
    if len(mercado)==0:
      print("Nenhum Produto Cadastrado!\n")
      continue
    else:
      listarMercadoria.listar1(mercado)
      atualizarMercadoria(mercado)
      continue
  
  if op == 3:
    if len(mercado)==0:
      print("Nenhum Produto Cadastrado!\n")
    else:
      caixa.iniciarCompra(mercado)
      continue
  
  if op == 4:
    if len(mercado)==0:
      print("Nenhum Produto Cadastrado!\n")
      continue
    else:
      listarMercadoria.listar2(mercado)
      continue
      
  if op== 5:
    if len(mercado)==0:
      print("Nenhum Produto Cadastrado!\n")
      continue
    else:
      listarMercadoria.listar1(mercado)
      continue
  
  else:
    print("Opção Inválida")
    continue