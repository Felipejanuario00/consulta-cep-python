import requests

print("====================")
print("CONSULTA DE CEP")
print("====================")

continuar = "sim"

while continuar == "sim":

    cep = input("Digite o CEP: ").strip().replace("-", "")

    if len(cep) != 8 or not cep.isdigit():
        print("CEP inválido. Digite exatamente 8 números.")

    else:
        print(f"CEP informado: {cep}")

        url = f"https://viacep.com.br/ws/{cep}/json/"

        try:
            resposta = requests.get(url, timeout=5)
            dados = resposta.json()

        except requests.RequestException:
            print("Erro de conexão. Verifique sua internet e tente novamente.")
        else:
            if "erro" in dados:
                print("CEP não encontrado.")

            else:
                print(f"Cidade: {dados['localidade']}")
                print(f"Bairro: {dados['bairro']}")
                print(f"Rua: {dados['logradouro']}")
                print(f"Estado: {dados['uf']}")

    continuar = input("Deseja consultar outro CEP? (sim/não): ").lower()

print("Programa encerrado.")
   
 