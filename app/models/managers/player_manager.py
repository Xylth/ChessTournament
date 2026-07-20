import json
from typing import Optional
from app.config import PLAYER_DATA_FILE 
from app.models.entities.player import Player


class PlayerManager:
    def __init__(self):
        pass
        
    def get(self):
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

    def save(self, entry : Player):
        try:
            self.validate_unicity(entry)
        except ValueError as e:
            raise ValueError(f"Cannot add player: {e}")
        players = self.get()
        if (entry.get_id() == None):
            if len(players)>0:
                new_id = players[-1].get_id()+1
            else:
                new_id = 1
            entry.set_id(new_id)
            players.append(entry)
        else :
            players[int(entry.get_id())-1] = entry
        with open(PLAYER_DATA_FILE, "w") as f:
            json.dump([player.get_dict() for player in players], f, indent=4)
        return entry
    
    def validate_unicity(self, entry: Player):
        players = self.get()
        for player in players:
            if (player.get_first_name() == entry.get_first_name() and
                player.get_last_name() == entry.get_last_name() and player.get_id() != entry.get_id()):
                raise ValueError("Player name already exists.")
            if (entry.get_national_id()!="") and (player.get_national_id() == entry.get_national_id() and player.get_id() != entry.get_id()):
                raise ValueError("Player with this national ID already exists.")
