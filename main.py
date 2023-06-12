from CpfCnpj import Documento
from validate_docbr import CNPJ

#cpf_um = Cpf("15316264754")
#print(cpf_um)

exemplo_cnpj = "35379838000112"
exemplo_cpf = "11111111112"

#cnpj = CNPJ()
#print(cnpj.validate(exemplo_cnpj))
documento = Documento.cria_documento(exemplo_cpf)
print(documento)


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