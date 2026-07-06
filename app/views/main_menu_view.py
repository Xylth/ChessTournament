class MainMenuView:
    
    def __init__(self):
        print("Welcome to the Chess Tournament Manager")
    
    def display_menu(self):
        print("Select an option:")
        print("1. Player Management")
        print("0. Exit")

    def display_error_message(self):
        print("Invalid option. Please try again.")
        
    def display_exit_message(self):
        print("Closing the Chess Tournament Manager.") 
               