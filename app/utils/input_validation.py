AGE_MIN = 18
AGE_MAX = 100

from re import match, search
from datetime import datetime
from typing import Optional

def validate_numeric_input(input: str, min_value : int, max_value : int):
    try:
        number = int(input)
    except ValueError:
        raise ValueError("Input must be an integer")
    
    if not (min_value <= number <= max_value):
        raise ValueError(f"Input must be between {min_value} and {max_value}")
    return True

def validate_date_input(input : str):
    buf_data = input.split("/")
    if len(buf_data)!=3:
        raise ValueError("Wrong format")
    if len(buf_data[0])!=2 or len(buf_data[1])!=2 or len(buf_data[2])!=4:
        raise ValueError("Wrong format")
    for element in buf_data: 
        if not (element.isdigit()):
            raise ValueError("Not a number")
    try:
        datetime(int(buf_data[2]), int(buf_data[1]), int(buf_data[0]))
    except ValueError:
        raise ValueError("Invalid date")
    
def validate_id(data : int):
    if not(isinstance(data,int)):
        raise ValueError("Not a int")
    if data < 0 :
        raise ValueError("Negative")
    
def validate_names(data : str):
        if not(isinstance(data,str)):
            raise ValueError("Not a string")
        if len(data)<1:
            raise ValueError("Empty")
        if len(data)>10:
            raise ValueError("Too long")
        data = data.lower()
        if not bool(match(r"^[a-zà-ÿ\s\-']+$", data)):
            raise ValueError("Invalid character")
        if search(r"[-' ]{2}", data):
            raise ValueError("Wrong usage of special character")
        if not bool(match(r"^[a-zà-ÿ](?:.*[a-zà-ÿ])?$", data)):
            raise ValueError("Wrong usage of special character")
        
def validate_birth_date(data : str):
    buf_data = data.split("/")
    current_date = datetime.now()
    age = current_date.year - int(buf_data[2])
    if current_date.month > int(buf_data[1]) or (current_date.month == int(buf_data[1]) and current_date.day > int(buf_data[0])):
        age -= 1
    if age < AGE_MIN:
        raise ValueError("Too young")
    if age > AGE_MAX:
        raise ValueError("Too old")

    
def validate_national_id(data : Optional[str]= None):
    if data is None:
        return None
    if not (isinstance(data,str)):
        raise ValueError("Not a string")
    if data == "" :
        return True
    if not (bool(match(r"^[A-Z]{2}\d{5}$", data))):
        raise ValueError("Wrong format")
    