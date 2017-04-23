setup:
	pip install -r requirements.txt

clean:
	@echo "Cleaning up build, *.pyc and docs files..."
	@find . -name '*.pyc' -delete
