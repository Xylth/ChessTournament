MAX_MENU_OPTION = 3

from app.utils.input_validation import validate_numeric_input
from app.views.main_menu_view import MainMenuView
from app.controllers.player_controller import PlayerController

class MainMenuController:
    def __init__(self):
        self.view = MainMenuView()

    def run_menu(self):
        while True:
            self.view.display_menu()
            option = input("Enter your choice: ")
            try:
                validate_numeric_input(option, 0, MAX_MENU_OPTION)
            except ValueError as e:
                self.view.display_error_message(e)
                continue
            
            match int(option):
                case 1:
                    player_controller = PlayerController()
                    player_controller.run_menu()
                case 2 :
                    print("tournament menu launched")
                case 3 :
                    print("report menu launched")
                case 0:
                    self.view.display_exit_message()
                    break
                
        