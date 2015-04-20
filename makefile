cs:

config:
	git config -l

init:
	touch README
	git init
	git add README
	git commit -m 'first commit'
	git remote add origin git@github.com:gpdowning/cs373.git
	git push -u origin master

pull:
	@rsync -r -t -u -v --delete             \
	--include "Hello.js"                    \
	--include "Assertions.js"               \
	--include "Exceptions.js"               \
	--include "Arrays.js"                   \
	--exclude "*"                           \
	../../examples/javascript/ javascript
	@rsync -r -t -u -v --delete             \
	--include "Hello.py"                    \
	--include "Assertions.py"               \
	--include "UnitTests1.py"               \
	--include "UnitTests2.py"               \
	--include "UnitTests3.py"               \
	--include "Coverage1.py"                \
	--include "Coverage2.py"                \
	--include "Coverage3.py"                \
	--include "Exceptions.py"               \
	--include "Types.py"                    \
	--include "Operators.py"                \
	--include "Generators.py"               \
    --include "Iteration.py"                \
	--include "Iterables.py"                \
	--include "Variables.py"                \
	--include "Cache.py"                    \
	--include "FunctionKeywords.py"         \
	--include "FunctionDefaults.py"         \
	--include "FunctionUnpacking.py"        \
	--include "FunctionTuple.py"            \
	--include "FunctionDict.py"             \
	--include "GlobalVariables.py"          \
	--include "ClassVariables.py"           \
	--include "InstanceVariables.py"        \
	--include "Closures.py"                 \
	--include "Methods.py"                  \
	--include "Functions.py"                \
	--include "RegExps.py"                  \
	--exclude "*"                           \
	../../examples/python/ python
	@rsync -r -t -u -v --delete             \
	--include "IsPrimeT.py"                 \
	--include "IsPrimeT2.py"                \
	--include "Factorial.py"                \
	--include "Factorial2.py"               \
	--include "RMSE.py"                     \
	--include "RMSE2.py"                    \
	--include "Reduce.py"                   \
	--include "Reduce2.py"                  \
	--include "Map.py"                      \
	--include "Map2.py"                     \
	--include "Collatz2.py"                 \
	--include "Collatz3.py"                 \
	--include "Decorators.py"               \
	--include "Decorators2.py"              \
	--include "Select.py"                   \
	--include "Select2.py"                  \
	--include "Project.py"                  \
	--include "Project2.py"                 \
	--include "CrossJoin.py"                \
	--include "CrossJoin2.py"               \
	--include "ThetaJoin.py"                \
	--include "ThetaJoin2.py"               \
	--include "NaturalJoin.py"              \
	--include "NaturalJoin2.py"             \
	--exclude "*"                           \
	../../exercises/python/ python
	@rsync -r -t -u -v --delete             \
	--include "Bookstore1.xml"              \
	--include "Bookstore1.dtd.xml"          \
	--include "Bookstore2.dtd.xml"          \
	--include "Bookstore3.xml"              \
	--include "Bookstore3.xsd.xml"          \
	--exclude "*"                           \
	../../examples/xml/ xml
	@rsync -r -t -u -v --delete             \
	--include "Bookstore.json"              \
	--include "BookstoreSchema.json"        \
	--exclude "*"                           \
	../../examples/json/ json
	@rsync -r -t -u -v --delete             \
	--include "MySQL.txt"                   \
	--include "ShowDatabases.sql"           \
	--include "ShowGrants.sql"              \
	--include "ShowCharacterSet.sql"        \
	--include "ShowCollation.sql"           \
	--include "ShowVariables.sql"           \
	--include "ShowEngines.sql"             \
	--include "Create.sql"                  \
	--include "Select.sql"                  \
	--include "Join.sql"                    \
	--include "Joins.sql"                   \
	--include "Subqueries.sql"              \
	--include "Sets.sql"                    \
	--include "Aggregation.sql"             \
	--include "Insert.sql"                  \
	--include "Delete.sql"                  \
	--include "Update.sql"                  \
	--include "Other.sql"                   \
	--exclude "*"                           \
	../../examples/sql/ sql
	@rsync -r -t -u -v --delete             \
	--include "Store1.java"                 \
	--include "Store2.java"                 \
	--include "Store3.java"                 \
	--include "Store4.java"                 \
	--include "Store5.java"                 \
	--include "Store6.java"                 \
	--exclude "*"                           \
	../../examples/java/ java
	@rsync -r -t -u -v --delete             \
	--include "*.py"                        \
	--include "*.sql"                       \
	--include "*.txt"                       \
	--include "*.xml"                       \
	--exclude "*"                           \
	../quizzes/ quizzes
	@rsync -r -t -u -v --delete             \
	--include "collatz/"                    \
	--include "Collatz.py"                  \
	--include "gitignore.sample"            \
	--include "makefile.sample"             \
	--include "RunCollatz.py"               \
	--include "RunCollatz.sample.in"        \
	--include "RunCollatz.sample.out"       \
	--include "TestCollatz.py"              \
	--include "TestCollatz.sample.out"      \
	--exclude "*"                           \
	../../projects/python/ projects
	@rsync -r -t -u -v --delete             \
	--include "netflix/"                    \
	--include "gitignore.sample"            \
	--include "makefile.sample"             \
	--include "RunNetflix.sample.in"        \
	--include "RunNetflix.sample.out"       \
	--exclude "*"                           \
	../../projects/python/ projects

