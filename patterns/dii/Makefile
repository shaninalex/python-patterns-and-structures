start:
	python dii.py 

unittest:
	python -m unittest dii_test.py

coverage:
	coverage run -m unittest dii_test

view_coverage:
	coverage report

format:
	black *.py

test: unittest coverage view_coverage