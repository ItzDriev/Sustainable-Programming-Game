Usage
=====

.. _installation:

Installation
------------

Prerequisites:
^^^^^^^^^^^^^^^

* :ref:`chocolatey` (Windows)
* :ref:`gnu-make` (Windows)
* :ref:`graphviz`


.. _chocolatey:

Chocolatey
^^^^^^^^^^^

**Windows**:

`Link to chocolatey website <https://chocolatey.org/install>`_.

.. _gnu-make:

GNU Make
^^^^^^^^^^^

`Link to GNU Make installation website <https://community.chocolatey.org/packages/make>`_.

.. code-block:: powershell

   PS choco install make

Ensure make is installed:

.. code-block:: powershell

   make --version


.. _graphviz:

Graphviz
^^^^^^^^^^^

**Windows**:

`Link to Graphviz website <https://graphviz.org/download/>`_.

.. code-block:: powershell

   PS choco install graphviz

**Other**:

.. code-block:: powershell

   sudo apt-get update && sudo apt-get install -y graphviz

.. _project-setup:

Project setup
-------------

**Virtual Environtment setup**:

   1. Create venv, execute in project root:

   .. code-block:: bash

      $ make venv

   2. Activate venv, execute in project root:

   .. code-block:: bash

      Windows:
      $ . .venv/Scripts/activate
      Unix:
      $ . .venv/bin/activate
      Mac:
      $ . .venv/bin/activate

   3. Ensure venv is used:

   .. code-block:: bash

      $ which python
      /Sustainable-Programming-Game/.venv/*/python

**Install requirements**:

.. code-block:: bash

   (.venv) $ make install


.. _run-game:

Run Game
----------------

To run the game, use the ``pig_game.game.main.main()`` function:

.. autofunction:: pig_game.game.main.main
   :no-index:

For example:

>>> import pig_game
>>> pig_game.game.main.main()

**Launching the game**:

Using make command:

.. code-block:: bash

   (.venv) $ make game

Using python command:

.. code-block:: bash

   (.venv) $ python -m pig_game.game.main


.. _testing:

Testing
------------

This project uses linters and unittests.

**Run all tests**:

.. code-block:: console

   (.venv) $ make test

**Run unittests**:

Runs unittests, generates a coverage, html report and report in terminal.

.. code-block:: console

   (.venv) $ make coverage

**Run linters**:

Runs linters (flake8, pylint).

.. code-block:: console

   (.venv) $ make lint


* **Run flake8**:

Runs flake8.

.. code-block:: console

   (.venv) $ make flake8

* **Run pylint**:

Run pylint:

.. code-block:: console

   (.venv) $ make pylint

.. _documentation-generation:

Documenation generation
------------------------

The project provides tools for generating complete documentation of code, coverage and UML diagrams.

.. code-block:: console

   (.venv) $ make doc

Code documentation output is stored in `./doc/api/build/html`, open `index.html`.

UML diagrams output is stored in `./doc/pyreverse`.

Coverage report is stored in `./doc/coverage_report`, open `index.html`.

**Code documentation**:

Code documentation requires UML diagram and coverage report, therefore is run the same way was mentioned earlier.

.. code-block:: console

   (.venv) $ make doc

**UML Diagrams**:

Generates UML Diagrams of the game.

.. code-block:: console

   (.venv) $ make uml

UML diagrams output is stored in `./doc/pyreverse`.

**Coverage report**:

Generate coverage report.

.. code-block:: console

   (.venv) $ make coverage-html

Coverage report is stored in `./doc/coverage_report`, open `index.html`.
