MAX_MENU_OPTION = 1

from app.utils.input_validation import validate_option
from app.views.main_menu_view import MainMenuView

class MainMenuController:
    def __init__(self):
        self.view = MainMenuView()

    def run(self):
        while True:
            self.view.display_menu()
            option = input("Enter your choice: ")
            try:
                validate_option(option, MAX_MENU_OPTION)
            except ValueError as e:
                self.view.display_error_message()
                continue
            
            match int(option):
                case 1:
                    print("Player Management selected.")
                case 0:
                    self.view.display_exit_message()
                    break
                
        