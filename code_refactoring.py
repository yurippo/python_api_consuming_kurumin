# A classe CpfCnpj é bastante grande e possui muitos métodos com uma lógica bem complexa no __init__(), o que dificulta sua legibilidade. Afinal, é importante que nosso código seja simples e de fácil entendimento.

# Em nosso caso, se quisermos colocar algum documento extra, o texto ficará ainda mais difícil com outro elif para verificar o tipo de documento e outra validação dentro da __str__().

# Neste cenário, há uma boa prática de programação chamada Factory; esta é responsável por chamar a classe certa que nosso objeto precisa. Ou seja, se passarmos um CNPJ, a Factory chamará a classe DocCnpj, e se passarmos um CPF, chamará a classe DocCpf.

# Na prática, transformaremos nossa grande CpfCnpj em três classes diferentes, cada uma com sua reusabilidade.

# No arquivo cpf_cnpj.py do PyCharm, criaremos uma nova classe Documento com um método estático chamado cria_documento() que receberá um documento.

# Para indicar à Factory que se trata de um CPF ou CNPJ, optaremos por utilizar o número de caracteres, sendo onze e quatorze respectivamente.

# Verificaremos se o len() do documento é igual a 11 para podermos retornar a classe DocCpf() que ainda não foi criada e será responsável pelo CPF, além de ser uma das três classes resultantes da transformação de CpfCnpj.

# Em seguida, verificaremos também para o caso do CNPJ com o tamanho de 14 dígitos, retornando a classe DocCnpj() que possuirá responsabilidade por este documento, e também não foi criada ainda.

# Caso o número não preencha esses quesitos, lançaremos a exceção ValueError com a mensagem "Quantidade de dígitos incorreta!".

# Agora pegaremos a grande CpfCnpj e a transformaremos em DocCpf e DocCnpj. Começando pela primeira, definiremos seu __init__() sem preenchê-lo a princípio, mas criaremos os demais métodos antes.

# O primeiro será valida() recebendo self e documento, verificando a validade por meio da biblioteca, como já fizemos em cpf_eh_Valido(). Então poderemos simplesmente copiar este bloco de código para o novo método, e não precisaremos mais verificar a quantidade de caracteres nesta parte.

# Para a formatação, definiremos outra variável format() sem precisar do documento. Também poderemos copiar e colar a máscara de CPF presente em format_cpf().

# O valida() deverá ser chamado em __init__() na verificação com if. Na linha seguinte, escreveremos self.cpf sendo igual a documento e, caso contrário, jogaremos uma exceção com a mensagem "cpf inválido!". Definindo o __str__() da classe, retornaremos o self.format().

# Todo o bloco da classe DocCpf pode ser adaptado para a nova classe DocCnpj na sequência. Por fim, poderemos apagar todo o texto de CpfCnpj.

# from validate_docbr import CPF, CNPJ

# class Documento:

#     @staticmethod
#     def cria_documento(documento):
#         if len(documento) == 11:
#             return DocCpf(documento)
#         elif len(documento) == 14:
#             return DocCnpj(documento)
#         else:
#             raise ValueError("Quantidade de dígitos incorreta!")

# class DocCpf:
#     def __init__(self, documento):
#         if self.valida(documento):
#             self.cpf = documento
#         else:
#             raise ValueError("Cpf inválido!")

#     def __str__(self):
#         return self.format()

#     def valida(self, documento):
#         validador = CPF()
#         return validador.validate(documento)

#     def format(self):
#       mascara = CPF()
#       return mascara.mask(self.cpf)

# class DocCnpj:
#     def __init__(self, documento):
#         if self.valida(documento):
#             self.cnpj = documento
#         else:
#             raise ValueError("Cnpj inválido!")

#     def __str__(self):
#         return self.format()

#     def valida(self, documento):
#         mascara = CNPJ()
#         return mascara.validate(documento)

#     def format(self):
#         mascara = CNPJ()
#         return mascara.mask(self.cnpj)

# Com este código salvo, retornaremos ao main.py para alterarmos a importação de CpfCnpj para Documento e de CpfCnpj() para Documento.cria_documento() que receberá somente o exemplo_cnpj. Comentaremos o exemplo_cpf para podermos imprimir o documento.

# from cpf_cnpj import Documento
# from validate_docbr import CNPJ

# #cpf_um = Cpf("15316264754")
# #print(cpf_um)

# exemplo_cnpj = "35379838000112"
# #exemplo_cpf = "11111111112"

# #cnpj = CNPJ()
# #print(cnpj.validate(exemplo_cnpj))
# documento = Documento.cria_documento(exemplo_cnpj)
# print(documento)


# Como resultado, visualizaremos o CNPJ já na formatação correta.

# Testaremos a mesma coisa com o CPF, descomentando a linha de cpf_um para retirar Cpf() e manter somente o número, para depois comentarmos a linha de exemplo_cnpj.

# from cpf_cnpj import Documento
# from validate_docbr import CNPJ

# cpf_um = "15316264754"
# #print(cpf_um)

# #exemplo_cnpj = "35379838000112"
# #exemplo_cpf = "11111111112"

# #cnpj = CNPJ()
# #print(cnpj.validate(exemplo_cnpj))
# documento = Documento.cria_documento(cpf_um)
# print(documento)

# A saída da impressão também apresenta a numeração já formatada corretamente.

# Se passarmos uma quantidade errada de dígitos ou um número inválido, o sistema também acusará o erro, lançando a exceção.

# Notaremos que nosso texto com as classes ficou bem mais fácil de ler, e é a partir de Documento que chamamos as demais classes com base no número de caracteres, e seus retornos serão onde o objeto irá instanciar.

# Desta forma, transformamos a antiga grande classe CpfCnpj em três mais simples e eficientes.

# A seguir, começaremos a entender a validação de número de telefone fixo e celular. Também usaremos uma máscara, mas usaremos expressões regulares para isso.

