# Mais sobre APIs

# Para entender mais como uma API funciona, é importante que tenhamos em mente o que é uma requisição HTTP (Hypertext Transfer Protocol), protocolo baseado em streams de texto. Sempre que acessamos uma página na web ou enviamos um formulário estamos usando o protocolo de forma transparente.

# Agora vamos entender como um requisição HTTP é composta:
    
# request line
# headers
# headers
# headers…

# body

# Apenas a request line é obrigatória, e perceba que o body vem após uma linha em branco.

# De modo geral uma request line se parece com algo assim:
    
# GET http://google.com/ HTTP/1.1
# <Método><Espaço><Endereço><Espaço><VersãoHTTP><Envio>

# Referência

# https://medium.com/clebertech/como-funciona-uma-requisi%C3%A7%C3%A3o-http-cf76f66fe36e

# Dentro da request line é importante destacar o método utilizado. Este método também é conhecido como verbo HTTP, que indica qual ação deve ser executada no servidor. Os verbos mais utilizados são os seguintes:

# GET: Solicita informações de um recurso; POST: Cria um recurso; PUT: Atualiza um recurso; DELETE: Remove um recurso. Referência

# https://www.alura.com.br/artigos/diferencas-entre-get-e-post?_gl=1*1fe7hy*_ga*MTI5NDc2NTA1MS4xNjgzNTkyNDg4*_ga_59FP0KYKSM*MTY4OTEwNjA1OC4xNDMuMS4xNjg5MTA3MjU3LjAuMC4w*_fplc*WndzZHNGbUx5aG1UMTNMT1dNNDFxc2FMTHVIa2ZuVFNyQjdnaElSRG4lMkZLNUd4dHljaEJjSUFtJTJCOSUyQjluRGxNJTJGZVMzWWlWa1VCazlkSW10Uzg1SkFOWGxwWWhUaWNDQWxZT3RkclJnN1NnbWpKT1dZTDRvVVFEQkF0TU03SXclM0QlM0Q.

# O header pode possuir a seguinte aparência:
    
# Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
# Accept-Encoding:gzip, deflate, br
# Accept-Language:en-US,en;q=0.9,pt;q=0.8
# Cache-Control:max-age=0
# Connection:keep-alive
# ...

# Os cabeçalhos têm a função de definir os parâmetros de uma requisição HTTP. Se você quiser entender mais a fundo quais são e para que servem os cabeçalhos fica aqui essa Referência.

# https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Headers

# O body possui a seguinte aparência:

# parametro=valor&outroparametro=outrovalor

# O body é passado através do HTTP quando enviamos um formulário. Consumir APIs começa com o entendimento do protocolo HTTP, então, se necessário, leiam mais de uma vez e tire dúvidas.
    