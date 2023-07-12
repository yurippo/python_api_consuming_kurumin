import requests

cep = "01001000"

def retorna_endereco(cep):
    url = 'https://viacep.com.br/ws/{}/json'.format(cep)
    r = requests.get(url)
    dados = r.json()
    #print(dados)
    bairro = dados.get('bairro')
    cidade = dados.get('localidade')
    uf = dados.get('uf')
    print(dados)
    print(bairro,cidade,uf)
    

retorna_endereco(cep)

#Nesse projeto vimos vimos:

# O que são requisições HTTP;
# Para que serve e como acessar uma API;
# Como utilizar a biblioteca requests do Python;
# Acessar a API do ViaCEP e retornar informações do endereço a partir do CEP.
#https://viacep.com.br/