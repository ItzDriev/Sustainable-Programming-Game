#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Lets play a game of "PIG, the Dice Game 🐷.

Your goal is to beat the opposing player
by reaching the target points before them!

During your turn, you can roll the dice as many times as you'd like,
however, if exactly ONE of your dice roll a '1',
all your points during that turn are lost.
If you happen to roll two '1's', all of you points will be reset to 0,
including points acquired from previous turns.

🐷 Play carefully, and don't be a PIG! 🐷  ⚀
"""

from PigGame import shell


def main():
    """Execute the main program."""
    print(__doc__)
    shell.Shell().cmdloop()


if __name__ == "__main__":
    main()
