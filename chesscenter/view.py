class ChessView:
    @staticmethod
    def welcome():
        welcome_application = " Welcome to the << CHESS-CENTER >> application "
        print(f"\n{welcome_application.center(106, ' ')}")

    @staticmethod
    def instruction():
        instructions = " Please follow the instructions below "
        print(f"\n{instructions.center(106, ' ')}")

    @staticmethod
    def start_menu():
        start_menu = "> 1.Player  2.Tournament  3.Match  4.Quit <"
        print(f"\n{start_menu.center(106, '-')}")

    @staticmethod
    def exiting_program():
        information_decoration = " Exiting the program "
        print(f"{information_decoration.center(106, '*')}")
