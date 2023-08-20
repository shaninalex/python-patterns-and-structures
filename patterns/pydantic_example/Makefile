start:
	python main.py 

unittest:
	python -m unittest main_test.py

coverage:
	coverage run -m unittest main_test

view_coverage:
	coverage report

format:
	black *.py

test: unittest coverage view_coverage