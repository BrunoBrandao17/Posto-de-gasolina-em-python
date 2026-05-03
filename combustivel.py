combustivel = {}

def cadastroCombustivel():
    tipo = input("Combustível: ")
    preco = float(input("Preço: R$"))
    combustivel[tipo] = {"combustivel": tipo, "preco": preco}
    print("Combustível e preço cadastrado!✅\n")


def obterPreco(tipo): 
    if tipo in combustivel: 
        return combustivel[tipo]['preco']
    return None


def listarCombustivel():    
    if not combustivel:
        print("#ERRO: Nenhum combustível cadastrado. ❌\n")
        return
    for tipo, dados in combustivel.items():
        print(f"Combustivel: {dados['combustivel']}  |  Preço: R$ {dados['preco']}")


def pesquisarCombustivel():
    tipo = input("Informe o tipo de combustível: ")
    if tipo in combustivel:
        print(f"Preço: R${combustivel[tipo]['preco']}")
    else:
        print("#ERRO: Combustível não encontrado. ❌")


def alterarDados():
    tipo = input("Informe o tipo de combustível para alterar: ")
    if tipo in combustivel:
        novo_tipo = input("Novo combustível: ") 
        novo_preco = float(input("Novo preço: R$"))

        del combustivel[tipo]#apagar os dados do combustível alterado
        combustivel[novo_tipo] = {"combustivel": novo_tipo, "preco": novo_preco}#atribuir novos dados
        
        print("Dados alterado com sucesso! ✅")
    else:
        print("#ERRO: Tipo de combustível não encontrado. ❌")