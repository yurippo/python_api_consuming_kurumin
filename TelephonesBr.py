import re
#biblioteca expressoaes regulares python

class TelephonesBr:
    def __init__(self,telephone):
        if self.valida_telephone(telephone):
            self.numero = telephone
        else:
            raise ValueError("Incorrect number")
 
 #in this class we worked with phone formatting using Regex that's another interesting way of validating we validate and then format using Regex
    
    def valida_telephone(self,telephone):
        
        padrao = "[0-9]{2,3}[0-9]{2}[0-9]{4,5}[0-9]{4}"
        resposta = re.findall(padrao,telephone)
        if resposta:
            return True
        else:
            return False