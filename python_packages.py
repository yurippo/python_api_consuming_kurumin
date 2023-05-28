# Anteriormente, nossa validação apenas verificando a quantidade de dígitos no CPF não é suficiente para um resultado correto, e precisamos de algumas variáveis e lógicas para sabermos se o número é realmente válido dentro do sistema nacional.

# Para isso, acessaremos um algoritmo para validar CPF neste link https://dicasdeprogramacao.com.br/algoritmo-para-validar-cpf/


# Mais importante do que entender o algoritmo em si, é aprendermos como utilizar pacotes já prontos para aplicarmos em um projeto, como buscar ou como plugar para reutilizarmos os métodos de um pacote de classes.

# Estes estão dentro do Python Package Index ou PyPI e podem ser acessados através deste endereço https://pypi.org/


# Na barra de busca, escreveremos "valida cpf" e clicaremos na versão mais recente de validate-docbr para abri-lo em uma nova guia.

# Nesta página com maiores detalhes sobre a biblioteca, teremos o comando pip install validate-docbr que escreveremos no terminal para instalar o pacote que lida com CPF, CNPJ e CNS, além de plugá-lo em nosso código.

# Outra página importante do PyPI é a Homepage de Project links  https://github.com/alvarofpp/validate-docbr 

# que pode ser encontrada nesta mesma parte de detalhes da biblioteca validate-docbr, onde todos os códigos-fontes estarão presentes no GitHub do repositório deste pacote.

# Clicando na pasta de "validate_docbr" da lista, veremos o arquivo CPF.py com o código disponível para adaptarmos.

# Primeiro, instalaremos a biblioteca validate-docbr no terminal do PyCharm.

# Feito isso, apagaremos todo o conteúdo de main.py deixando somente a importação de Cpf. Na página principal do pacote PyPI, há uma pequena documentação que poderemos utilizar; começaremos importando e instanciando o objeto da classe importada para termos acesso ao método validate().

# Em seguida, imprimiremos cpf.validate() passando "012.345.678-90" que sabemos ser verdadeira por estar no exemplo do código presente na página do pacote. Como esta biblioteca é bem robusta, já possui a máscara correta com os pontos e hífen.

# from validate_docbr import CPF
# from cpf import Cpf

# cpf = CPF()

# print(cpf.validate("012.345.678-90"))


# Pegando o mesmo exemplo do passo anterior, tentaremos passar 11111111112 ao validate() com a certeza de que o resultado será falso. O mesmo acontecerá se tiver um dígito a mais ou a menos.

# Já sabemos o funcionamento básico desta biblioteca, e começaremos a passar sua lógica para dentro da nossa classe a seguir, afinal validate() precisará receber uma str e não um valor inteiro.