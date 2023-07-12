from datetime import datetime, timedelta

agora = datetime.now()
agora_formatado = agora.strftime("%Y/%m/%d %H:%M:%S")

#print(agora)

print(agora_formatado)

#Qual o valor correto da variável formatacao para que o valor mostrado na tela tenha o seguinte formato: aaaa/mm/dd-hh:mm:ss ?

# vimos alguns dos caracteres importantes para podermos trabalhar com as datas. A lista utilizada está aqui também:

# Caracteres	Descrição	Exemplos
# %A	Dias da semana por extenso	Sunday, Monday, ...
# %d	Dias do mês	01, 02, ..., 31
# %m	Meses em formato de números	01, 02, ..., 12
# %y	Ano em formato de 2 dígitos	99, 15
# %Y	Ano em formato de 4 dígitos	1993, 2011
# %H	Hora em formato decimal	00, 01, ..., 23
# %M	Minuto em formato decimal	00, 01, ..., 59
# %S	Segundo em formato decimal	00, 01, ..., 59

# Como trabalhar com datas e horas no Python;
# Métodos da classe datetime;
# Para que serve o timedelta() e como utilizá-lo.