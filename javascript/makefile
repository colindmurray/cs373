all:

test:
	mocha -u tdd Hello.js
	mocha -u tdd Exceptions.js
	mocha -u tdd Arrays.js
	mocha -u tdd UnitTests3.js
	istanbul cover _mocha -- -u tdd Coverage1.js
	istanbul cover _mocha -- -u tdd Coverage2.js
	istanbul cover _mocha -- -u tdd Coverage3.js
