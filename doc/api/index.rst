Welcome to documentation for Sustainable Programming Game!
===========================================================

**Sustainable Programming Game** is a Python project
designed to teach sustainable programming practices
through interactive gameplay.

.. .. include:: README.md
..    :parser: myst


About the project and implementation
----------------------------------------
----------------------------------------

Game concept
^^^^^^^^^^^^^
Pig Dice Game is a turn-based dice rolling game inspired by the classic Pig rules. It is written in Python and played through a terminal interface such as Windows Command Prompt or PowerShell.

Shell
^^^^^^^^^^^^^
The game menu is accessed in shell.py which itself uses the CMD module to create a shell for the main program. It enables the user to start a new game, change username, display leaderboard and quit the game.

Data Handlers
^^^^^^^^^^^^^
To store usernames and leaderboard information the application saves and retrieves data locally in JSON format. It allows users to change their username across current and previous sessions. User scores are handled in the same way using local JSON storage.

Gameplay and intelligence
^^^^^^^^^^^^^
The game can either be played against an in-game intelligence in singleplayer mode or as a multiplayer game with an amount of 2 players.

In singleplayer mode, a difficulty level is choosable between 1-3. The in-game intelligence evaluate conditions and make decisions depending on the difficulty level.

A turn begins with the player rolling two dice. The turn may continue only if neither die shows a one. If the conditions are met, the player can choose to roll again or end their turn. A player who reaches the choosen target points first ultimately wins.


Contents:
-----------
------------

.. toctree::
   :maxdepth: 3

   usage
   pig_game
   temp