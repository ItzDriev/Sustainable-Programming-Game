#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Using the cmd module to create a shell for the main program.

You can read about the cmd module in the docs:
    cmd — support for line-oriented command interpreters
    https://docs.python.org/3/library/cmd.html
"""

import cmd
from pig_game.game.game import Game
from pig_game.game.player import Player
from pig_game.game.computer import Computer


class Shell(cmd.Cmd):  # noqa : H601
    """Classes that handle most of the terminal's user inputs."""

    intro = (
        "Welcome to the PIG Game!. Type help or ? to list available commands."
        "\n\nTo start a game simply enter 'start'"
    )
    prompt = "(🐷 Game): "

    def __init__(self):
        """Init the object."""
        super().__init__()
        self.game = Game()

    def do_start(self, _):
        """Start the game and takes three additional inputs.

        :param _: Placeholder argument.
        :type _: :py:obj:`None`

        :raises LookupError: If a player UserID cannot be found in user data.
        """
        msg = "Game Started! Start off by rolling the dice!"

        # Try to get amount of players for game until valid number.
        while True:
            mode = input(
                "Please enter amount of players! 1 = Vs AI, 2 = 2 Player mode: "
            ).strip()
            if mode in ("1", "2"):
                break
            print("Error please enter a valid amount of players (1 or 2)! 🐷")

        # Try to get target points for game until valid number.
        while True:
            target_points = input("Enter the target points for the game! 🐷: ").strip()
            if target_points.isdigit() is False:
                print("Please enter a valid number, any positive number!")
            else:
                target_points = int(target_points)
                break
        players = []

        # Ask for username, create user in data if not present,
        # add user to leaderboard data i not present.
        for _ in range(int(mode)):
            username = input("Enter username: ")
            self.game.turn_manager.data_handler.user_data.add_user(username)
            userid = self.game.turn_manager.data_handler.user_data.get_user_id(username)
            self.game.turn_manager.data_handler.leaderboard_data.add_new_player(userid)
            if userid is None:
                raise LookupError("UserID Not Found!")

            players.append(Player(username, userid))

        # Ask for Computer difficulty until valid number, only for 1 player mode.
        if int(mode) == 1:
            print(
                "Difficulties (1-4):\n😇 --- Easiest --- 😇\n\n1. Easy 😃\n2. "
                "Medium 😊\n3. Hard 😠\n4. "
                "Expert 😡\n\n😈 --- Hardest --- 😈"
            )
            while Computer.difficulty < 1 or Computer.difficulty > 4:
                try:
                    Computer.difficulty = int(input("Select your difficulty: "))
                except ValueError:
                    print("Must be an integer!")
        else:
            Computer.difficulty = None

        print(msg)
        self.game.start(players, target_points)

    def help_start(self):
        """Provide syntax for start command."""
        print("Usage: start")

    def do_cheat(self, _):
        """Activates cheating for testing purposes.

        :param _: Placeholder argument.
        :type _: :py:obj:`None`

        Immediately goes to the end of the game.
        """
        Game.cheat_mode = True
        print("Cheat Mode Activated - You're a god daddy")

    def help_cheat(self):
        """Provide syntax for cheat command."""
        print("Usage: cheat")

    def do_namechange(self, args):
        """Will perform a namechange.

        :param args: Arguments separated by spaces representing
                     current and new usernames.
        :type args: str
        """
        name_info = args.split()

        if len(name_info) != 2:
            return  # Arguments were incorrect

        self.game.turn_manager.data_handler.user_data.update_username(
            name_info[0], name_info[1]
        )

        print("You change your name lul xd")

    def help_namechange(self):
        """Provide syntax for namechange command."""
        print("Usage: namechange <currentUsername> <newUsername>")

    def do_rules(self, _):
        """
        Will explain the rules once again.

        :param _: Placeholder argument.
        :type _: :py:obj:`None`
        """
        rules = """
        Your goal is to beat the opposing player
        by reaching the target points before them!

        During your turn, you can roll the dice as many times as you'd like,
        however, if exactly ONE of your dice roll a '1', all your points
        during that turn are lost. If you happen to roll two '1's', all of
        you points will be reset to 0, including points acquired from previous turns.
        """
        print(rules)

    def help_rules(self):
        """Provide syntax for help command."""
        print("Usage: help")

    def do_leaderboard(self, arg):
        """Show leaderboard.

        :param arg: Argument for number of top players to display
                    (ex. "leaderboard 50" shows Top 50)
        :type arg: :py:obj:`str`
        """
        self.game.turn_manager.data_handler.print_leaderboard(arg)

    def help_leaderboard(self):
        """Provide syntax for help command."""
        print("Usage: leaderboard <amount>")

    # Below are all ways to exit the game: exit, quite, q and EOF
    def do_exit(self, _):
        """Leave the game.

        :param _: Placeholder argument.
        :type _: :py:obj:`None`

        :return: True, indicating game exit
        :rtype: :py:obj:`bool`
        """
        print("Game Exited! Cya around!")
        return True

    def help_exit(self):
        """Provide syntax for exit command."""
        print("Usage: exit")

    def do_quit(self, arg):
        """Leave the game.

        :return: True, indicating game exit
        :rtype: :py:obj:`bool`
        """
        return self.do_exit(arg)

    def help_quit(self):
        """Provide syntax for exit command."""
        print("Usage: quit")

    def do_q(self, arg):
        """Leave the game.

        :return: True, indicating game exit
        :rtype: :py:obj:`bool`
        """
        return self.do_exit(arg)

    def help_q(self):
        """Provide syntax for exit command."""
        print("Usage: q")

    def do_EOF(self, arg):
        # pylint: disable=invalid-name
        """Leave the game.

        :return: True, indicating game exit
        :rtype: :py:obj:`bool`
        """
        return self.do_exit(arg)
