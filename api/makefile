requirements:
	poetry lock --no-update
	poetry export -f requirements.txt --without-hashes > requirements.txt
	poetry export -f requirements.txt --without-hashes --with dev > requirements-dev.txt