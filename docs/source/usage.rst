Usage
=====

.. _installation:

Installation
------------

**Virtual Environtment setup**

Set up a venv in the root directory.:

.. code-block:: console

   $ make venv

**Virtual Environtment activation**

Activate venv:

* On Unix and Mac, do:
   * . .venv/bin/activate
* On Windows (bash terminal), do:
   * . .venv/Scripts/activate

.. code-block:: console

   Windows:
   $ . .venv/Scripts/activate
   Unix:
   $ . .venv/bin/activate
   Mac:
   $ . .venv/bin/activate

To ensure the project contains all packages, first install the requirements using pip:

.. code-block:: console

   (.venv) $ pip install -r requirements.txt

Running the game
----------------

To run the game, use the ``pig_game.game.main.main()`` function:

.. autofunction:: pig_game.game.main.main
   :no-index:

For example:

>>> import pig_game
>>> pig_game.game.main.main()

Tests
------------


Run all tests:

.. code-block:: console

   (.venv) $ make test

Run unittests:

.. code-block:: console

   (.venv) $ make covarage

Run flake8:

.. code-block:: console

   (.venv) $ make flake8

Run pylint:

.. code-block:: console

   (.venv) $ make pylint

Documenation generation
------------------------

**Generating html documentation**

To generate the html documentation:

.. code-block:: console

   $ make sphinx

See our documentation in :ref:`Diagrams and Reports`.



