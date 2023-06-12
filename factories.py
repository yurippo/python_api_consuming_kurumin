# o padrão de projeto Factory pode ser bastante útil em situações em que temos objetos que pertencem a classes semelhantes. É importante perceber que os métodos das subclasses da classe factory possuem os métodos com os nomes iguais! Dessa forma, podemos usar a factory sem se preocupar em qual classe foi instanciada.

# Esta explicação é uma simplificação desse padrão de projeto. Abaixo listei alguns artigos com explicações mais formais.

# Artigos em português:

#Artigo 1 - https://pt.wikipedia.org/wiki/Factory_Method


#Artigo 2 Artigos em inglês: https://sourcemaking.com/design_patterns/factory_method

# Artigo 3 (Site incrível!) https://sourcemaking.com/design_patterns/factory_method

# Artigo 4 https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Factory.html

# Os artigos estão ordenados do mais simples ao mais complexo. Recomendo a leitura de todos, pois esse padrão de projeto é bem comum no código de diversos sistemas.

# Construímos uma factory que decidia entre instanciar uma classe responsável por CPFs e outra por CNPJs. Uma das vantagens de usar esse padrão de projeto é facilitar o crescimento do código.

# A nova classe precisará ter todos os métodos com os mesmos nomes das outras classes filhas. Para conseguirmos usar qualquer instância retornada pelo Factory livremente, os métodos das classes filhas precisam ser iguais.