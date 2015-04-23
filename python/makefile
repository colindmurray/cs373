all:

clean:
	rm -f  .coverage
	rm -f  *.pyc
	rm -rf __pycache__

test:
	./Hello.py
	./UnitTests3.py
	coverage run --branch Coverage1.py
	coverage report -m
	coverage run --branch Coverage2.py
	coverage report -m
	coverage run --branch Coverage3.py
	coverage report -m
	./Types.py
	./Functions.py
