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
3. rode o comando `python run.py parse` com os parametros necessarios.
4. rode o comando `python run.py cataloguer` com os parametros necessarios.
5. Abra o arquivo **catalogo.html** e visualize o seu catalogo.

Nota: Se tiver algum animes que não foi encontrado, o nome do mesmo estará no arquivo *not-found.log*.

Nota[2]: Se quiser excluir uma ou mais folders, abra o arquivo *config.yaml* e adicione as folders no _exclude_


## Comandos: ##

O comando `python run.py` possui os seguintes argumentos:

- `parse`: _utilizado para baixar as descrições dos animes_. Esse argumento possui os seguintes parametros:

    - `--list_type "<list||folder>"`: utilizado para saber de onde virá a fonte de dados com os nomes dos animes.
        - **list**_(default)_: uma lista txt com o nome de cada anime por linha
        - **folder**: todas as subpastas de uma pasta específica será utilizada como nome dos animes
    - `--file '<nome do arquivo.txt>'`: utilizado para dizer qual arquivo será lido, necessário apenas quando o --list_type for list. Default='list.txt'
    - `--path '<path>'`: path da pasta onde ficam/ficaram os animes. Default='./'
    - `--override`: Se usado, irá sobreescrever as infos dos animes (descriação e thumb). Default=False.
    - `--create_folder`: Se usado, irá criar as pastas com o nome dos animes. Default=False.
    - `--only`: Se usado irá fazer o update da chave passada (Ex.: description). Obrigatorio o uso do _--override_. Para cada chave nova, o comando deverá ser repetido.
    - `--starts_with`: Se usado, começará a parsear os animes a partir da letra selecinada.
    - `--ends_with`: Usado para delimitar até que letra será parseados. Obrigatório o uso do _--starts_with_
    - `--just_with`: Se usado, apenas os animes começados com a letra selecionada serão parseados.
      - _Nota:_ Parse começa a partir da letra **a** e termina no número **9**. [a-z0-9]



+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=

O comando `make` possui os seguintes comandos:

- `cataloguer`: _utilizado para criar o arquivo com todos as info dos animes_. Esse argumento possui os seguintes parametros:

    - `folder=<nome da folder>`: nome da folder onde estao todos os animes. Default=Animes


## Exemplos de uso: ##

1. Parse

    1.1. Parse simples:
      - Atualizar via arquivo < arquivo.txt >
      - Path onde os animes estarão será '../Animes'
      - **Não** criará folders se não existirem
      - **Não** substituirá tudo dos arquivos.

    ```
        python run.py parse --file 'arquivo.txt' --path '../Animes/'
    ```

    1.2. Parse com update:
      - Atualizar via arquivo < arquivo.txt >
      - Path onde os animes estarão será '../Animes'
      - Criará folders se não existirem
      - Substituirá apenas os nomes e descrições dos arquivos.

    ```
        python run.py parse --file 'arquivo.txt' --path '../Animes/' --create_folder --override --only 'name' --only 'description'
    ```

    1.3. Parse com sobreescrita:
      - Atualizar via arquivo < arquivo.txt >
      - Path onde os animes estarão será '../Animes'
      - Criará folders se não existirem
      - Substituirá tudo dos arquivos.

    ```
        python run.py parse --file 'arquivo.txt' --path '../Animes/' --create_folder --override
    ```

    1.4. Parse com sobreescrita:
      - Atualizar via folders
      - Path onde os animes estarão será '../Animes'
      - Substituirá apenas os nomes, descrições e generos dos arquivos.

    ```
      python run.py parse --list_type 'folder' --path '../Animes/' --override --only 'name' --only 'description' --only 'genre'
    ```

    1.5. Parse inciado a partir de uma letra:
      - Atualizar via folders
      - Path onde os animes estarão será '../Animes'
      - Começará a partir da letra selecionada.

    ```
      python run.py parse --list_type 'folder' --path '../Animes/' --starts_with f
    ```

    1.6. Parse inciado a partir de uma letra e terminada em outra:
      - Atualizar via folders
      - Path onde os animes estarão será '../Animes'
      - Começará a partir da letra selecionada.
      - Terminará na letra selecionada.

    ```
      python run.py parse --list_type 'folder' --path '../Animes/' --starts_with d --ends_with k
    ```

    1.7. Parse apenas de uma letra:
      - Atualizar via folders
      - Path onde os animes estarão será '../Animes'
      - Começará e terminará na letra selecionada.

    ```
      python run.py parse --list_type 'folder' --path '../Animes/' --just_with p
    ```

2. Cataloguer

    2.1. Simples

      - Cria o catalogo com os dados que estao na pasta _Animes/_

    ```
        make cataloguer folder="Animes/"
    ```
