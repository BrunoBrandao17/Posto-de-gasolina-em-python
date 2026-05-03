pagamento = {"dinheiro":True, "pix":True, "débito":True, "crédito":False} #false pra negar o desconto no crédito


def verificarDesconto():
    print("Olá, informamos que pagamentos feito no Débito, dinheiro ou pix tem 10% de desconto")

    while True: #loop caso caia no forma de pagamento inválida
        tipo = input("Forma de pagamento (dinheiro, pix, débito, crédito)? ").lower()

        if tipo in pagamento: #verificar se o tipo esta no dicionario pagamento
            if pagamento[tipo]:
                print("Desconto concedido ✅")
                return 0.1 #retornar um desconto de 10%
            else:
                print("Sem desconto ❌")
                return 0.0 #não retornar desconto
        else:
            print("Forma de pagamento inválida (⚠️  Não esqueça do acento  ⚠️  )")   