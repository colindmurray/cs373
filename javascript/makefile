all:

clean:
	rm -rf coverage

test:
	node Hello.js
	node Exceptions.js
	mocha -u tdd UnitTests3.js
	istanbul cover _mocha -- -u tdd Coverage1.js
	istanbul cover _mocha -- -u tdd Coverage2.js
	istanbul cover _mocha -- -u tdd Coverage3.js
	node Types.js
