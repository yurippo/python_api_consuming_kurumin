import requests

class BuscaAddress:
    
    def __init__(self,cep):
        self.cep = str(cep)
        if self.cep_is_valid(cep):
            self.cep == cep
        else:
            raise ValueError("Invalid CEP!")
   
   #This class it validates a cep and formats a cep and we needed to access an API learned more about APIs,
   #access APIs through Python using Python's Requests Library we got this data from the server and were able
   #to show this data to the user the way we wanted collecting the data we wanted 
        
    def __str__(self):
        return self.format_cep()
        
    
    def cep_is_valid(self,cep):
        if len(cep) == 8:
            return True
        else:
            return False
        
    def format_cep(self):
        return "{}-{}".format(self.cep[:5],self.cep[5:])
    
    #now we're going to create a method that access the API passing the Attribute we have here
    
    def access_via_cep(self): #only self is enough because we're going to use our own attribute
        url = "https://viacep.com.br/ws/{}/json/".format(self.cep)
        #print(url)
        r = requests.get(url) #to make the request using our URL
        dados = r.json()
        #which dados bytebank needs? bairro, localidade and uf (estado)
        return (
            dados['bairro'],
            dados['localidade'],
            dados['uf']            
        )
    
    
# The Kurumin API Webservice that our code will access and GET data we don't have From
#in order to complete Data required in our Database and we don't have it
    
# ViaCEP - Webservice CEP e IBGE gratuito

# viacep.com.br
# https://viacep.com.br
# 
# Translate this page
# Webservice gratuito para consulta de endereço via CEP, suporta Ajax e retorno nos formatos JSON ou XML.
# Atualizar CEP ·Código Fonte (Javascript e Json) Módulos e Pacotes

# Acessando o webservice de CEP
# Para acessar o webservice, um CEP no formato de {8} dígitos deve ser fornecido, por exemplo: "01001000".
# Após o CEP, deve ser fornecido o tipo de retorno desejado, que deve ser "json" ou "xml" (exemple of serialization)

# Exemplo de pesquisa por CEP:
# viacep.com.br/ws/01001000/json/

#This URL for example returns the following JSON Object

# JSON
# URL: viacep.com.br/ws/01001000/json/

#     {
#       "cep": "01001-000",
#       "logradouro": "Praça da Sé",
#       "complemento": "lado ímpar",
#       "bairro": "Sé",
#       "localidade": "São Paulo",
#       "uf": "SP",
#       "ibge": "3550308",
#       "gia": "1004",
#       "ddd": "11",
#       "siafi": "7107"
#     }
    
# JSONP
# URL: viacep.com.br/ws/01001000/json/?callback=callback_name

#     callback_name({
#       "cep": "01001-000",
#       "logradouro": "Praça da Sé",
#       "complemento": "lado ímpar",
#       "bairro": "Sé",
#       "localidade": "São Paulo",
#       "uf": "SP",
#       "ibge": "3550308",
#       "gia": "1004",
#       "ddd": "11",
#       "siafi": "7107"
#     });

# XML
# URL: viacep.com.br/ws/01001000/xml/

#     <?xml version="1.0" encoding="UTF-8"?>
#     <xmlcep>
#         <cep>01001-000</cep>
#         <logradouro>Praça da Sé</logradouro>
#         <complemento>lado ímpar</complemento>
#         <bairro>Sé</bairro>
#         <localidade>São Paulo</localidade>
#         <uf>SP</uf>
#         <ibge>3550308</ibge>
#         <gia>1004</gia>
#         <ddd>11</ddd>
#         <siafi>7107</siafi>
#     </xmlcep>

#We have to use Python to extract this data from the API to be used by the organization
#and for that we're going to use the Requests Python Library

# Requests

# PyPI
# https://pypi.org › project › requests
# Installing Requests and Supported Versions. Requests is available on PyPI: $ python -m pip install requests. Requests officially supports Python 3.7+.

# Requests: HTTP for Humans™ — Requests 2.31.0 ...

# Read the Docs
# https://requests.readthedocs.io
# Requests officially supports Python 3.7+, and runs great on PyPy. The User Guide¶. This part of the documentation, which is mostly prose, begins with some ...


# This Library already comes native with Python all we have to do is to import the code and use it