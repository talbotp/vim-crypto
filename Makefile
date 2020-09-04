PYTHON = python3


test:
	${PYTHON} -m unittest tests/test_crypto.py
	echo "Test"

config:
	${PYTHON} scripts/create_config.py
	echo "Config created."


