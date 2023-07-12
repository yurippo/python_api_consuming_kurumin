import requests
from datetime import datetime, timedelta
from DatesBr import DatesBr
from cep_access import BuscaAddress



#Test Accessing the CEP API from my Class BuscaAddress

#Second Test
new_cep = "01001000"

cep_object = BuscaAddress(new_cep)

#Testing returning dados from Class BuscaAddress

bairro, cidade, uf = cep_object.access_via_cep()

print(bairro,cidade,uf)
#Sé São Paulo SP Yay code working great
#Now our database is complete if the guys from bytebank in in doubt where to deliver the invoice 
#he runs bairro, cidade, uf = cep_object.access_via_cep() and will be able to discover the city, state and province
#there are many public APIs that we can keep trying to access that we can learn with this access
#Twitter's API is a very good example that we can control a lot of things we can publish things with Twitter
#It's just read the Twitter documentation documentation is always a very important word in everything we're gonna do
#in the universe of programming and technology


#a = cep_object.access_via_cep()

# print(type(a.text))
# #<class 'str'>

# print(type(a.json()))
#<class 'dict'>
#Json e um dictionary e eh muito mais facil extrair dados de um dictionary de que um text
#um dictionary eh uma extrutura de dados parecida com uma lista mas so que ao invez dos indices
#serem de 0 a n os indices sao nomeaveis
#exemplo trabalhando com indices nomeaveis em Json eu coloco por exemplo 'cep' e ele me retorna o valor relacionado a ele
#no caso o valor '01001-000'
#{'cep': '01001-000', 'logradouro': 'Praça da Sé', 'complemento': 'lado ímpar', 'bairro': 'Sé', 'localidade': 'São Paulo', 'uf': 'SP', 'ibge': '3550308', 'gia': '1004', 'ddd': '11', 'siafi': '7107'}
# print(a.json()) #retorna o nosso Json inteiro
# print(a.json()['cep']) #voila funcionou
# print(a.json()['logradouro'])
# print(a.json()['bairro'])
#se eu tivesse que buscar esses dados dentro de uma String eu precisaria usar o find ir fatiando a String ia dar muito mais trabalho
#que usar o dictionary
#agora vamos usar isso que aprendemos no nosso teste e implementar na nossa classe


# print(a)
# #that returned <Response [200]>

# print(type(a))
# #<class 'requests.models.Response'>

# print(dir(a)) #returns all the attributes and methods that this object posseds
#it's very nice to use it when we don't know with what we're working
#When we're using this library for the first time dir is very interesting because of that
#all the methods and attributs are here
#we can test them one by one but we already know that we're going to use 'json' to return this data
# in a way that we can work with it and show to the end users the neighborhood, city and state of the cep
#that is the data they need

# ['__attrs__', '__bool__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__nonzero__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_content', '_content_consumed', '_next', 'apparent_encoding', 'close', 'connection', 'content', 'cookies', 'elapsed', 'encoding', 'headers', 'history', 'is_permanent_redirect', 'is_redirect', 'iter_content', 'iter_lines', 'json', 'links', 'next', 'ok', 'raise_for_status', 'raw', 'reason', 'request', 'status_code', 'text', 'url']







#First Test
#new_cep = "25870145"
# new_cep = "01001000"

# cep_object = BuscaAddress(new_cep)

# cep_object.access_via_cep()
#it worked returned my URL https://viacep.com.br/ws/25870145/json/ sending my cep and getting a response
#first response with a non existing cep
# {
#   "erro": true
# }
#Second response with an existing cep Json returned
# {
#   "cep": "01001-000",
#   "logradouro": "Praça da Sé",
#   "complemento": "lado ímpar",
#   "bairro": "Sé",
#   "localidade": "São Paulo",
#   "uf": "SP",
#   "ibge": "3550308",
#   "gia": "1004",
#   "ddd": "11",
#   "siafi": "7107"
# }

#Test Making an API request

# r = requests.get("https://viacep.com.br/ws/01001000/json/")

# print(r) #returns the http status code
# #<Response [200]>
# print(r.text) #returns the Json responded by the API
# {
#   "cep": "01001-000",
#   "logradouro": "Praça da Sé",
#   "complemento": "lado ímpar",
#   "bairro": "Sé",
#   "localidade": "São Paulo",
#   "uf": "SP",
#   "ibge": "3550308",
#   "gia": "1004",
#   "ddd": "11",
#   "siafi": "7107"
# }

