#!/usr/bin/env make

# Change this to be your variant of the python command
# Set the env variable PYTHON to another value if needed
# PYTHON=python3 make version
PYTHON ?= python # python3 py

# Print out colored action message
MESSAGE = printf "\033[32;01m---> $(1)\033[0m\n"

all:


# ---------------------------------------------------------
# Check the current python executable.
#
version:
	@printf "Currently using executable: $(PYTHON)\n"
	which $(PYTHON)
	$(PYTHON) --version


# ---------------------------------------------------------
# Setup a venv and install packages.
#
venv:
	[ -d .venv ] || $(PYTHON) -m venv .venv
	@printf "Now activate the Python virtual environment.\n"
	@printf "On Unix and Mac, do:\n"
	@printf ". .venv/bin/activate\n"
	@printf "On Windows (bash terminal), do:\n"
	@printf ". .venv/Scripts/activate\n"
	@printf "Type 'deactivate' to deactivate.\n"

install:
	$(PYTHON) -m pip install -r requirements.txt

installed:
	$(PYTHON) -m pip list


# ---------------------------------------------------------
# Cleanup generated and installed files.
#
clean:
	@$(call MESSAGE,$@)
	rm -f .coverage *.pyc
	rm -rf __pycache__
	rm -rf htmlcov

clean-doc: clean
	@$(call MESSAGE,$@)
	rm -rf doc

clean-all: clean clean-doc
	@$(call MESSAGE,$@)
	rm -rf .venv


# ---------------------------------------------------------
# Work with static code linters.
#
pylint:
	@$(call MESSAGE,$@)
	-cd pig_game && $(PYTHON) -m pylint */*.py

flake8:
	@$(call MESSAGE,$@)
	-flake8

lint: flake8 pylint


# ---------------------------------------------------------
# Work with codestyle.
#
black:
	@$(call MESSAGE,$@)
	 $(PYTHON) -m black pig_game/ test/

codestyle: black


# ---------------------------------------------------------
# Work with unit test and code coverage.
#
unittest:
	@$(call MESSAGE,$@)
	 $(PYTHON) -m unittest discover

coverage:
	@$(call MESSAGE,$@)
	coverage run -m unittest discover
	coverage html -d doc/coverage_report
	coverage report -m

coverage-html:
	@$(call MESSAGE,$@)
	install -d doc/api/build/html/coverage_report
	coverage run -m unittest discover
	coverage html -d doc/coverage_report
	cp doc/coverage_report/*.* doc/api/build/html/coverage_report
#	mv doc/api/build/html/coverage_report/index.html doc/api/build/html/coverage_report/cover_index.html

coverage-xml:
	@$(call MESSAGE,$@)
	coverage run -m unittest discover
	coverage xml

test: lint coverage


# ---------------------------------------------------------
# Work with generating documentation.
#
.PHONY: pydoc
pydoc:
	@$(call MESSAGE,$@)
	install -d doc/pydoc
	$(PYTHON) -m pydoc -w pig_game/game/*.py
	mv *.html doc/pydoc

pdoc:
	@$(call MESSAGE,$@)
	pdoc --force --html --output-dir doc/pdoc pig_game/game/*.py

pyreverse:
	@$(call MESSAGE,$@)
	install -d doc/pyreverse
	pyreverse -o dot -p pig_game pig_game
	dot -Tpng classes_pig_game.dot -o doc/pyreverse/classes.png
	dot -Tpng packages_pig_game.dot -o doc/pyreverse/packages.png
	rm -f classes_pig_game.dot packages_pig_game.dot
	cp doc/pyreverse/classes.png doc/api

sphinx:
	@$(call MESSAGE,$@)
	install -d doc/api
	rm -f doc/api/pig_game*.rst
	curl -L https://raw.githubusercontent.com/ItzDriev/Sustainable-Programming-Game/main/README.md -o doc/api/README.md
	sphinx-apidoc -f -o doc/api ./pig_game --separate --no-toc --module-first
	$(MAKE) -C doc html

doc: pdoc pyreverse sphinx



# ---------------------------------------------------------
# Calculate software metrics for your project.
#
radon-cc:
	@$(call MESSAGE,$@)
	radon cc --show-complexity --average pig_game

radon-mi:
	@$(call MESSAGE,$@)
	radon mi --show pig_game

radon-raw:
	@$(call MESSAGE,$@)
	radon raw pig_game

radon-hal:
	@$(call MESSAGE,$@)
	radon hal pig_game

cohesion:
	@$(call MESSAGE,$@)
	cohesion --directory pig_game

metrics: radon-cc radon-mi radon-raw radon-hal cohesion



# ---------------------------------------------------------
# Find security issues in your project.
#
bandit:
	@$(call MESSAGE,$@)
	bandit --recursive pig_game
