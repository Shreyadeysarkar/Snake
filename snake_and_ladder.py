import random

class Player:
    def __init__(self, player_id):
        self.player_id = player_id
        self.position = 0  # Starting position

class Board:
    def __init__(self, size):
        self.size = size
        self.snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
        self.ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

class Game:
    def __init__(self, board_size=100):
        self.board = Board(board_size)
        self.players = [Player(1), Player(2)]
        self.current_player_index = 0

    def roll_dice(self):
        return random.randint(1, 6)

    def move_token(self, player, steps):
        new_position = player.position + steps
        if new_position in self.board.snakes:
            player.position = self.board.snakes[new_position]
        elif new_position in self.board.ladders:
            player.position = self.board.ladders[new_position]
        else:
            player.position = min(new_position, self.board.size)

    def check_winner(self):
        for player in self.players:
            if player.position == self.board.size:
                return player
        return None

    def play(self):
        while True:
            current_player = self.players[self.current_player_index]
            print(f"Player {current_player.player_id}'s turn.")
            input("Press Enter to roll the dice...")
            steps = self.roll_dice()
            print(f"Player {current_player.player_id} rolled {steps}.")
            self.move_token(current_player, steps)
            print(f"Player {current_player.player_id} moved to square {current_player.position}.")
            winner = self.check_winner()
            if winner:
                print(f"Player {winner.player_id} wins!")
                break
            self.current_player_index = (self.current_player_index + 1) % len(self.players)

# Example usage
if __name__ == "__main__":
    game = Game()
    game.play()
