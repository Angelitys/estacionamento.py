
# Listagem das informações dos veiculos e as placas: utilizando o if e else para as informações necessarias do codigo.
veiculos_estacionados = []

def estacionar_veiculo(placa):
    if placa not in veiculos_estacionados:
        veiculos_estacionados.append(placa)
        print(f"Veículo {placa} estacionado com sucesso!")
    else:
        print(f"Veículo {placa} já está estacionado.")
# O def é utilizado para definir as funções dos veiculos estacionados;
def retirar_veiculo(placa):
    if placa in veiculos_estacionados:
        veiculos_estacionados.remove(placa)
        print(f"Veículo {placa} retirado com sucesso!")
    else:
        print(f"Veículo {placa} não está estacionado")
# Aqui o def é para retirar o veiculo .
def listar_veiculos_estacionados():
    if veiculos_estacionados:
        print("Veículos estacionados:")
        for veiculo in veiculos_estacionados:
            print(f"- {veiculo}")
    else:
        print("Não há veículos estacionados")
# a mesma coisa só  que para listar os veiculos estacionandos e a utilização do if e else para criar as condições necessárias.
def esta_estacionado(placa):
    if placa in veiculos_estacionados:
        print(f"Veículo {placa} está estacionado")
    else:
        print(f"Veículo {placa} não está estacionado")

def menu(): 
    while True:
        print("\Menu:")
        print("1 - Estacionar veiculo")
        print("2 - Retirar veículo")
        print("3 - Veiculos estacionados")
        print("4 - Está estacionado?")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")
# o print é utilizado para fazer a interação com o usuario, ou seja fazer com que gere a tabela que ele deve escolher.
        try:
            if opcao == "1":
                placa = input("Digite a placa do veiculo: ")
                estacionar_veiculo(placa)
            elif opcao == "2":
                placa = input("Digite a placa do veiculo: ")
                retirar_veiculo(placa)
            elif opcao == "3":
                listar_veiculos_estacionados()
            elif opcao == "4":
                placa = input("Digite a placa do veiculo: ")
                esta_estacionado(placa)
            elif opcao == "0":
                print("Saindo")
                break
            else:
                print("Opção inválida. Tente novamente.")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
            
# Placa do meu carro que já está estacionado
meu_carro = "ARIEL7070"
estacionar_veiculo(meu_carro)
menu()

#Na parte de cima é as opções que o  usuário deve escolher para o estacionamento do carro, ou a retirada.

