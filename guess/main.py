#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Lets play a game of "Pig, Dice Game".

Your job is to beat the opposing player, reaching the
target points before your opponent!

During your turn, you can roll the dice as many times as
you'd like, however, if you roll a single 1 all your points during
your turn are lost. If you roll two 1's, all of you points will be reset
to 0.

Play carefully, and don't become a Pig!

"""

import shell

def main():
    """Execute the main program."""
    print(__doc__)
    shell.Shell().cmdloop()

if __name__ == "__main__":
    main()
