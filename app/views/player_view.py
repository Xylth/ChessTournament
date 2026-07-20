from tabulate import tabulate

class PlayerView:
    
    def __init__(self):
        print("Player Management Menu")
    
    def display_menu(self):
        print("Select an option:")
        print("1. Create Player")
        print("2. View All Players")
        print("0. Return to Main Menu")
        
    def display_players(self, players_data):
        if not players_data:
            print("No players found.")
            return
        print("All players :")
        print(tabulate(players_data, headers="keys"))
    
    def display_player_created(self, player_data):
        print("New player created:")
        print(tabulate(player_data, headers="keys"))
        
    def display_player_creation(self):
        print("Create a new player:")
        
    def display_request_first_name(self):
        print("Enter first name: ")
    
    def display_request_last_name(self):
        print("Enter last name: ")
        
    def display_request_birth_date(self):
        print("Enter birth date: ")
    
    def display_request_national_id(self):
        print("Enter national ID (optional): ")
                
    def display_error_message(self, e : ValueError, retry: bool = False):
        if retry:
            print(f"Error: {e}. Please try again.")
        else:
            print(f"Error: {e}.")
        
    def display_exit_message(self):
        print("Returning to Main Menu.") 