import json
from typing import Optional
from app.config import PLAYER_DATA_FILE 
from app.models.entities.player import Player


class PlayerManager:
    def __init__(self):
        self.load()
        
    def load(self):
        self.players = []
        try:
            with open(PLAYER_DATA_FILE, "r") as f:
                data = json.load(f)
                for element in data:
                    self.players.append(Player(**element))
        except json.JSONDecodeError:
            pass
        
    def save(self):
        with open(PLAYER_DATA_FILE, "w") as f:
            json.dump([player.get_dict() for player in self.players], f, indent=4)

    def create_player(self, first_name: str, last_name: str, birth_date: str, national_id: Optional[str] = None):
        player = Player(first_name, last_name, birth_date, national_id)
        try:
            self.validate_unicity(player)
        except ValueError as e:
            raise ValueError(f"Cannot add player: {e}")
        self.players.append(player)
        self.save()
        return player.get_dict()

    def read_all_players(self):
        return [player.get_dict() for player in self.players]
    
    def validate_unicity(self, new_player: Player):
        for player in self.players:
            if (player.get_first_name() == new_player.get_first_name() and
                player.get_last_name() == new_player.get_last_name() ):
                raise ValueError("Player name already exists.")
            if (new_player.get_national_id()!="") and (player.get_national_id() == new_player.get_national_id()):
                raise ValueError("Player with this national ID already exists.")
