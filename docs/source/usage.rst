Usage
=====

.. _installation:

Installation
------------

To ensure the project contains all packages, first install the requirements using pip:

.. code-block:: console

   (.venv) $ pip install -r requirements.txt

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

.. Creating recipes
.. ----------------

.. To retrieve a list of random ingredients,
.. you can use the ``lumache.get_random_ingredients()`` function:

.. .. autofunction:: lumache.get_random_ingredients

.. The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
.. or ``"veggies"``. Otherwise, :py:func:`lumache.get_random_ingredients`
.. will raise an exception.

.. .. autoexception:: lumache.InvalidKindError

.. For example:

.. >>> import lumache
.. >>> lumache.get_random_ingredients()
.. ['shells', 'gorgonzola', 'parsley']

