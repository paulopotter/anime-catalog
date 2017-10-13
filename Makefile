setup:
	@pip install -r requirements.txt

clean:
	@echo "Cleaning up build, *.pyc and docs files..."
	@find . -name '*.pyc' -delete

cataloguer:
	@python run.py cataloguer --folder_name $(folder)

parse_file:
	@python run.py parse --file $(file) --path $(folder) $(filter-out $@,$(MAKECMDGOALS))

parse_file_update:
	@python run.py parse --file $(file) --path $(folder) --override $(filter-out $@,$(MAKECMDGOALS))

parse_folder:
	@python run.py parse --list_type 'folder' --path $(folder) $(filter-out $@,$(MAKECMDGOALS))

parse_folder_update:
	@python run.py parse --list_type 'folder' --path $(folder) --override $(filter-out $@,$(MAKECMDGOALS))

rename:
	@python run.py rename --folder_name $(folder)
