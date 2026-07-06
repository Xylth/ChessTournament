def validate_option(option: str, maximum_value: int) -> bool:
    try:
        option = int(option)
    except ValueError:
        raise ValueError("Option must be an integer")
    
    if 0 <= option <= maximum_value:
            return True
    else:
        raise ValueError("Option out of range")