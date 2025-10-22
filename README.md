# Sustainable Programming Game

**Sustainable Programming Game** is a Python project
designed to teach sustainable programming practices
through interactive gameplay.

## Table of content:

- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Project Setup](#project-setup)
- [Run Game](#run-game)
- [Testing](#testing)
- [Documentation Generation](#documentation-generation)
- [Documentation](#documentation)
- [Contributors](#contributors)

## About the project and implementation

## Installation

### Prerequisites:

- [Chocolatey (Windows)](#Chocolatey)
- [GNU Make (Windows)](#gnu-make)
- [Graphviz](#graphviz)

### Chocolatey

**Windows:**

Install chocolatey [Chocolatey](https://chocolatey.org/install).

### GNU Make

[Refernece.](https://community.chocolatey.org/packages/make)

```PowerShell
PS choco install make
```

Ensure make is installed:

```
make --version
```

### Graphviz

**Windows:**

[Reference.](https://graphviz.org/download/)

```PowerShell
PS choco install graphviz
```

**Other:**

```
sudo apt-get update && sudo apt-get install -y graphviz
```

### Project Setup

**Virtual Environtment setup**:

1. Create venv, execute in project root:

   ```bash
   $ make venv
   ```

2. Activate venv, execute in project root:

   ```bash
   Windows:
   $ . .venv/Scripts/activate
   Unix:
   $ . .venv/bin/activate
   Mac:
   $ . .venv/bin/activate
   ```

3. Ensure venv is used:

   ```bash
   $ which python
   /Sustainable-Programming-Game/.venv/*/python
   ```

**Instal requirements**:

```bash
(.venv) $ make install
```

---

Also visit project documentation page for installation intructions.
<a href="https://itzdriev.github.io/Sustainable-Programming-Game/usage.html#installation">
<img align="top" alt="Installation Badge" src="https://img.shields.io/badge/Installation-Link-blue">
</a>

## Run Game

**Launching the game**:

Using make command:

```
(.venv) $ make game
```

Using python command:

```
(.venv) $ python -m pig_game.game.main
```

## Testing

This project uses linters and unittests.

**Run all tests**:

```bash
(.venv) make test
```

**Run unittests**:

Runs unittests, generates a coverage, html report and report in terminal.

```bash
(.venv) make coverage
```

**Run linters**:

Runs linters (flake8, pylint).

```bash
(.venv) make lint
```

- **Run flake8**:

  Runs flake8.

  ```bash
  (.venv) make flake8
  ```

- **Run pylint**:

  Runs pylint.

  ```bash
  (.venv) make pylint
  ```

## Documentation generation

The project provides tools for generating complete documentation of code, coverage and UML diagrams.

```bash
(.venv) make doc
```

Code documentation output is stored in `./doc/api/build/html`, open `index.html`.

UML diagrams output is stored in `./doc/pyreverse`.

Coverage report is stored in `./doc/coverage_report`, open `index.html`.

**Code documentation**:

Code documentation requires UML diagram and coverage report, therefore is run the same way was mentioned earlier.

```bash
(.venv) make doc
```

**UML Diagrams**:

Generates UML Diagrams of the game.

```bash
(.venv) make uml
```

UML diagrams output is stored in `./doc/pyreverse`.

**Coverage report**:

Generate coverage report.

```bash
(.venv) make coverage-html
```

Coverage report is stored in `./doc/coverage_report`, open `index.html`.

## Documentation

<a href="https://itzdriev.github.io/Sustainable-Programming-Game/">
  <img align="top" alt="Static Badge" src="https://img.shields.io/badge/Documenation-Link-blue">
</a>

<br>

## Contributors

<a href="https://github.com/Flurry2005/Brogress/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=Flurry2005/Brogress" />
</a>
