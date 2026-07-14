from typing import Optional

class Player:
    def __init__(self, id: Optional[int], first_name: str, last_name: str, birth_date: str, national_id: str =""):
        self._id = id
        self._first_name = first_name
        self._last_name = last_name
        self._birth_date = birth_date
        self._national_id = national_id
        
    def set_id(self, id: Optional[int] = None):
        self._id = id
    
    def set_first_name(self, first_name: str):
        self._first_name = first_name
    
    def set_last_name(self, last_name: str):
        self._last_name = last_name
    
    def set_birth_date(self, birth_date: str):
        self._birth_date = birth_date
        
    def set_national_id(self, national_id: Optional[str]):
        self._national_id = national_id
        
    def get_id(self) -> Optional[str]:
        return self._id
    
    def get_first_name(self) -> str:
        return self._first_name
    
    def get_last_name(self) -> str:
        return self._last_name
    
    def get_birth_date(self) -> str:
        return self._birth_date
    
    def get_national_id(self) -> Optional[str]:
        return self._national_id
    
    def get_dict(self):
        return {
            "id": self._id,
            "first_name": self._first_name,
            "last_name": self._last_name,
            "birth_date": self._birth_date,
            "national_id": self._national_id
        }
        
        