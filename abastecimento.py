from combustivel import obterPreco#importar apenas uma função especifica do dicionario 
from pagamento import verificarDesconto#importar apenas uma função especifica do dicionario 

def iniciarAbastecimento():
    tipo = input("Qual tipo de combustível você deseja? ").lower()
    litros = float(input("Quantos litros? "))

    preco = obterPreco(tipo)#atribuir o valor de preco atraves da função 

    if preco is None: #verificar se o preço foi definido ou se n recebeu nenhum valor
        print("Não temos esse combustível aqui")
    else:
        desconto = verificarDesconto()
        total_sem_desconto = preco * litros
        total_com_desconto = total_sem_desconto * (1-desconto)

        print(f"Preço por litro: R${preco}")
        print(f"Total sem desconto: R${total_sem_desconto}")
        print(f"Desconto aplicado de:{desconto * 100:.0f}%")
        print(f"O total a pagar ficou no valor de R${total_com_desconto}")
        print("Obrigado volte sempre!")


