class Menu:
    def display_main_menu(self):  # Fixed typo
        print("Main Menu")
        print("1. Start Game") 
        print("2. Exit")
        choice = input("Enter your choice (1 or 2): ")
        return choice

    def display_endgame_menu(self):
        menu_text = """
        Game Over!
        1. Restart Game 
        2. Quit Game
        Enter your choice (1 or 2): """
        choice = input(menu_text)
        return choice