from typing import Optional
from app.utils.data_validation import validate_names, validate_birthdate, validate_national_id


class Player:
    def __init__(self, first_name: str, last_name: str, birth_date: str, national_id: Optional[str] = None):
        try:
            self.set_first_name(first_name)
            self.set_last_name(last_name)
            self.set_birth_date(birth_date)
            self.set_national_id(national_id)
        except ValueError as e:
            raise ValueError(f"Invalid player data: {e}")    
        
    def set_first_name(self, first_name: str):
        try:
            validate_names(first_name)
        except ValueError as e:
            raise ValueError(f"Invalid first name: {e}")
        self.first_name = first_name
    
    def set_last_name(self, last_name: str):
        try:
            validate_names(last_name)
        except ValueError as e:
            raise ValueError(f"Invalid last name: {e}")
        self.last_name = last_name
    
    def set_birth_date(self, birth_date: str):
        try:
            validate_birthdate(birth_date)
        except ValueError as e:
            raise ValueError(f"Invalid birth date: {e}")
        self.birth_date = birth_date
        
    def set_national_id(self, national_id: Optional[str]):
        try:
            validate_national_id(national_id)
        except ValueError as e:
            raise ValueError(f"Invalid national ID: {e}")
        self.national_id = national_id
        
    def get_first_name(self) -> str:
        return self.first_name
    
    def get_last_name(self) -> str:
        return self.last_name
    
    def get_birth_date(self) -> str:
        return self.birth_date
    
    def get_national_id(self) -> Optional[str]:
        return self.national_id
    
    def get_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birth_date": self.birth_date,
            "national_id": self.national_id
        }
        
        