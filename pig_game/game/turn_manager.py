"""TurnManager module handles turns during the game."""

from time import sleep
from pig_game.game.player import Player
from pig_game.utils.data_handler import DataHandler
from pig_game.game.game_ui import GameUI
from pig_game.game.dice_hand import DiceHand
from pig_game.utils.dice_evaluator import DiceEvaluator
from pig_game.game.computer import Computer


class TurnManager:
    """Represents a manager handling turns during a game."""

    def __init__(self, dir_path, dice_emoji, game):
        """Inititializes needed instance variables.

        :param dir_path: Directory path, eg. './pig_game/GameData'.
        :type dir_path: :py:obj:`str`
        :param dice_emoji: String containing Unicode characters of dice.
        :type dice_emoji: :py:obj:`str`
        :param game: Reference to game instance.
        :type game: Game
        """
        self.data_handler = DataHandler(dir_path)
        self.game_ui = GameUI(dice_emoji)
        self.game = game

    def player_turn(
        self,
        player: Player,
        dice_hand: DiceHand,
        computer: Computer,
        test_mode,
    ):
        """Player(s) takes turn rolling dice.

        :param player: Current player rolling.
        :type player: Player
        :param dice_hand: Dice hand, handling rolling the dice.
        :type dice_hand: DiceHand
        :param computer: Computer, the player is playing against.
        :type computer: Computer
        :param test_mode: Boolean indicating if test mode is active.
        :type test_mode: :py:obj:`bool`
        """
        if self.game.cheat_mode:
            player.score += self.game.target_points
        turn_score = 0
        turn_history = (
            "🐷----------Turn History For:" + f"{player.get_username()}----------🐷\n"
        )

        while True:
            self.game_ui.clear_terminal()
            print(turn_history)

            dice_hand.roll_dice()
            computer.difficulties.increment_turn_round_for_player()
            dice_points = dice_hand.get_last_roll()

            self.game_ui.show_roll(player.get_username(), dice_points)

            # Evaluate if any roll is 1
            if not DiceEvaluator.rolled_one(dice_points[0], dice_points[1]):

                total_points = sum(dice_points)
                player.score += total_points
                turn_score += total_points
                if player.score >= self.game.target_points:
                    print(
                        f"🎉 {player.get_username()} reached"
                        f" {self.game.target_points} points. "
                        f"{player.get_username()} wins! 🎉\n"
                    )
                    self.game.game_over = True
                    computer.difficulties.reset_turn_score()
                    self.data_handler.leaderboard_data.update_ppt_and_turns(
                        player, turn_score
                    )
                    self.data_handler.leaderboard_data.update_games_played(True, player)

                    for p in self.game.players:
                        if p != player:
                            (
                                self.data_handler.leaderboard_data.update_games_played(
                                    False, p
                                )
                            )
                    break

                turn_history += (
                    f"Rolled: {dice_hand.get_last_roll()[0]}"
                    + f" and {dice_hand.get_last_roll()[1]}\n"
                )

                option = ""
                while option not in ["y", "n", "quit"]:
                    if not test_mode:
                        option = (
                            self.game_ui.prompt_next_action(
                                player.get_username(), player.score
                            )
                            .strip()
                            .lower()
                        )
                    else:
                        option = "n"
                    match option:
                        case "y":
                            break
                        case "n":
                            (
                                self.data_handler.leaderboard_data.update_ppt_and_turns(
                                    player, turn_score
                                )
                            )
                            return
                        case "quit":
                            self.game.quit_game(player)  # Prompts quit message
                            return  # Breaks loop and returns to start()

                    self.game_ui.clear_terminal()
                    print(turn_history)

            elif not DiceEvaluator.rolled_two_ones(
                dice_hand.get_last_roll()[0], dice_hand.get_last_roll()[1]
            ):
                computer.difficulties.reset_turn_score()
                self.data_handler.leaderboard_data.update_ppt_and_turns(player, 0)
                player.score -= turn_score
                print(
                    f"❌ Dang it! {player.get_username()} rolled 1."
                    f"Score will be reset down to {player.score} ❌"
                )
                sleep(2.5)
                break
            else:
                player.score = 0
                self.data_handler.leaderboard_data.update_ppt_and_turns(player, 0)
                print(
                    f"❌ Oh noooooo! {player.get_username()} rolled two 1's. "
                    f"Score will be reset down to {player.score} ❌"
                )
                sleep(2.5)
                break

    def npc_turn(self, computer: Computer, dice_hand: DiceHand):
        """Npc takes turn, sends result to the intelligence class.

        :param computer: Computer, the player is playing against.
        :type computer: Computer
        :param dice_hand: Dice hand, handling rolling the dice.
        :type dice_hand: DiceHand
        """
        turn_score = 0
        turn_history = "🐷----------Turn History For: Computer-AI----------🐷\n"

        while True:
            self.game_ui.clear_terminal()
            print(turn_history)
            player_score = self.game.players[0].score
            if computer.should_roll(player_score):
                dice_hand.roll_dice()
                self.game_ui.show_roll("🤖 Mr AI", dice_hand.get_last_roll())
            else:
                return False

            if not DiceEvaluator.rolled_one(
                dice_hand.get_last_roll()[0], dice_hand.get_last_roll()[1]
            ):
                total_roll = sum(dice_hand.get_last_roll())
                computer.score += total_roll
                turn_score += total_roll
                computer.difficulties.increment_turn_score(total_roll)

                if computer.score >= self.game.target_points:
                    print(
                        f"🤖 Mr AI reached {self.game.target_points} points. "
                        f"Game over 🤖\n"
                    )
                    self.game.game_over = True
                    computer.difficulties.reset_turn_score()
                    self.data_handler.leaderboard_data.update_games_played(
                        False, self.game.players[0]
                    )
                    break
                print(f"Mr AI's total score: {computer.score}")
                turn_history += (
                    f"Rolled: {dice_hand.get_last_roll()[0]}"
                    + f" and {dice_hand.get_last_roll()[1]}\n"
                )
                sleep(1)

            elif not DiceEvaluator.rolled_two_ones(
                dice_hand.get_last_roll()[0], dice_hand.get_last_roll()[1]
            ):
                computer.difficulties.reset_turn_score()
                computer.score -= turn_score
                print(
                    "❌ Mr AI rolled 1. His score will "
                    f"be reset down to {computer.score} ❌"
                )
                sleep(2.5)
                break
            else:
                computer.score = 0
                print(
                    f"❌ Oh noooooo! Mr. AI rolled two 1's. "
                    f"Score will be reset down to {computer.score} ❌"
                )
                sleep(2.5)
                break
        return True
