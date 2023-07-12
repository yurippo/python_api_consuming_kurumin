# Vamos criar uma máscara para aparelhos de telefone fixo e móvel utilizando as expressões regulares.

# Antes de começar a escrever algum código vamos definir a máscara da seguinte forma: +xxx(xx)xxxxx-xxxx. Tendo essa forma como base, vamos criar o padrão:

# Vamos primeiro cuidar da parte do número antes de fazer os códigos de área e de país.

# [0-9]{4,5}[0-9]{4}

# Perceba que a primeira parte pode conter 4 ou 5 dígitos. Agora vamos fazer as partes dos códigos de área e de país:
    
# [0-9]{2,3}[0-9]{2}[0-9]{4,5}[0-9]{4}

# Vamos separar o padrão em grupos:
    
# ([0-9]{2,3})([0-9]{2})([0-9]{4,5})([0-9]{4})

# Agora, vamos utilizar o format e o método group para construir a máscara:
    
    
# padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
# resposta = re.search(padrao, telefone)
# “+{}({}){}-{}”.format(resposta.group(1),  resposta.group(2), resposta.group(3), resposta.group(4))

# E, assim, construímos uma máscara para celular e telefone fixo utilizando expressões regulares.

# Fixando as regex

#  vimos alguns dos caracteres importantes para podermos trabalhar com as regex. A lista utilizada está aqui também:

# Caracteres	Descrição	Exemplos
# []	Define um range ou um grupo de caracteres	[0-9]; [a-z]; [abc]
# *	Marca nenhuma, uma ou mais ocorrências	sol*
# {}	Quantidade de repetições de uma ocorrência definida	[abc]{5}
# \d	Qualquer número de 0 até 9	\d{3,4}
# \w	Qualquer número de a té 9 letra de a até z ou _	\w{10}
# |	Um ou outro	@$
# ()	Captura e agrupa	(\w{4})
# Lembre que capturar em grupo utilizando os parênteses () é importante, pois deixa o padrão melhor explicado e mais fácil de ser controlado, além de os grupos poderem ser separados utilizando o método .group(index). Para se aprofundar nos caracteres da lista acima e, ainda, conhecer todos os outros que são utilizados pela biblioteca re, leia este texto da W3Scools, uma ótima fonte para vocês buscarem mais informações.

# Além desse link, quero deixar outras duas indicações legais para estudar a fundo o tema de expressões regulares: Python: Manipulação de Strings e Expressões regulares: Capturando textos de forma mágica.

#  https://www.w3schools.com/python/python_regex.asp
 
#  https://www.alura.com.br/curso-online-string-python-extraindo-informacoes-url
 
 
# Vimos:

# O que são expressões regulares;
# Como construir padrões e encontra-los dentro de textos;
# Como validar com expressões regulares;
# Como criar máscaras com expressões regulares.
