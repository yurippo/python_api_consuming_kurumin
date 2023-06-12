from validate_docbr import CPF, CNPJ

class Documento:
    
   # A classe CPF será chamada quando o documento conter 11 dígitos, e a classe CNPJ quando possuir 14.
   #1- Criamos a classe e definimos um método estático que decidirá qual classe instanciar:

    @staticmethod
    def cria_documento(documento):
        doc_str = str(documento)
        if len(doc_str) == 11:
            return DocCpf(doc_str)
        elif len(doc_str) == 14:
            return DocCnpj(doc_str)
        elif len(doc_str) == 20:
            return DocQualquer(doc_str)
        else:
            raise ValueError("Wrong Document!")
        
        
        # 1- Agora, criamos os condicionais:

class DocCpf:
    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError("Cpf inválido!")

    def __str__(self):
        return self.format()

    def valida(self, documento):
        validador = CPF()
        return validador.validate(documento)

    def format(self):
      mascara = CPF()
      return mascara.mask(self.cpf)

class DocCnpj:
    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError("Cnpj inválido!")

    def __str__(self):
        return self.format()

    def valida(self, documento):
        mascara = CNPJ()
        return mascara.validate(documento)

    def format(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)
    
    

# entendemos:

# Como utilizar mais uma classe da validate_docbr;
# O que é o padrão de projeto Factory;
# Como e quando implementar uma Factory em nosso código.
# Agora, vamos construir mais uma classe em nossa biblioteca, e dessa vez ela irá trabalhar com números de telefone e e-mails.

# class CpfCnpj:

#    def __init__(self,document,document_type):
#     self.document_type = document_type
#     document = str(document) 
#     if self.document_type == "cpf":
#        if self.cpf_is_valid(document):
#             self.cpf = document
#        else:
#           raise ValueError("Invalid CPF!!")
   
#     elif self.document_type == "cnpj":
#        if self.cnpj_is_valid(document):
#           self.cnpj = document
#        else:
#           raise ValueError("Invalid CNPJ!!")
#     else:
#        raise ValueError("Invalid DOCUMENT!!")
      
   
   
# #método dentro da representação string da classe   
#    def __str__(self):
#     if self.document_type == "cpf":
#      return self.format_cpf()
#     elif self.document_type == "cnpj":
#       return self.format_cnpj()
#     else:
#        raise ValueError ("Invalid DOCUMENT!!!")
   

# def cpf_is_valid(self,cpf):
   
#    if len(cpf) == 11:
#       validator = CPF()
#       return validator.validate(cpf)
#    else:
#       raise ValueError("The quantity of digits is invalid!!")
   
# def cnpj_is_valid(self,cnpj):
#       if len(cnpj) == 14:
#          validator = CNPJ()
#          return validator.validate(cnpj)
#       else:
#          raise ValueError("The quantity of digits is invalid!!")
   
# #New format method contido na biblioteca validate_docbr we did not reinvent the wheel we got from a place and plugged on our code
# # using the import and we have the advantage of the documentation Who created this library created with the documentation for who
# #would like to use it could use with no problems

# def format_cpf(self): 
#       mascara = CPF()
#       return mascara.mask(self.cpf)       
   

# #Old format method criado na unha :)
# #       
# #    def format_cpf(self):
# #        slice_one = self.cpf[:3]
# #        slice_two = self.cpf[3:6]
# #        slice_three = self.cpf[6:9]
# #        slice_four = self.cpf[9:]
# #        return(
# #            "{}.{}.{}-{}".format(
# #        slice_one,
# #        slice_two,
# #        slice_three,
# #        slice_four
# #          )
# #        )


# def format_cnpj(self): 
#    mascara = CNPJ()
#    return mascara.mask(self.cnpj)   
   
# # entendemos como:

# # Validar um documento pela quantidade de caracteres;
# # Encontrar, instalar e importar bibliotecas no PyPI;
# # Ler documentações de bibliotecas e utilizá-las em meus códigos  