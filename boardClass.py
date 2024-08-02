class Board:
    def __init__(self):
        self.board = [str(i) for i in range(1, 10)]  # Fixed typo

    def display_board(self):
        for i in range(0, 9, 3):
            print(" | ".join(self.board[i:i+3]))  # Fixed typo
            if i < 6:
                print("-" * 11)

    def update_board(self, choice, symbol):  # Fixed typo
        if self.is_valid_move(choice):
            self.board[choice-1] = symbol
            return True
        return False

    def is_valid_move(self, choice):  # Fixed typo
        return self.board[choice-1].isdigit()

    def reset_board(self):  # Fixed typo
        self.board = [str(i) for i in range(1, 10)]