# Introducao APIs e validação de CEP

# Faremos um resumo geral do que é uma API, afinal é um assunto bastante importante que provavelmente lidaremos em nosso dia-a-dia.

# Aqui na Plataforma Alura há diversos conteúdos sobre este tema, e é altamente recomendável se aprofundar, pois as empresas a estão utilizando cada vez mais e ter conhecimento sobre acesso e criação de APIs é muito benéfico no mercado de trabalho.

# Em resumo, os clientes acessam essa API enviando uma requisição http, seja get() para pegar informação, post() para criar, put() para atualizar algo que já existe ou delete() para deletar.

# A partir disso, a API acessa o sistema ou banco de dados e faz uma ação que retorna uma resposta. Se somente for encontrar uma resposta, o retorno será uma resposta serializada.

# Uma resposta serializada é em json ou xml e realiza a integração entre sistemas; com isso, poderemos pegá-la e mostrá-la à usuário ou usuário da forma que quisermos.

# Neste passo, acessaremos a API do ViaCEP - https://viacep.com.br/ para enviar o CEP dos clientes e receber o endereço completo. Afinal, nossa questão é a falta de informações sobre bairro, cidade e estado, visto que já é requisitado a rua, o número e o CEP.

# Para não precisarmos excluir este banco de dados e fazer outro novo, usaremos o ViaCEP para completar essas informações e suprir a demanda do ByteBank.

# No PyCharm, criaremos um novo arquivo Python chamado acesso_cep.py contendo a classe BuscaEndereco. Antes mesmo de acessarmos a API, precisaremos validar o CEP que será enviado.

# Definiremos cep_eh_Valido() recebendo self e cep. Caso o len() de cep for igual a 8, o retorno deverá ser True, e caso contrário será False.

# No topo do texto da classe, adicionaremos __init__() com self e cep também. O cep possuirá a versão str() dele mesmo, e passaremos para dentro do método cep_eh_Valido(). Se for válido, o self.cep é igual a cep, e lançaremos uma exceção se não for.

# class BuscaEndereco:

#     def __init__(self, cep):
#         cep = str(cep)
#         if self.cep_eh_Valido(cep):
#             self.cep = cep
#         else:
#             raise ValueError("CEP inválido!")

#     def cep_eh_Valido(self, cep):
#         if len(cep) == 8:
#             return True
#         else:
#             return False
        

# No arquivo main.py, importaremos essa classe e escreveremos a variável cep com um valor fictício 25870145 e um objeto_cep igual a BuscaEndereco() recebendo cep também.

# from acesso_cep import BuscaEndereco

# cep = 25870145
# objeto_cep = BuscaEndereco(cep)

# Ao rodar o código, nenhum erro nos é apresentado. Se retirarmos ou adicionarmos um dígito por exemplo, veremos a exceção sendo lançada conforme o esperado; portanto, a validação está funcionando corretamente.

# Agora poderemos fazer a máscara de formatação do CEP com format_cep(). Precisaríamos fazer o fatiamento, mas como se trata de um número pequeno, bastará retornar os dois componentes com "{}-{}". O primeiro grupo cep[] pegará de zero a cinco dígitos e o segundo de cinco em diante.

# Antes de testarmos, chamaremos o método format_cep() dentro da representação __str__() da classe.

# class BuscaEndereco:

#     def __init__(self, cep):
#         cep = str(cep)
#         if self.cep_eh_Valido(cep):
#             self.cep = cep
#         else:
#             raise ValueError("CEP inválido!")

#     def __str__(self):
#         return self.format_cep()

#     def cep_eh_Valido(self, cep):
#         if len(cep) == 8:
#             return True
#         else:
#             return False

#     def format_cep(self):
#         return "{}-{}".format(self.cep[:5],self.cep[5:])
    
    
# De volta ao main.py, imprimiremos o objeto_cep para visualizarmos o CEP devidamente formatado como estamos habituados.

# A seguir, aprenderemos como usar a biblioteca de fato. 