# SP Urbanismo - Croqui Fiscal
Este plugin visa a facilitar o trabalho de servidores públicos e pesquisadores ao terem que analisar a estrutura fundiária das quadras, por meio dos croquis fiscais. A contribuição está em permitir que o usuário consiga baixá-los pelo QGIS, selecionando um conjunto de quadras ou indicando uma lista de qudras de interesse.

### Diretório Padrão
É possível indicar um diretório padrão que sempre será usado como referência inicial para o local de armazenamento.

Para isso, deve-se criar um arquivo chamado "Diretorio_QuadrasFiscais.txt" na pasta do plugin e dentro deste arquivo texto deve-se inserir o diretório desejado. Exemplo: 

> C:\Users\Personal\Downloads\Quadras-CroquiFiscal


## Pendencias (TODO)
* Inserir o github nos arquivos (TRACK, ISSUE, Descrição do Plugin)
* Ajustar o METADADO
* Inserir a opção de fonte de dado pelo campo SQ
* Inserir campo para o tipo de quadra
* Avaliar se já existe o croqui na pasta padrão
* Verificar a sucesso do download
* Verificar limite de Requests
* Mudar o método para o QgsNetwork, devido o uso de proxy
* Transformar o campo de Lista de SQ em um campo multilinhas