#	@rsync -r -t -u -v --delete             \
#	--include "Hello.js"                    \
#	--include "Assertions.js"               \
#	--include "Types.js"                    \
#	--include "Operators.js"                \
#	--include "Variables.js"                \
#	--exclude "*"                           \
#	../../examples/javascript/ examples/

#	@rsync -r -t -u -v --delete             \
#	--include "Join.sql"                    \
#	--include "Joins.sql"                   \
#	--exclude "*"                           \
#	../../examples/sql/ examples/

#	@rsync -r -t -u -v --delete             \
#	--include "MethodOverriding1.java"      \
#	--include "MethodOverriding2.java"      \
#	--include "Reflection.java"             \
#	--include "Store7.java"                 \
#	--include "Singleton.java"              \
#	--include "Creational.java"             \
#	--include "FactoryMethod.java"          \
#	--include "AbstractFactory.java"        \
#	--exclude "*"                           \
#	../../examples/java/ examples

#	--include "Equals.py"                   \
#	--include "Copy.py"                     \
#	--include "Complex.py"                  \
#	--include "Inheritance.py"              \
#	--include "Sequences.py"                \
#	--include "Lists.py"                    \
#	--include "Strings.py"                  \
#	--include "Sets.py"                     \
#	--include "Dicts.py"                    \
#	--include "Builder.py"                  \
#	--include "Prototype.py"                \
#	--include "Adapter.py"                  \
#	--include "Decorator.py"                \
#	--include "Composite.py"                \
#	--include "Visitor.py"                  \

#	--include "Sets.sql"                    \
#	--include "Aggregation.sql"             \
#	--include "Insert.sql"                  \
#	--include "Delete.sql"                  \
#	--include "Update.sql"                  \
#	--include "Other.sql"                   \

#	--include "Builder.java"                \
#	--include "Prototype.java"              \
#	--include "Adapter.java"                \
#	--include "Decorator.java"              \
#	--include "Composite.java"              \
#	--include "Visitor.java"                \

push:
	cd python; make clean
	git add .travis.yml
	git add java
	git add javascript
	git add json
	git add makefile
	git add package.json
	git add projects
	git add python
	git add quizzes
	git add sql
	git add xml
	git commit -m "another commit"
	git push
	git status

status:
	git branch
	git remote -v
	git status
