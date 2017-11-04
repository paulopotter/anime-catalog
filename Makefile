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



# Add the following 'help' target to your Makefile
# And add help text after each target name starting with '\#\#'
# A category can be added with @category
# https://gist.github.com/prwhite/8168133

HELP_FUN = \
    %help; \
    while(<>) { push @{$$help{$$2 // 'options'}}, [$$1, $$3] if /^([a-zA-Z\-\$\(\)]+)\s*:.*\#\#(?:@([a-zA-Z\-\$\(\)]+))?\s(.*)$$/ }; \
    print "usage: make [target]\n\n"; \
    for (sort keys %help) { \
    print "${WHITE}$$_:${RESET}\n"; \
    for (@{$$help{$$_}}) { \
    $$sep = " " x (15 - length $$_->[0]); \
    print "  ${YELLOW}$$_->[0]${RESET}$$sep${GREEN}$$_->[1]${RESET}\n"; \
    }; \
    print "\n"; }

	# @echo -e "$$(grep -hE '^\S+:.*##' $(MAKEFILE_LIST) | sed -e 's/:.*##\s*/:/' -e 's/^\(.\+\):\(.*\)/\\x1b[36m\1\\x1b[m:\2/' | column -c2 -t -s :)"
# help: ##@miscellaneous Show this help.
# 	@perl -e '$(HELP_FUN)' $(MAKEFILE_LIST)
help: ## Show this help message.
	echo 'usage: make [target] ...'
	echo
	echo 'targets:'
	@egrep '^(.+)\:\ ##\ (.+)' ${MAKEFILE_LIST} | column -t -c 2 -s ':#'


setup: ##@Setup Instala as dependencias do projeto.
	@pip install -r requirements.txt

clean: ##@Setup Remove pyc e __pycache__.
	@echo "Cleaning up build, *.pyc and docs files..."
	@find . -name '*.pyc' -delete
	@find . -name '*__pycache__' -delete

cataloguer: ## Cataloga a coleção no arquivo HTML.
	@python run.py cataloguer --folder_name $(folder)

parse_file: ## Obtém informações dos animes.
	## Os animes serão buscados a partir de um arquivo com os nomes dos animes.
	@python run.py parse --file $(file) --path $(folder) $(filter-out $@,$(MAKECMDGOALS))

parse_file_update: ## Obtém informações dos animes.
	## Os animes serão buscados a partir de um arquivo com os nomes dos animes. As informações serão atualizadas.
	@python run.py parse --file $(file) --path $(folder) --override $(filter-out $@,$(MAKECMDGOALS))

parse_folder: ## Obtém informações dos animes.
	## Os animes serão buscados a partir de uma pasta que estarão com as pastas dos animes. As informações serão atualizadas.
	@python run.py parse --list_type 'folder' --path $(folder) --starts_with $(starts_with) --ends_with $(ends_with) --just_with $(just_with)

parse_folder_update: ## Obtém informações dos animes.
	## Os animes serão buscados a partir de uma pasta que estarão com as pastas dos animes. As informações serão atualizadas.
	@python run.py parse --list_type 'folder' --path $(folder) --override --only $(only) --starts_with $(starts_with) --ends_with $(ends_with) --just_with $(just_with)

rename: ## Renomeia as pastas dos animes.
	@python run.py rename --folder_name $(folder)
