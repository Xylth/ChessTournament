import json
from typing import Optional
from app.config import PLAYER_DATA_FILE 
from app.models.entities.player import Player


class PlayerManager:
    def __init__(self):
        pass
        
    def load(self):
        players = []
        try:
            with open(PLAYER_DATA_FILE, "r") as f:
                try:
                    data = json.load(f)
                    for element in data:
                        players.append(Player(**element))
                except json.JSONDecodeError:
                    pass
        except FileNotFoundError:
            pass
        return players
        
    def save(self, players : list[Player]):
        with open(PLAYER_DATA_FILE, "w") as f:
            json.dump([player.get_dict() for player in players], f, indent=4)

    def create_player(self, new_player : Player):
        try:
            self.validate_unicity(new_player)
        except ValueError as e:
            raise ValueError(f"Cannot add player: {e}")
        players = self.load()
        if len(players)>0:
            new_id = players[-1].get_id()+1
        else:
            new_id = 1
        new_player.set_id(new_id)
        players.append(new_player)
        self.save(players)
        players = self.load()
        return players[-1].get_dict()

    def read_all_players(self):
        players = self.load()
        return [player.get_dict() for player in players]
    
    def validate_unicity(self, new_player: Player):
        players = self.load()
        for player in players:
            if (player.get_first_name() == new_player.get_first_name() and
                player.get_last_name() == new_player.get_last_name() ):
                raise ValueError("Player name already exists.")
            if (new_player.get_national_id()!="") and (player.get_national_id() == new_player.get_national_id()):
                raise ValueError("Player with this national ID already exists.")
