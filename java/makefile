%.class: %.java
	javac -Xlint $<

all:            \
	Store1.class

clean:
	rm -f *.class

test: all
	java -ea Store1
