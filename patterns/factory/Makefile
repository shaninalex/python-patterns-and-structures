start:
	python exporter.py 

unittest:
	python -m unittest exporter_test.py

coverage:
	coverage run -m unittest exporter_test

view_coverage:
	coverage report

format:
	black *.py

test: unittest coverage view_coverage