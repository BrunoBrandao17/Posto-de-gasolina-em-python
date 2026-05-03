import combustivel
import pagamento
import abastecimento

def menu(): 
    while True:
        print("\n------MENU------")
        print("1. Cadastrar Combustível")
        print("2. Listar Combustíveis")
        print("3. Pesquisar Combustível")
        print("4. Alterar dados do Combustível")
        print("5. Abastecer Veículo")
        print("0. Sair")

        opcao = input("\nEscolha uma opção: ")

        match opcao: 
            case "1": combustivel.cadastroCombustivel()
            case "2": combustivel.listarCombustivel()
            case "3": combustivel.pesquisarCombustivel()
            case "4": combustivel.alterarDados()
            case "5": abastecimento.iniciarAbastecimento()
            case "0": 
                print("Sistema Encerrado")
                break
            case _: 
                print("Opção inválida")

menu()