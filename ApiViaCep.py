import requests
def main():
#Cabeçalho
    print("##########################")
    print("########API ViaCEP########")
    print()

#Para o usuário digitar o CEP
    cep_input = input("Digite o CEP: ")
    while len(cep_input) != 8:
        print("Quantidade de caracteres inválido!")
        cep_input = input("Insira um CEP válido: ")
    
#fazendo a requisição e formatando o CEP digitado
    request = requests.get("https://viacep.com.br/ws/{}/json/".format(cep_input))
    address_data = request.json()

#Realiza busca no API ViaCep os dados condizentes 
#Caso esteja tudo certo, rodar o comando
    if "erro" not in address_data:
        print("  CEP ENCONTRADO!")

        print("CEP: {}" .format(address_data["cep"]))
        print("Rua/Avenida: {}" .format(address_data["logradouro"]))
        print("Complemento: {}" .format(address_data["complemento"]))
        print("Bairro: {}" .format(address_data["bairro"]))
        print("Cidade: {}" .format(address_data["localidade"]))
        print("Estado: {}" .format(address_data["uf"]))

#Se não estiver correto, vai dar mensagem de erro
    else:
        print("{}: CEP INVÁLIDO!" .format(cep_input))
        print("----------------------------------")

#Pergunta os usuário se ele deseja fazer uma nova consulta de CEP
    option = int(input("Realizar procura novamente? \n 1- Sim. \n 2- encerrar."))

    if option == 1 : 
        main()
    else:
        print ("Programa encerrando...")

#nome do ambiente nivel superior do programa
if __name__ == '__main__':
    main()
