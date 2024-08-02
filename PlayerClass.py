
class Player:  # Fixed typo
    def __init__(self):
        self.name = "" 
        self.symbol = "" 

    def choose_name(self):  # Removed parameter
        while True:
            name = input("Enter your name: ")  # Fixed typo
            if name.isalpha():
                self.name = name 
                break
            print("Invalid name")

    def choose_symbol(self):
        while True:
            symbol = input(f"{self.name}, choose your symbol: ")  # Fixed typo
            if symbol.isalpha() and len(symbol) == 1:
                self.symbol = symbol.upper()
                break
            print("Invalid symbol")