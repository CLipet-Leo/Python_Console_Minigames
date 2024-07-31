class GameManager:
    def __init__(self):
        self.game = None
        self.players = []
        self.current_player = 0

    def add_player(self, player):
        self.players.append(player)

    def start_game(self, game):
        self.game = game

    def get_current_player(self):
        return self.players[self.current_player]

    def next_turn(self):
        self.current_player = (self.current_player + 1) % len(self.players)

    def play(self):
        while not self.game.is_over():
            player = self.get_current_player()
            move = player.get_move(self.game)
            self.game.make_move(move)
            self.next_turn()

        print("Game over! %s wins!" % self.get_current_player().name)