SHELL := /bin/bash
.PHONY: help

#COLORS
GREEN  := $(shell tput -Txterm setaf 2)
WHITE  := $(shell tput -Txterm setaf 7)
YELLOW := $(shell tput -Txterm setaf 3)
RESET  := $(shell tput -Txterm sgr0)

#Default variables
folder='../Animes/'
file='lista.txt'
create_folder=False
only=''
starts_with=''
ends_with=''
just_with=''

## ------ Setup


## Instala as dependencias do projeto.
setup:

	@pip install -r requirements.txt

## Remove pyc e __pycache__.
clean:
	@echo "Cleaning up build, *.pyc and docs files..."
	@find . -name '*.pyc' -delete
	@find . -name '*__pycache__' -delete

## Renomeia as pastas dos animes.
rename:
	@python run.py rename --folder_name $(folder)

## ------ Catalogar

## Cataloga a coleção no arquivo HTML.
cataloguer:
	@python run.py cataloguer --folder_name $(folder)


## ------ Obtém informações dos animes a partir de um arquivo com os nomes dos animes.

## Sem atualizar.
parse_file:
	@python run.py parse --file $(file) --path $(folder) $(filter-out $@,$(MAKECMDGOALS))

## Atualizando as informações dos animes.
parse_file_update:
	@python run.py parse --file $(file) --path $(folder) --override $(filter-out $@,$(MAKECMDGOALS))


## ------ Obtém informações dos animes a partir de uma folder com as folders de animes.


## Sem atualizar.
parse_folder:
	@python run.py parse --list_type 'folder' --path $(folder) --starts_with $(starts_with) --ends_with $(ends_with) --just_with $(just_with)

## Atualizando as informações dos animes.
parse_folder_update:
	@python run.py parse --list_type 'folder' --path $(folder) --override --only $(only) --starts_with $(starts_with) --ends_with $(ends_with) --just_with $(just_with)


test:
	@python -m unittest discover -s src


# ------------------------------------------

# Add the following 'help' target to your Makefile
# And add help text after each target name starting with '\#\#'
# A category can be added with @category
# https://gist.github.com/prwhite/8168133

help:
	@printf "Usage: make [target]\n";

	@awk '{ \
			if ($$0 ~ /^.PHONY: [a-zA-Z\-\_0-9]+$$/) { \
				helpCommand = substr($$0, index($$0, ":") + 2); \
				if (helpMessage) { \
					printf " ${GREEN}%s\n", \
						helpCommand, helpMessage; \
					helpMessage = ""; \
				} \
			} else if ($$0 ~ /^[a-zA-Z\-\_0-9.]+:/) { \
				helpCommand = substr($$0, 0, index($$0, ":")); \
				if (helpMessage) { \
					printf "${GREEN}%-20s\033[0m %s\n", \
						helpCommand, helpMessage; \
					helpMessage = ""; \
				} \
			} else if ($$0 ~ /^##/) { \
				if (helpMessage) { \
					helpMessage = helpMessage"\n                     "substr($$0, 3); \
				} else { \
					helpMessage = substr($$0, 3); \
				} \
			} else { \
				if (helpMessage) { \
					print "\n"helpMessage"\n" \
				} \
				helpMessage = ""; \
			} \
		}' \
		$(MAKEFILE_LIST)