#print(type(r.text)) #returns the type of data returned in this case String
#<class 'str'> 

#Now we can work with this object returned

# new_cep = "25870145"

# cep_object = BuscaAddress(new_cep)

# print(cep_object)

# today = DatesBr()
# print(today.time_cadastro())

# hoje = datetime.today()
# amanha = datetime.today() + timedelta(days=1,hours=20)

# print(amanha - hoje)

# numero = 1

# string = "um"

# print(len(string))

#print(len(numero))
# cadastro = DatesBr()

# print(cadastro)

# hoje = datetime.today()

# hoje_formatado = hoje.strftime("%d/%m/%Y %H:%M") #To Format Date To Brazil's Style
# print(hoje)

# print(hoje_formatado)

# print(type(hoje_formatado))

# cadastro = DatesBr()

# print(cadastro.momento_cadastro)

# print(cadastro.month_cadastro())

# print(cadastro.day_cadastro())



# from datetime import datetime, timedelta

# print(datetime.today())




# from TelephonesBr import TelephonesBr
# import re #biblioteca expressoaes regulares python

# #Testing TelephonesBR and its class TelephonesBR

# telephone = "552126481234"

# telephone_objeto = TelephonesBr(telephone)


#creating a pattern to find phone number in Strings

# padrao_molde = "(xx)aaa-wwww"

# padrao = "[0-9]{2}[0-9]{4,5}[0-9]{4}"

# texto = "eu gosto do numero 2126451234 e gosto tambem do 2136431234"

# resposta = re.findall(padrao,texto) #find all brings all the correspondences of a pattern in a text and return us a list with all of the occurencies found
# print(resposta)


#Esse padraoserviria para todos os emails

#simple pattern to find an email in a sequence of characters

#pattern = "\w{5,50}@\w{3,10}.\w{2,3}.\w{2,3}" #more general code

# pattern = "\w{5,50}@[a-z]{3,10}.com.br" #more specific code work for this case way more specific lose a bit of the previous generalization and just works for .com.br in the end

# text = "aaabbbccc rodrigo123@gmail.com.br ufghjkljhgjtfghg huyfrtgrytyikjgilkn."

# response = re.search(pattern,text)
# print(response.group())





#first pattern test

# pattern = "[0-9][a-z][0-9]"

# text ="123 1a2 1cc aa1"

# response = re.search(pattern,text)

# print(response.group())



# from CpfCnpj import Documento
# from validate_docbr import CNPJ

# #cpf_um = Cpf("15316264754")
# #print(cpf_um)

# exemplo_cnpj = "35379838000112"
# exemplo_cpf = "11111111112"

# #cnpj = CNPJ()
# #print(cnpj.validate(exemplo_cnpj))
# documento = Documento.cria_documento(exemplo_cpf)
# print(documento)


# cnpj = CNPJ()

# print(cnpj.validate(cnpj_exemplo))

# one_cpf = Cpf("33451556804")
# print(one_cpf)



#Testing 
# cpf = CPF()

# print(cpf.validate("15316389752"))




# #We are using the code below to slice the cpf numbers that in this case is a String

# cpf = "15398745687"

# #new_cpf = "11111111112" Does it exist?

# cpf_object = Cpf(cpf)

# print(cpf_object)

#We've installed the library validate-docbr with pip install validate-docbr
#and also upgraded pip with
#python.exe -m pip install --upgrade pip


# slice_one = cpf[:3]
# print(slice_one)

# slice_two = cpf[3:6]
# print(slice_two)

# slice_three = cpf[6:9]
# print(slice_three)

# slice_four = cpf[9:]
# print(slice_four)


# #Now let's create a variable and set the slices inside of this new variable

# formated_cpf = "{}.{}.{}-{}".format(
#     slice_one,
#     slice_two,
#     slice_three,
#     slice_four
# )

# print(formated_cpf)




#Old tests

#cpf_object = Cpf(cpf)

#print(cpf_object)



# cpf = str(cpf)

# cpf_size = len(cpf)

# print(cpf_size)


#Venv creation

#python3 -m venv venv
#ai roda  venv\Scripts\activate