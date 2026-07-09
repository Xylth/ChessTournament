def validate_text_input(input: str, max_length: int, empty_allowed: bool = False) -> bool:
    if not isinstance(input, str):
        raise ValueError("Input must be a string")
    
    if len(input) == 0 and not empty_allowed:
        raise ValueError("Input cannot be empty")
    
    if len(input) > max_length:
        raise ValueError(f"Input exceeds maximum length of {max_length}")
    
    return True

def validate_numeric_input(input: str, min_value : int, max_value : int,size : int=0):
    try:
        number = int(input)
    except ValueError:
        raise ValueError("Input must be an integer")
    
    if size > 0 and len(input) != size:
        raise ValueError(f"Input must be exactly {size} digits long")
    
    if not (min_value <= number <= max_value):
        raise ValueError(f"Input must be between {min_value} and {max_value}")
    
    return True

