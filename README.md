# Catalogo de animes #

Esse catalogo funciona lendo todas as pastas ede um diretorio atras dos dados do anime e
cria um arquivo _js_ lido por um _html_ formatado.

## Requisitos: ##

- Python
- Virtualenv

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

- `cataloguer`: _utilizado para criar o arquivo com todos as info dos animes_. Esse argumento possui os seguintes parametros:

    - `--folder_name <nome da folder>`: nome da folder onde estao todos os animes. Default=Animes

## Como usar: ##

1. Baixe o projeto na mesma pasta onde estará a pasta com os animes.
2. Com a virtualenv levantada rode o comando `make setup`
3. rode o comando `python run.py parse` com os parametros necessarios.
4. rode o comando `python run.py cataloguer` com os parametros necessarios.
5. Abra o arquivo **catalogo.html** e visualize o seu catalogo.


## Exemplos de uso: ##

1. Parse

    1.1. Parse simples:
      - Atualizar via arquivo < arquivo.txt >
      - Path onde os animes estarão será '../Animes'
      - **Não** criará folders se não existirem
      - **Não** subistituirá tudo dos arquivos.

    ```
        python run.py parse --file 'arquivo.txt' --path '../Animes/'
    ```

    1.2. Parse com update:
      - Atualizar via arquivo < arquivo.txt >
      - Path onde os animes estarão será '../Animes'
      - Criará folders se não existirem
      - Subistituirá apenas os nomes e descrições dos arquivos.

    ```
        python run.py parse --file 'arquivo.txt' --path '../Animes/' --create_folder --override --only 'name' --only 'description'
    ```

    1.3. Parse com sobreescrita:
      - Atualizar via arquivo < arquivo.txt >
      - Path onde os animes estarão será '../Animes'
      - Criará folders se não existirem
      - Subistituirá tudo dos arquivos.

    ```
        python run.py parse --file 'arquivo.txt' --path '../Animes/' --create_folder --override
    ```

2. Cataloguer

    2.1. Simples

      - Cria o catalogo com os dados que estao na pasta _Animes/_

    ```
        python run.py cataloguer --folder_name "Animes/"
    ```
