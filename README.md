# Catalogo de animes #

Esse catalogo funciona lendo todas as pastas de um diretorio atras dos dados do anime e
cria um arquivo _js_ lido por um _html_ formatado.

## Requisitos: ##

- Python 3
- Virtualenv

## Como usar: ##

1. Baixe o projeto na pasta irmã da pasta onde estará a pasta com os animes.
  ```
    Ex.:
      /
        Animes
        Animes-catalog

  ```
2. Com a virtualenv levantada rode o comando `make setup`
3. rode o comando `make parse_file` ou `make parse_folder` com os parametros necessarios.
4. rode o comando `make cataloguer` com os parametros necessarios.
5. Abra o arquivo **catalogo.html** e visualize o seu catalogo.

Nota: Se tiver algum animes que não foi encontrado, o nome do mesmo estará no arquivo *not-found.log*.

Nota[2]: Se quiser excluir uma ou mais folders, abra o arquivo *config.yaml* e adicione as folders no _exclude_


## Comandos: ##

O comando `make` possui os seguintes comandos:

`parse`: _utilizado para baixar as descrições dos animes_. 

- make parse_**list**: Utiliza uma lista txt com o nome de cada anime por linha. Parâmetros:

  - `file='<nome do arquivo.txt>'`: utilizado para dizer qual arquivo será lido. Default='./list.txt' **OBRIGATÓRIO**

  - `folder='<path>'`: Caminho da pasta onde ficam/ficaram os animes. Default='./' **OBRIGATÓRIO**

  - `create_folder`: Se usado, irá criar as pastas com o nome dos animes. Default=False. _Opcional_
  
- make parse_**folder**: Utiliza todas as subpastas de uma pasta específica será utilizada como nome dos animes. Parâmetros:

  - `folder='<path>'`: Caminho da pasta onde ficam/ficaram os animes. Default='./' **OBRIGATÓRIO**

- Se acrescentar o **_update** no final dos comandos anteriores (parse_file_update, parse_folder_update ) ele irá executar um update nas informações que já existem. Parâmetro:

  - `only=<campo para ser atualizado>`: Se usado irá fazer o update da chave passada (Ex.: description). Para cada chave nova, o comando deverá ser repetido. _Opcional_


Parâmetros **opcionais** que podem ser utilizados nos comandos anteriores:
- `starts_with`: Se usado, começará a parsear os animes a partir da letra selecinada.
- `ends_with`: Usado para delimitar até que letra será parseados. Obrigatório o uso do _starts_with_
- `just_with`: Se usado, apenas os animes começados com a letra selecionada serão parseados.
  - _Nota:_ Parse começa a partir da letra **a** e termina no número **9**. [a-z0-9]


- make `cataloguer`: _utilizado para criar o arquivo com todos as info dos animes_. Esse argumento possui os seguintes parametros:

  - `folder=<nome da folder>`: nome da folder onde estao todos os animes. Default=Animes


## Exemplos de uso: ##

1. Parse

    1.1. Parse simples:
      - Atualizar via arquivo < arquivo.txt >
      - Path onde os animes estarão será '../Animes'
      - **Não** criará folders se não existirem
      - **Não** substituirá tudo dos arquivos.

    ```
        make parse_file file='arquivo.txt' folder='../Animes/'
    ```

    1.2. Parse com update:
      - Atualizar via arquivo < arquivo.txt >
      - Path onde os animes estarão será '../Animes'
      - Criará folders se não existirem
      - Substituirá apenas os nomes e descrições dos arquivos.

    ```
        make parse_file_update file='arquivo.txt' folder='../Animes/' create_folder only='name' only='description'
    ```

    1.3. Parse com sobreescrita:
      - Atualizar via arquivo < arquivo.txt >
      - Path onde os animes estarão será '../Animes'
      - Criará folders se não existirem
      - Substituirá tudo dos arquivos.

    ```
        make parse_file_update file='arquivo.txt' folder='../Animes/' create_folder
    ```

    1.4. Parse com sobreescrita:
      - Atualizar via folders
      - Path onde os animes estarão será '../Animes'
      - Substituirá apenas os nomes, descrições e generos dos arquivos.

    ```
      make parse_folder_update folder='../Animes/' only='name' only='description' only='genre'
    ```

    1.5. Parse inciado a partir de uma letra:
      - Atualizar via folders
      - Path onde os animes estarão será '../Animes'
      - Começará a partir da letra selecionada.

    ```
      make parse_folder folder='../Animes/' starts_with=f
    ```

    1.6. Parse inciado a partir de uma letra e terminada em outra:
      - Atualizar via folders
      - Path onde os animes estarão será '../Animes'
      - Começará a partir da letra selecionada.
      - Terminará na letra selecionada.

    ```
      make parse_folder folder='../Animes/' starts_with=c ends_with=k
    ```

    1.7. Parse apenas de uma letra:
      - Atualizar via folders
      - Path onde os animes estarão será '../Animes'
      - Começará e terminará na letra selecionada.

    ```
      make parse_folder folder='../Animes/' just_with=p
    ```

2. Cataloguer

    2.1. Simples

      - Cria o catalogo com os dados que estao na pasta _Animes/_

    ```
        make cataloguer folder="Animes/"
    ```
