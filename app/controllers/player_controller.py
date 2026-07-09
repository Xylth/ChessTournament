MAX_MENU_OPTION = 2

from datetime import datetime
from unittest import case
from unittest import case
from app.models.managers.player_manager import PlayerManager
from app.views.player_view import PlayerView
from app.utils.input_validation import validate_numeric_input, validate_text_input
from app.utils.data_validation import validate_birthdate

class PlayerController:
    def __init__(self):
        self.player_manager = PlayerManager()
        self.view = PlayerView()
        
    def run(self):
        while True:
            self.view.display_menu()
            option = input("Enter your choice: ")
            try:
                validate_numeric_input(option, 0, MAX_MENU_OPTION)
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
        status = 0
        birth_date = ["DD","MM","YYYY"]
        while True:
            current_birth_date = birth_date[0] + "/" + birth_date[1] + "/" + birth_date[2]
            match status:
                case 0:
                    self.view.display_player_creation()
                    status=1
                case 1 :
                    self.view.display_request_first_name()
                    data = input("")
                    try:
                        validate_text_input(data, 10)
                    except ValueError as e:
                        self.view.display_error_message(e, True)
                        continue
                    first_name = data.lower()
                    status = 2
                case 2:
                    self.view.display_request_last_name()
                    data = input("")
                    try:
                        validate_text_input(data, 10)
                    except ValueError as e:
                        self.view.display_error_message(e, True)
                        continue
                    last_name = data.lower()
                    status = 3
                case 3 :
                    self.view.display_request_birth_date()
                    birth_date = ["DD","MM","YYYY"]
                    status = 4
                case 4 :
                    self.view.display_current_birth_date(current_birth_date)
                    self.view.display_request_birth_date_year()
                    data = input("")
                    try :
                        validate_numeric_input(data,1900,datetime.now().year,4)
                    except ValueError as e:
                        self.view.display_error_message(e,True)
                        continue
                    birth_date[2]=data
                    status = 5
                case 5 :
                    self.view.display_current_birth_date(current_birth_date)
                    self.view.display_request_birth_date_month()
                    data = input("")
                    try :
                        validate_numeric_input(data,1,12,2)
                    except ValueError as e:
                        self.view.display_error_message(e,True)
                        continue
                    birth_date[1]=data
                    status = 6
                case 6 :
                    self.view.display_current_birth_date(current_birth_date)
                    self.view.display_request_birth_date_day()
                    data = input("")
                    try :
                        validate_numeric_input(data,1,31,2)
                    except ValueError as e:
                        self.view.display_error_message(e,True)
                        continue
                    birth_date[0]=data
                    status = 7
                case 7:
                    try:
                        validate_birthdate(current_birth_date)
                    except ValueError as e:
                        self.view.display_error_message(e,True)
                        status = 3
                        continue
                    status = 8
                case 8 :
                    self.view.display_request_national_id()
                    data=input("")
                    try:
                        validate_text_input(data,7,True)
                    except ValueError as e :
                        self.view.display_error_message(e,True)
                        continue
                    idn= data.upper()
                    status=9
                case 9:
                    try:
                        player = self.player_manager.create_player(first_name,last_name,current_birth_date,idn)
                    except ValueError as e:
                        self.view.display_error_message(e,False)
                        break
                    self.view.display_players([player])
                    break
                    
    def view_all_players(self): 
        players_data = self.player_manager.read_all_players()
        players_data = [{"id" : i+1, **d} for i,d in enumerate(players_data)] 
        self.view.display_players(players_data)