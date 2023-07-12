import requests

cep = "20040030"
url =  'https://viacep.com.br/ws/{}/json'.format(cep)
r = requests.get(url)
print(r)
print(r.json())          


# cep = “20040030”
# url =  'https://viacep.com.br/ws/{}/json'.format(cep)
# r = requests.<método_HTTP>(url)

# utilizamos a biblioteca requests para fazermos requisições HTTP ao ViaCEP, uma API que retorna informações de endereço a partir do CEP. Com base nisso analise o código acima

# Para requisitar informações sobre o CEP, qual seria o método HTTP correto?
# O método GET retorna informações de algum recurso. Ele pode ser feito durante o envio de um formulário, mas sem alterar o banco de dados.

