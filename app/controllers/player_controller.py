MAX_MENU_OPTION = 2

from app.models.managers.player_manager import PlayerManager
from app.models.entities.player import Player
from app.views.player_view import PlayerView
from app.utils import input_validation

class PlayerController:
    def __init__(self):
        self.player_manager = PlayerManager()
        self.view = PlayerView()
        
    def run_menu(self):
        while True:
            self.view.display_menu()
            option = input("Enter your choice: ")
            try:
                input_validation.validate_numeric_input(option, 0, MAX_MENU_OPTION)
            except ValueError as e:
                self.view.display_error_message(e,True)
                continue
            
            match int(option):
                case 1:
                    self.create_player_flow()
                case 2:
                    self.view_all_players()
                case 0:
                    self.view.display_exit_message()
                    break

    def create_player_flow(self):
        self.view.display_player_creation()
        
        while True: 
            self.view.display_request_first_name()
            data = input("").strip()
            data = data.lower()
            try:
                input_validation.validate_names(data)
            except ValueError as e:
                self.view.display_error_message(e, True)
                continue
            first_name = data
            break
        
        while True:
            self.view.display_request_last_name()
            data = input("").strip()
            data = data.lower()
            try:
                input_validation.validate_names(data)
            except ValueError as e:
                self.view.display_error_message(e, True)
                continue
            last_name = data
            break
        
        while True:
            self.view.display_request_birth_date()
            data = input("").strip()
            try:
                input_validation.validate_date_input(data)
                input_validation.validate_birth_date(data)
            except ValueError as e:
                self.view.display_error_message(e, True)
                continue
            birth_date = data
            break
        
        while True:
            self.view.display_request_national_id()
            data=input("").strip()
            try:
                input_validation.validate_national_id(data)
            except ValueError as e :
                self.view.display_error_message(e,True)
                continue
            idn = data
            break
        
        try:
            player = Player(None, first_name, last_name, birth_date, idn)
            new_player = self.player_manager.save(player)
            new_player_data = new_player.get_dict()
            self.view.display_player_created([new_player_data])
        except ValueError as e:
            self.view.display_error_message(e,False)
                    
    def view_all_players(self): 
        players = self.player_manager.get()
        players_data = [player.get_dict() for player in players]
        self.view.display_players(players_data)