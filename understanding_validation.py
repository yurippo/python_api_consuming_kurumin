# construímos uma classe que verifica se o CPF inserido pelo usuário é valido ou não. 
# Inicialmente, o documento foi validado somente pela quantidade de caracteres e, em seguida, por meio de um pacote que baixamos no PyPi(Python Package Index) https://pypi.org/

# A classe abaixo deve verificar o CPF inserido no momento que é instanciada:

from validate_docbr import CPF


class ValidaCpf:
    def __init__(self, documento):
        self.analisa_cpf(documento)

    def analisa_cpf(self, documento):
        if len(documento) == 11:
            valida_cpf = CPF()
            if valida_cpf.validate(documento):
                self.cpf = documento
                print('CPF valido')
            else:
                print('CPF inserido não é valido')
        else:
            print('Número de digitos incorreto')

cpf_um = '1235436791'
cpf_dois = 12354367912
cpf_tres = '12354367996'

# objeto_cpf_um = ValidaCpf(cpf_um )
# objeto_cpf_dois = ValidaCpf(cpf_dois )
# objeto_cpf_tres = ValidaCpf(cpf_tres )


#Para saber mais

# É importante que você esteja habituado a ler códigos de outras pessoas (tarefa comum no seu dia a dia de programador). Pensando nisso de uma olhada na classe e nos métododos Abra o Repositório da biblioteca e divirta-se!
# https://github.com/alvarofpp/validate-docbr/blob/main/validate_docbr/CPF.py

# Não se preocupe em entender perfeitamente como tudo está funcionando, mas é muito interessante que você dê uma lida no código 
