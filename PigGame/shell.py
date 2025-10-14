#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Using the cmd module to create a shell for the main program.

You can read about the cmd module in the docs:
    cmd — support for line-oriented command interpreters
    https://docs.python.org/3/library/cmd.html
"""

import cmd
from PigGame.game import Game
from PigGame.player import Player


class Shell(cmd.Cmd):
    """Classes that handle the terminal's user inputs."""

    intro = "Welcome to the PIG Game!. Type help or ? to list available commands.\n"
    prompt = "(Game) "

    def __init__(self):
        """Init the object."""
        super().__init__()
        self.game = Game()  # Game is a singleton persistant during "program" lifespan

    def do_start(self, mode):
        # 50/50 if computer goes first or if the human playing goes first?
        """Start a game versus the computer."""
        msg = "Game Started! Start off by rolling the dice!"

        players = []
        for _ in range(int(mode)):
            username = input("Enter username: ")
            self.game.data_handler.user_data.add_user(username)
            userid = self.game.data_handler.user_data.get_user_id(username)
            if userid is None:
                raise Exception("UserID Not Found!")

            players.append(Player(username, userid))
        if int(mode) == 1:
            print("Difficulties (1-4):\n😇 --- Easiest --- 😇\n\n1. Rasmus (Easy 😃)\n2. "
                  "Johan (Medium 😊)\n3. Anton (Hard 😠)\n4. "
                  "Liam (Expert 😡)\n\n😈 --- Hardest --- 😈")
            difficulty = 0
            while difficulty < 1 or difficulty > 4:
                try:
                    difficulty = (int(input("Select your difficulty: ")))
                except ValueError:
                    print("Must be an integer!")
        else:
            difficulty = None

        # Prompted to select 2 player mode or VS AI
        # Prompted to input name for player player 2 respectively
        print(msg)
        self.game.start(players, difficulty)

    def do_cheat(self, _):
        """Activates cheating for testing purposes."""
        Game.cheat_mode = True
        print("Cheat Mode Activated - You're a god daddy")

    def do_roll(self, _):
        """Decide to to roll the dice."""
        # Guess this will call a dice class, roll the dice and add the
        # points to the current dice hand or something

        print("You roll the dice!")

    def do_namechange(self, args):
        """Will perform a namechange."""
        name_info = args.split()

        if len(name_info) != 2:
            return  # Arguments were incorrect

        self.game.data_handler.user_data.update_username(name_info[0], name_info[1])

        print("You change your name lul xd")

    def help_namechange(self):
        """Provide help for namechange syntax."""
        print("Usage: namechange <currentUsername> <newUsername>")

    def do_rules(self, _):
        """Will explain the rules once again."""
        rules = """
        Your goal is to beat the opposing player
        by reaching the target points before them!

        During your turn, you can roll the dice as many times as you'd like,
        however, if exactly ONE of your dice roll a '1', all your points
        during that turn are lost. If you happen to roll two '1's', all of
        you points will be reset to 0, including points acquired from previous turns.
        """
        print(rules)

    # Below are all ways to exit the game: exit, quite, q and EOF

    def do_exit(self, _):
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

    def do_leaderboard(self, _):
        """Show leaderboard."""
        self.game.data_handler.print_leaderboard()
        # parameters = arg.split()
        # self.game.data_handler.leaderboard_data.register_highscore(parameters[0],
        # parameters[1])
        # print(self.game.data_handler.leaderboard_data.get_highscore(parameters[0]))
