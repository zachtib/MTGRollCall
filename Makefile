freeze:
	pip freeze | grep -Ev "^(pkg-resources|pylint|pep8)" > requirements.txt
