#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Using the cmd module to create a shell for the main program.

You can read about the cmd module in the docs:
    cmd — support for line-oriented command interpreters
    https://docs.python.org/3/library/cmd.html
"""

import cmd
import game

class Shell(cmd.Cmd):
    """Classes that handle the terminal's user inputs"""

    intro = "Welcome to the PIG Game!. Type help or ? to list available commands.\n"
    prompt = "(Game) "

    def __init__(self):
        """Init the object."""
        super().__init__()
        self.game = game.Game()
    def do_start(self, _):
        # 50/50 if computer goes first or if the human playing goes first?

        """Start a game versus the computer"""
        msg = (
            "Game Started! Start off by rolling the dice!"
        )
        self.game.start()
        print(msg)

    def do_cheat(self, _):
        """This will cheat the game towards the end of it for testing purposes"""
        #Plan: Cheat the game to like 95% of the target points for both sides I guess or something?

        print("This will do some kind of cheat for the game")

    def do_roll(self, _):
        """Decide to to roll the dice"""
        #Guess this will call a dice class, roll the dice and add the points to the current dice hand or something 

        print("You roll the dice!")


    #Potentially add do_namechange
    def do_namechange(self, _):
        """Will perform a namechange"""

        print("You change your name lul xd")
    
    def do_rules(self, _):
        """Will explain the rules once again"""

        rules = """
        Your goal is to beat the opposing player 
        by reaching the target points before them!

        During your turn, you can roll the dice as many times as you'd like, 
        however, if exactly ONE of your dice roll a '1', all your points during that turn are lost. 
        If you happen to roll two '1's', all of you points will be reset to 0, 
        including points acquired from previous turns.
        """
        print(rules)

    #Below are all ways to exit the game: exit, quite, q and EOF

    def do_exit(self, _):
        # pylint: disable=no-self-use
        """Leave the game."""
        print("Game Exited! Cya around!")
        return True

    def do_quit(self, arg):
        """Leave the game."""
        return self.do_exit(arg)

    def do_q(self, arg):
        """Leave the game."""
        return self.do_exit(arg)

    def do_EOF(self, arg):
        # pylint: disable=invalid-name
        """Leave the game."""
        return self.do_exit(arg)
