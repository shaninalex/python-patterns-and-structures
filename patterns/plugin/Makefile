start:
	python main.py 

unittest:
	python -m unittest *_test.py

coverage:
	coverage run -m unittest *_test

view_coverage:
	coverage report

format:
	black **/*.py

test: unittest coverage view_coverage